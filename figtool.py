#!/usr/bin/env python3
"""把「AI 親自繪畫」的 SVG 示意圖插入某一頁的題解 card。

用法：
  python3 figtool.py PAGE.html --svg /tmp/fig.svg --caption "圖：…" [--anchor "第 2 步"] [--force]

規則：
  * 圖一定插入 <h2>題解</h2> 所屬的那個 card 之內（不是題目 card）。
  * --anchor 給「第 N 步」時，插在該 step 之前；否則插在 <h2>題解</h2> 之後。
  * 題解 card 內已有 <svg> 時會拒絕（除非 --force），避免重複插圖。
"""
import argparse
import re
import sys


def solve_card_bounds(s):
    m = re.search(r"<h2>\s*題解\s*</h2>", s)
    if not m:
        sys.exit("找不到 <h2>題解</h2>")
    start = m.end()
    # card 以 <div class="card"> 開始，到對應的 </div> 前，題解 card 之後通常是 <div class="practice"> 或 </div></div>
    end = len(s)
    for pat in ('<div class="practice"', '<div class="ans"'):
        pass
    # 用下一個 card / practice / footer 作界線
    nxt = [s.find(x, start) for x in ('<div class="practice"', '<div class="card"', "<footer")]
    nxt = [x for x in nxt if x != -1]
    if nxt:
        end = min(nxt)
    return start, end


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("page")
    ap.add_argument("--svg", required=True)
    ap.add_argument("--caption", required=True)
    ap.add_argument("--anchor", default="")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    s = open(a.page, encoding="utf-8").read()
    start, end = solve_card_bounds(s)
    card = s[start:end]

    if "<svg" in card and not a.force:
        sys.exit("題解 card 內已有 <svg>，未插入（要覆寫請加 --force）")

    svg = open(a.svg, encoding="utf-8").read().strip()
    svg = re.sub(r"<\?xml.*?\?>", "", svg, flags=re.S).strip()
    block = ('\n    <figure class="fig">\n%s\n      <figcaption>%s</figcaption>\n    </figure>\n'
             % (svg, a.caption))

    if a.anchor:
        i = s.find(a.anchor, start, end)
        if i == -1:
            sys.exit("在題解 card 內找不到 anchor：%s" % a.anchor)
        j = s.rfind('<div class="step">', start, i)
        if j == -1:
            j = i
        s = s[:j] + block + "    " + s[j:]
    else:
        s = s[:start] + block + s[start:]

    open(a.page, "w", encoding="utf-8").write(s)
    print("已插入圖：", a.page)


if __name__ == "__main__":
    main()
