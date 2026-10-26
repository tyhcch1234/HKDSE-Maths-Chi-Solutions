#!/usr/bin/env python3
"""2024 卷一 中文題解頁面生成器（沿用 chi-site 既有版式）"""
import os

HEAD = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<script>
  window.MathJax = {{ tex:{{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]'],['$$','$$']]}}, svg:{{fontCache:'global'}} }};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
<link rel="stylesheet" href="assets/core.css">
<link rel="stylesheet" href="assets/extra.css">
</head>
<body>
<div class="hero"><div class="wrap">
  <span class="tag">{tag}</span>
  <h1>{h1}</h1>
  <p class="sub">{sub}</p>
</div></div>
<div class="wrap">
  <div class="card">
    <h2>題目</h2>
    <div class="question">
      {q}<span class="marks">[{marks}]</span>
    </div>
{fig}  </div>

  <div class="card">
    <h2>題解</h2>
"""

STEP = """    <div class="step">
      <span class="step-tag">{tag}</span>
      <div class="step-title">{title}</div>
{rule}{body}
    </div>
"""

RULE = """      <div class="rule">
        <span class="rule-name">{name}</span>
        <span class="rule-math">{math}</span>
        <span class="rule-why">{why}</span>
      </div>
"""

PRACTICE = """  <div class="practice">
    <div class="p-head">練習 <span class="p-badge">同類新題</span></div>
    <div class="p-body">
      <div class="p-q"><b>題目.</b> {q}</div>
      <details>
        <summary>顯示題解</summary>
        <div class="p-sol">
{steps}
          <div class="p-ans">答案：{ans}</div>
        </div>
      </details>
    </div>
  </div>

"""

PAGER = """  <nav class="pager">{prev}<a href="index.html">目錄</a>{next}</nav>
</div>
</body>
</html>
"""


def pager(n, year=2024, paper='P1'):
    prev_link = '<a href="%d_%s_Q%d.html">‹ 上一題</a>' % (year, paper, n - 1) \
        if os.path.exists('%d_%s_Q%d.html' % (year, paper, n - 1)) else '<span></span>'
    nxt = '%d_%s_Q%d.html' % (year, paper, n + 1)
    next_link = '<a href="%s">下一題 ›</a>' % nxt if os.path.exists(nxt) else '<span></span>'
    return prev_link, next_link


def render(item, paper='P1', year=2024):
    fig = ''
    if item.get('fig'):
        fig = ('    <figure class="fig">\n      %s\n      <figcaption>%s</figcaption>\n    </figure>\n'
               % (item['fig'], item.get('cap', '')))
    out = HEAD.format(title=item['title'], tag=item['tag'], h1=item['h1'],
                      sub=item['sub'], q=item['q'], marks=item['marks'], fig=fig)
    for s in item['steps']:
        rule = ''
        if s.get('rule'):
            r = s['rule']
            rule = RULE.format(name=r[0], math=r[1], why=r[2])
        out += STEP.format(tag=s['tag'], title=s['title'], rule=rule, body=s['body'])
    out += '    <div class="ans"><span class="lbl">答案</span>%s</div>\n  </div>\n\n' % item['ans']
    if item.get('practice'):
        p = item['practice']
        steps = ''
        for i, (t, b) in enumerate(p['steps'], 1):
            steps += '          <div class="p-step"><b>第 %d 步.</b> %s</div>\n' % (i, b)
        out += PRACTICE.format(q=p['q'], steps=steps, ans=p['ans'])
    prev_link, next_link = pager(item['n'], year, paper)
    out += PAGER.format(prev=prev_link, next=next_link)
    return out


def write_all(items, paper='P1', year=2024):
    for item in items:
        fn = '%d_%s_Q%d.html' % (year, paper, item['n'])
        with open(fn, 'w', encoding='utf8') as f:
            f.write(render(item, paper, year))
        print('wrote', fn)
