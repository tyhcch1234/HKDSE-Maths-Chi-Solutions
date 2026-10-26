#!/usr/bin/env python3
"""把題目 card 內已有的 AI 自繪 SVG（inline svg）複製一份到題解 card。

用於「題目已有自繪圖、但題解沒有圖」的頁面：
  python3 copyfig.py PAGE...
圖解 card 已有 <svg> 的頁面會自動跳過。
"""
import hashlib
import re
import sys


def card_bounds(s, heading):
    m = re.search(r"<h2>\s*%s\s*</h2>" % heading, s)
    if not m:
        return None
    start = m.end()
    nxt = [s.find(x, start) for x in ('<div class="practice"', '<div class="card"', "<footer")]
    nxt = [x for x in nxt if x != -1]
    return start, (min(nxt) if nxt else len(s))


def dedupe_ids(block, tag):
    ids = set(re.findall(r'\sid="([^"]+)"', block))
    for i in ids:
        block = block.replace('id="%s"' % i, 'id="%s_%s"' % (i, tag))
        block = block.replace('url(#%s)' % i, 'url(#%s_%s)' % (i, tag))
    return block


def main():
    for page in sys.argv[1:]:
        s = open(page, encoding="utf-8").read()
        qb = card_bounds(s, "題目")
        sb = card_bounds(s, "題解")
        if not qb or not sb:
            print("SKIP (no card):", page)
            continue
        if "<svg" in s[sb[0]:sb[1]]:
            print("SKIP (already has figure):", page)
            continue
        withsvg = [m for m in re.finditer(r'<figure class="fig">.*?</figure>', s[qb[0]:qb[1]], re.S)
                   if "<svg" in m.group(0)]
        if not withsvg:
            print("SKIP (no svg in question):", page)
            continue
        block = withsvg[-1].group(0)
        tag = hashlib.md5(page.encode()).hexdigest()[:6]
        block = dedupe_ids(block, tag)
        block = block.replace('<figure class="fig">', '<figure class="fig fig-solution">', 1)
        ins = "\n    " + block + "\n"
        s = s[:sb[0]] + ins + s[sb[0]:]
        open(page, "w", encoding="utf-8").write(s)
        print("COPIED:", page)


if __name__ == "__main__":
    main()
