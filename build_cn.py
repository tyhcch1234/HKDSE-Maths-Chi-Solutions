#!/usr/bin/env python3
"""組裝中文練習頁：cn/<slug>.body.html (含 <!--PAGE ... PAGE--> 前置資料) -> <slug>.html

用法：python3 build_cn.py            # 組裝全部
      python3 build_cn.py percentages  # 只組裝一套
"""
import json, os, re, sys, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
CN = os.path.join(ROOT, "cn")

HEAD = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<script>
window.MathJax = {{
  tex: {{ inlineMath: [['\\\\(','\\\\)']], displayMath: [['\\\\[','\\\\]']] }},
  svg: {{ fontCache: 'global' }},
  options: {{ ignoreHtmlClass: 'tex2jax_ignore' }}
}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js" async></script>
<link rel="stylesheet" href="assets/cn.css">
</head>
<body id="top">
"""

TAIL = """<script src="assets/cn.js"></script>
</body>
</html>
"""


def load_body(path):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"\s*<!--PAGE\s*(\{.*?\})\s*PAGE-->", raw, re.S)
    if not m:
        raise SystemExit(f"{path}: 缺少 <!--PAGE {{...}} PAGE--> 前置資料")
    meta = json.loads(m.group(1))
    body = raw[m.end():]
    return meta, body


def validate(slug, body, meta):
    errs = []
    for k in ("title", "desc"):
        if not meta.get(k):
            errs.append(f"缺少 {k}")
    secs = re.findall(r'<section class="type-section" id="(t\d+)">', body)
    if secs != [f"t{i}" for i in range(1, 8)]:
        errs.append(f"section 應為 t1..t7，實得 {secs}")
    qids = re.findall(r'<article class="q" id="(q\d+)">', body)
    if qids != [f"q{i}" for i in range(1, 51)]:
        errs.append(f"article 應為 q1..q50（共 {len(qids)} 個）")
    arts = re.findall(r'<article class="q" id="q\d+">(.*?)</article>', body, re.S)
    for i, a in enumerate(arts, 1):
        if 'class="answer"' not in a:
            errs.append(f"q{i} 缺 answer")
        if '<ol class="steps">' not in a:
            errs.append(f"q{i} 缺 steps")
        n_li = len(re.findall(r"<li>", a))
        if n_li < 2:
            errs.append(f"q{i} 步驟只得 {n_li} 條")
        m = re.search(r'data-target="(q\d+-sol)"', a)
        if not m or f'id="{m.group(1)}"' not in a:
            errs.append(f"q{i} 的 toggle 與詳解 id 對不上")
    tabs = re.findall(r'<a href="#(t\d+)" data-t="t\d+">', body)
    if tabs != [f"t{i}" for i in range(1, 8)]:
        errs.append(f"typebar 應有 7 個連結，實得 {tabs}")
    # 英文字眼殘留
    leftovers = []
    for w in ("Show answer", "Hide solution", "Common mistake", "Back to contents",
              "question types", "Expand all", "Collapse all", "Answer</span>",
              "Opened ", "Index by topic", "How to use these"):
        if w in body:
            leftovers.append(w)
    if leftovers:
        errs.append("仍有英文：" + ", ".join(leftovers))
    # 中文字比例
    text = re.sub(r"<svg.*?</svg>", " ", body, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\\\(.*?\\\)", " ", text, flags=re.S)
    han = len(re.findall(r"[\u4e00-\u9fff]", text))
    latin_words = len(re.findall(r"[A-Za-z]{3,}", text))
    if han < 1200:
        errs.append(f"中文字數偏少（{han}）")
    if latin_words > han / 8:
        errs.append(f"英文殘留偏多（英文詞 {latin_words} vs 中文字 {han}）")
    texts = [t for t in re.findall(r"\\text\{([^}]*)\}", body) if re.fullmatch(r"[A-Za-z ]{3,}", t or "")]
    return errs, {"han": han, "latin": latin_words, "figs": body.count("<svg"), "text_en": texts}


def main(only=None):
    files = sorted(glob.glob(os.path.join(CN, "*.body.html")))
    if only:
        files = [f for f in files if os.path.basename(f).startswith(only)]
    report = []
    for f in files:
        slug = os.path.basename(f).replace(".body.html", "")
        meta, body = load_body(f)
        errs, stats = validate(slug, body, meta)
        out = os.path.join(ROOT, meta.get("file", slug + ".html"))
        if errs:
            report.append((slug, "FAIL", errs, stats))
            continue
        html = HEAD.format(title=meta["title"], desc=meta["desc"]) + body.strip() + "\n" + TAIL
        open(out, "w", encoding="utf-8").write(html)
        report.append((slug, "OK", [], stats))
    for slug, status, errs, stats in report:
        warn = ("  提醒: \\text 仍為英文 " + ",".join(stats.get("text_en", [])[:6])) if stats.get("text_en") else ""
        print(f"{status:4s} {slug:28s} 中文字={stats['han']:5d} 英文詞={stats['latin']:4d} 圖={stats['figs']:2d}"
              + ("" if not errs else "  " + "; ".join(errs)) + warn)
    return all(r[1] == "OK" for r in report) and bool(report)


if __name__ == "__main__":
    ok = main(sys.argv[1] if len(sys.argv) > 1 else None)
    sys.exit(0 if ok else 1)
