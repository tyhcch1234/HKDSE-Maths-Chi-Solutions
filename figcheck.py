#!/usr/bin/env python3
"""檢查四大課題（幾何、解析幾何、三角學、求積法）每頁題解是否已有 AI 繪圖（inline SVG）。

用法：
  python3 figcheck.py            # 全部四課題，列出未達標頁面
  python3 figcheck.py 幾何        # 只查某課題
  python3 figcheck.py --pages a.html b.html   # 只查指定頁
"""
import re
import sys

TOPICS = ["求積法", "幾何", "解析幾何", "三角學"]


def topic_pages():
    s = open("DSE_Maths_By_Topic.html", encoding="utf-8").read()
    heads = [(m.group(1).split("<span")[0].strip(), m.start())
             for m in re.finditer(r'<h2 class="topic-head">(.*?)</h2>', s)]
    out = {}
    for i, (name, pos) in enumerate(heads):
        end = heads[i + 1][1] if i + 1 < len(heads) else len(s)
        out[name] = re.findall(r'class="chip" href="([^"]+)"', s[pos:end])
    return out


def has_fig(page):
    s = open(page, encoding="utf-8").read()
    m = re.search(r"<h2>\s*題解\s*</h2>", s)
    if not m:
        return False
    start = m.end()
    nxt = [s.find(x, start) for x in ('<div class="practice"', '<div class="card"', "<footer")]
    nxt = [x for x in nxt if x != -1]
    end = min(nxt) if nxt else len(s)
    return "<svg" in s[start:end]


def main():
    args = sys.argv[1:]
    if args and args[0] == "--pages":
        pages = args[1:]
        miss = [p for p in pages if not has_fig(p)]
        print("指定頁 %d，缺圖 %d" % (len(pages), len(miss)))
        for p in miss:
            print("  MISS", p)
        return
    tp = topic_pages()
    want = args[0] if args else None
    total = allmiss = 0
    for t in TOPICS:
        if want and t != want:
            continue
        pages = tp.get(t, [])
        miss = [p for p in pages if not has_fig(p)]
        total += len(pages)
        allmiss += len(miss)
        print("%s：%d 頁，缺圖 %d（達標 %d）" % (t, len(pages), len(miss), len(pages) - len(miss)))
        for p in miss:
            print("   ", p)
    print("合計 %d 頁，缺圖 %d 頁" % (total, allmiss))


if __name__ == "__main__":
    main()
