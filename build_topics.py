#!/usr/bin/env python3
"""按課題索引（DSE_Maths_By_Topic.html）增量建置工具。

用法：
  python3 build_topics.py            # 加入下方 MAP 指定的題目並重排
  python3 build_topics.py --report   # 只列出未被收錄的頁面，不改檔
"""
import re
import sys
import glob

PATH = "DSE_Maths_By_Topic.html"

TOPICS = [
    "百分數",
    "率、比及變分",
    "估算、近似與誤差",
    "多項式",
    "公式與數列",
    "方程",
    "函數及其圖像",
    "指數定律、指數函數與對數函數",
    "不等式與線性規劃",
    "求積法",
    "幾何",
    "解析幾何",
    "三角學",
    "概率",
    "統計學",
]

# 2026 全年（卷一 19 題 + 卷二 45 題）
MAP = {}
for q, t in {
    1: "方程", 2: "指數定律、指數函數與對數函數", 3: "解析幾何", 4: "多項式",
    5: "百分數", 6: "不等式與線性規劃", 7: "百分數", 8: "幾何",
    9: "統計學", 10: "統計學", 11: "率、比及變分", 12: "解析幾何",
    13: "求積法", 14: "多項式", 15: "概率", 16: "解析幾何",
    17: "三角學", 18: "公式與數列", 19: "函數及其圖像",
}.items():
    MAP[f"2026_P1_Q{q}.html"] = t

for q, t in {
    1: "多項式", 2: "指數定律、指數函數與對數函數", 3: "多項式", 4: "估算、近似與誤差",
    5: "多項式", 6: "方程", 7: "函數及其圖像", 8: "多項式", 9: "不等式與線性規劃",
    10: "率、比及變分", 11: "百分數", 12: "率、比及變分", 13: "公式與數列",
    14: "解析幾何", 15: "函數及其圖像", 16: "求積法", 17: "求積法", 18: "幾何",
    19: "三角學", 20: "幾何", 21: "幾何", 22: "幾何", 23: "幾何", 24: "幾何",
    25: "幾何", 26: "解析幾何", 27: "解析幾何", 28: "概率", 29: "統計學",
    30: "統計學", 31: "指數定律、指數函數與對數函數", 32: "多項式", 33: "公式與數列",
    34: "方程", 35: "指數定律、指數函數與對數函數", 36: "指數定律、指數函數與對數函數",
    37: "不等式與線性規劃", 38: "幾何", 39: "三角學", 40: "三角學", 41: "三角學",
    42: "概率", 43: "概率", 44: "統計學", 45: "統計學",
}.items():
    MAP[f"2026_P2_Q{q}.html"] = t


# 舊頁面 .sub 課題名稱的統一對照（只用於補漏，不改動既有分類）
NORM = {
    "百分數": "百分數", "百分法": "百分數", "百分數與應用題": "百分數",
    "率、比及變分": "率、比及變分", "率、比與變分": "率、比及變分",
    "變分": "率、比及變分", "比率": "率、比及變分", "比與比例": "率、比及變分",
    "比例尺": "率、比及變分",
    "估算、近似與誤差": "估算、近似與誤差", "估算與誤差": "估算、近似與誤差",
    "近似與誤差": "估算、近似與誤差", "數值與誤差": "估算、近似與誤差",
    "多項式": "多項式", "代數": "多項式", "代數分式": "多項式", "因式分解": "多項式",
    "公式與數列": "公式與數列", "數列": "公式與數列", "等比數列": "公式與數列",
    "數列與對數": "公式與數列", "公式": "方程",
    "方程": "方程", "二次方程": "方程", "複數": "方程", "$i$ 的冪": "方程",
    "代數變換": "方程",
    "函數及其圖像": "函數及其圖像", "函數與圖象": "函數及其圖像",
    "函數": "函數及其圖像", "二次函數": "函數及其圖像",
    "指數定律、指數函數與對數函數": "指數定律、指數函數與對數函數",
    "指數與對數": "指數定律、指數函數與對數函數", "指數定律": "指數定律、指數函數與對數函數",
    "指數律": "指數定律、指數函數與對數函數", "對數": "指數定律、指數函數與對數函數",
    "對數律": "指數定律、指數函數與對數函數", "數制": "指數定律、指數函數與對數函數",
    "不等式與線性規劃": "不等式與線性規劃", "不等式": "不等式與線性規劃",
    "線性規劃": "不等式與線性規劃",
    "求積法": "求積法", "扇形": "求積法", "度量": "求積法", "面積與體積": "求積法",
    "幾何": "幾何", "平面幾何": "幾何", "圓的性質": "幾何", "圓形性質": "幾何",
    "圓的基本性質": "幾何", "圓形幾何": "幾何", "切線性質": "幾何",
    "相似三角形": "幾何", "全等與相似": "幾何", "三角形": "幾何", "四邊形": "幾何",
    "解析幾何": "解析幾何", "坐標幾何": "解析幾何", "坐標與幾何": "解析幾何",
    "直線": "解析幾何", "直線方程": "解析幾何", "圓方程": "解析幾何",
    "圓的方程": "解析幾何", "軌跡": "解析幾何", "圓與直線": "解析幾何",
    "極坐標": "解析幾何",
    "三角學": "三角學", "三角比": "三角學", "三角方程": "三角學",
    "三角函數圖像": "三角學", "平方關係": "三角學", "三角比與相似三角形": "三角學",
    "立體圖形": "三角學",
    "概率": "概率", "排列": "概率", "組合與概率": "概率", "概率與統計": "概率",
    "統計": "統計學", "統計學": "統計學", "平均數": "統計學",
}


# 2021 重複收錄的 12 題：只保留單一課題
MAP.update({
    "2021_P1_Q18.html": "三角學",
    "2021_P1_Q19.html": "函數及其圖像",
    "2021_P1_Q5.html": "率、比及變分",
    "2021_P1_Q7.html": "解析幾何",
    "2021_P1_Q8.html": "幾何",
    "2021_P2_Q2.html": "方程",
    "2021_P2_Q24.html": "三角學",
    "2021_P2_Q28.html": "概率",
    "2021_P2_Q33.html": "指數定律、指數函數與對數函數",
    "2021_P2_Q34.html": "指數定律、指數函數與對數函數",
    "2021_P2_Q39.html": "幾何",
    "2021_P2_Q45.html": "統計學",
})


def parse(html):
    """回傳 {topic: [filenames...]}，保持原檔次序。"""
    out = {}
    for m in re.finditer(r'<h2 class="topic-head">(.*?)</h2>\s*<div class="group">(.*?)</div>', html, re.S):
        name = re.sub(r'<[^>]+>', '', m.group(1))
        name = re.sub(r'\s*\(\d+\)\s*$', '', name).strip()
        chips = re.findall(r'href="([^"]+\.html)"', m.group(2))
        out[name] = chips
    return out


def key(f):
    """排序：年份 → 卷 → 題號（皆由小至大）。"""
    m = re.match(r'(\d{4})_P(\d)_Q(\d+)\.html', f)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else (9999, 9, 999)


def main():
    html = open(PATH, encoding="utf8").read()
    groups = parse(html)

    if "--report" in sys.argv:
        have = {f for v in groups.values() for f in v}
        missing = sorted(set(glob.glob("20*_P*_Q*.html")) - have, key=key)
        print(f"total pages={len(glob.glob('20*_P*_Q*.html'))} indexed={len(have)} missing={len(missing)}")
        for f in missing[:400]:
            print(f)
        return

    indexed = {f for v in groups.values() for f in v}
    auto = 0
    for f in sorted(glob.glob("20*_P*_Q*.html")):
        if f in indexed:
            continue
        t = open(f, encoding="utf8").read()
        m = re.search(r'<p class="sub">(.*?)</p>', t, re.S)
        if not m:
            continue
        name = re.sub(r'<[^>]+>', '', m.group(1)).split("·")[0].strip()
        topic = NORM.get(name)
        if topic:
            MAP.setdefault(f, topic)
            auto += 1
    print(f"auto-classified {auto} pages from .sub")

    for topic in TOPICS:
        groups.setdefault(topic, [])
    for f, t in MAP.items():
        assert t in TOPICS, t
        for topic, items in groups.items():
            if f in items and topic != t:
                items.remove(f)
        if f not in groups[t]:
            groups[t].append(f)

    blocks = []
    for topic in TOPICS:
        items = sorted(set(groups.get(topic, [])), key=key)
        chips = "".join(
            f'<a class="chip" href="{f}">{f[:4]} P{f[6]} Q{int(re.search(r"Q(\d+)", f).group(1))}</a>'
            for f in items
        )
        blocks.append(
            f'<h2 class="topic-head">{topic} '
            f'<span style="font-weight:500;font-size:.9rem;color:#94a3b8">({len(items)})</span></h2>'
            f'<div class="group">{chips}</div>'
        )

    total_pages = len(glob.glob("20*_P*_Q*.html"))
    html = re.sub(r'共 \d+ 題', f'共 {total_pages} 題', html, count=1)
    html = re.sub(r'(<p class="sub">[^<]*?)</p>',
                  r'\1 · 排序：年份 → 卷 → 題號</p>', html, count=1)

    start = html.index('<h2 class="topic-head">')
    end = html.rindex('</div>') + len('</div>')
    new = html[:start] + "\n".join(blocks) + html[end:]
    open(PATH, "w", encoding="utf8").write(new)
    total = sum(len(v) for v in groups.values())
    print(f"updated: {total} chips across {len(TOPICS)} topics")


if __name__ == "__main__":
    main()
