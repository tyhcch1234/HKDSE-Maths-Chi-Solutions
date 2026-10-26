#!/usr/bin/env python3
"""Rebuild index chips from actual files, update counts, prune broken pager links."""
import re, glob, os

YEAR = '2015'
pages = sorted(glob.glob('[0-9][0-9][0-9][0-9]_P*_Q*.html'))
total = len(pages)

s = open('index.html', encoding='utf8').read()
sec = re.search(r'<section id="y%s".*?</section>' % YEAR, s, re.S).group(0)
new = sec
for paper, label in (('P1', '卷一'), ('P2', '卷二')):
    nums = sorted(int(re.search(r'Q(\d+)\.html', f).group(1))
                  for f in glob.glob('%s_%s_Q*.html' % (YEAR, paper)))
    chips = ''.join('<a class="chip" href="%s_%s_Q%d.html">第%d題</a>' % (YEAR, paper, n, n) for n in nums)
    hdr = '<h3 class="paper-label">%s <span class="cnt">%d 題</span></h3>' % (label, len(nums))
    pat = r'<h3 class="paper-label">%s <span class="cnt">\d+ 題</span></h3>\s*<div class="chips">.*?</div>' % label
    new = re.sub(pat, hdr + '<div class="chips">' + chips + '</div>', new, flags=re.S)
s = s.replace(sec, new)
s = re.sub(r'共 \d+ 題', '共 %d 題' % total, s)
open('index.html', 'w', encoding='utf8').write(s)

# prune pager links whose target does not exist
for f in glob.glob('*.html'):
    if not re.match(r'\d{4}_P\d_Q\d+\.html$', f):
        continue
    t = open(f, encoding='utf8').read()
    def fix(m):
        return m.group(0) if os.path.exists(m.group(1)) else '<span></span>'
    t2 = re.sub(r'<a href="([^"]+\.html)">[^<]*(?:上一題|下一題)[^<]*</a>', fix, t)
    if t2 != t:
        open(f, 'w', encoding='utf8').write(t2)

# report broken links
bad = []
for f in pages:
    t = open(f, encoding='utf8').read()
    for m in re.finditer(r'(?:href|src)="(?!https?:|#|data:)([^"]+)"', t):
        if not os.path.exists(m.group(1)):
            bad.append((f, m.group(1)))
p1 = len(glob.glob('%s_P1_Q*.html' % YEAR))
p2 = len(glob.glob('%s_P2_Q*.html' % YEAR))
print('total=%d P1=%d P2=%d broken=%s' % (total, p1, p2, bad[:5]))
