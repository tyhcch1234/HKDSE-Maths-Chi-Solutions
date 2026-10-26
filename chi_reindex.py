#!/usr/bin/env python3
"""Rebuild index year sections + year pills from actual files, update totals,
prune dead pager links. Works for every year that has question pages."""
import re, glob, os

PAPERS = (('P1', '卷一'), ('P2', '卷二'))
MIN_PER_YEAR = 15  # 少於此題數的年份視為試作頁，暫不加入目錄
# 可選：只重建指定年份的頁籤，例如 CHI_YEARS=2012,2013,2024
ALLOW = [y.strip() for y in os.environ.get('CHI_YEARS', '').split(',') if y.strip()]

all_pages = sorted(glob.glob('[0-9][0-9][0-9][0-9]_P*_Q*.html'))
counts = {}
for f in all_pages:
    counts[f[:4]] = counts.get(f[:4], 0) + 1
years = sorted({f[:4] for f in all_pages if counts[f[:4]] >= MIN_PER_YEAR
                and (not ALLOW or f[:4] in ALLOW)}, reverse=True)
pages = [f for f in all_pages if f[:4] in years]
total = len(pages)


def section_for(year):
    blocks = []
    for paper, label in PAPERS:
        files = glob.glob('%s_%s_Q*.html' % (year, paper))
        nums = sorted(int(re.search(r'Q(\d+)\.html', f).group(1)) for f in files)
        if not nums:
            continue
        chips = ''.join('<a class="chip" href="%s_%s_Q%d.html">Q%d</a>'
                        % (year, paper, n, n) for n in nums)
        blocks.append('<h3 class="paper-label">%s <span class="cnt">%d 題</span></h3>'
                      '<div class="group">%s</div>' % (label, len(nums), chips))
    return ('<section id="y%s" class="year-section"><h2 class="year-head">%s</h2>%s</section>'
            % (year, year, ''.join(blocks)))


s = open('index.html', encoding='utf8').read()

# 1) rebuild year pills (descending)
pills = ''.join('<a href="#y%s" data-year="%s">%s</a>' % (y, y, y) for y in years)
if re.search(r'<nav class="years">.*?</nav>', s, re.S):
    s = re.sub(r'<nav class="years">.*?</nav>', '<nav class="years">' + pills + '</nav>',
               s, flags=re.S)
else:
    print('WARN: year nav not found')
    s = s.replace('<main>', '<main>\n<nav class="years">' + pills + '</nav>', 1)

# 2) replace or insert each year section
for y in years:
    sec = section_for(y)
    pat = r'<section id="y%s" class="year-section">.*?</section>' % y
    if re.search(pat, s, re.S):
        s = re.sub(pat, sec, s, flags=re.S)
    else:
        # insert before the first section of a smaller year, else before </main>
        later = [yy for yy in years if yy < y and
                 re.search(r'<section id="y%s"' % yy, s)]
        if later:
            anchor = re.search(r'<section id="y%s"' % later[0], s).start()
            s = s[:anchor] + sec + '\n\n' + s[anchor:]
        else:
            s = s.replace('</main>', sec + '\n\n</main>', 1)
        print('inserted section for', y)

# 3) drop sections for years that no longer exist
for y in re.findall(r'<section id="y(\d{4})"', s):
    if y not in years:
        s = re.sub(r'<section id="y%s" class="year-section">.*?</section>\s*' % y, '', s, flags=re.S)

# 4) total count
s = re.sub(r'共 \d+ 題', '共 %d 題' % total, s)
open('index.html', 'w', encoding='utf8').write(s)

# 5) prune pager links whose target does not exist
for f in glob.glob('*.html'):
    if not re.match(r'\d{4}_P\d_Q\d+\.html$', f):
        continue
    t = open(f, encoding='utf8').read()

    def fix(m):
        return m.group(0) if os.path.exists(m.group(1)) else '<span></span>'
    t2 = re.sub(r'<a href="([^"]+\.html)">[^<]*(?:上一題|下一題)[^<]*</a>', fix, t)
    if t2 != t:
        open(f, 'w', encoding='utf8').write(t2)

# 6) report broken internal links
bad = []
for f in pages:
    t = open(f, encoding='utf8').read()
    for m in re.finditer(r'(?:href|src)="(?!https?:|#|data:)([^"]+)"', t):
        if not os.path.exists(m.group(1)):
            bad.append((f, m.group(1)))

print('total=%d years=%s' % (total, ','.join(years)))
for y in years:
    print('  %s P1=%d P2=%d' % (y,
          len(glob.glob('%s_P1_Q*.html' % y)), len(glob.glob('%s_P2_Q*.html' % y))))
print('broken=%s' % (bad[:5] if bad else 'none'))
