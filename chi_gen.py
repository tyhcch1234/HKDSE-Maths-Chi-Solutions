#!/usr/bin/env python3
"""Render Chinese solution pages from compact content dicts.

Usage: python3 chi_gen.py content_module.py
Each content module defines QUESTIONS = [ {...}, ... ] with keys:
  year, paper ('卷一'/'卷二'), num, h1, sub, q, opts, fig, steps, ans, practice
"""
import sys, os, importlib.util

HEAD = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DSE {year} {paper} 第{num}題 · {h1}</title>
<script>
  window.MathJax = {{ tex:{{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]'],['$$','$$']]}}, svg:{{fontCache:'global'}} }};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
<link rel="stylesheet" href="assets/core.css">
<link rel="stylesheet" href="assets/extra.css">
</head>
<body>
<div class="hero">
  <div class="wrap">
    <span class="tag">DSE {year} · {paper} · 第{num}題</span>
    <h1>{h1}</h1>
    <p class="sub">{sub}</p>
  </div>
</div>
<div class="wrap">
  <div class="card">
    <h2>題目</h2>
    <div class="question">
{q}
    </div>
{opts}{fig}  </div>

  <div class="card">
    <h2>題解</h2>
{steps}
    <div class="ans"><span class="lbl">答案</span>{ans}</div>
  </div>

{practice}
  <nav class="pager">{prev}<a href="index.html">目錄</a>{next}</nav>
</div>
<footer>香港中學文憑試 數學（必修部分）題解 · 中文版 · 題目取材自香港考試及評核局歷年試題</footer>
</body>
</html>
"""


def opts_html(options):
    if not options:
        return ''
    lis = ''.join('<li><span class="ol">%s</span>%s</li>' % (k, v)
                  for k, v in zip('ABCD', options))
    return '    <ol class="opts">%s</ol>\n' % lis


def fig_html(fig):
    if not fig:
        return ''
    return '    <figure class="fig">%s</figure>\n' % fig


def steps_html(steps):
    out = []
    for i, (title, rule, body) in enumerate(steps, 1):
        s = ['    <div class="step">',
             '      <span class="step-tag">第 %d 步</span>' % i,
             '      <div class="step-title">%s</div>' % title]
        if rule:
            s.append('      <div class="rule"><span class="rule-name">%s</span>%s</div>' % rule)
        if body:
            s.append(body)
        s.append('    </div>')
        out.append('\n'.join(s))
    return '\n\n'.join(out)


def practice_html(p):
    if not p:
        return ''
    body = ['  <div class="practice">',
            '    <div class="p-head">練習 <span class="p-badge">同類新題</span></div>',
            '    <div class="p-body">',
            '      <div class="p-q"><b>題目.</b> %s</div>' % p['q']]
    if p.get('opts'):
        lis = ''.join('<li><span class="ol">%s</span>%s</li>' % (k, v)
                      for k, v in zip('ABCD', p['opts']))
        body.append('      <ol class="opts p-opts">%s</ol>' % lis)
    body.append('      <details>')
    body.append('        <summary>顯示題解</summary>')
    body.append('        <div class="p-sol">')
    for i, st in enumerate(p['steps'], 1):
        body.append('          <div class="p-step"><b>第 %d 步.</b> %s</div>' % (i, st))
    body.append('          <div class="p-ans">答案：%s</div>' % p['ans'])
    body.append('        </div>')
    body.append('      </details>')
    body.append('    </div>')
    body.append('  </div>')
    return '\n'.join(body)


def pager(year, paper, num):
    code = 'P1' if paper == '卷一' else 'P2'
    prev = '<a href="%s_%s_Q%d.html">‹ 上一題</a>' % (year, code, num - 1) if num > 1 else '<span></span>'
    nxt = '<a href="%s_%s_Q%d.html">下一題 ›</a>' % (year, code, num + 1) if num < 60 else '<a href="index.html">下一題 ›</a>'
    return prev, nxt


def render(q):
    year, paper, num = q['year'], q['paper'], q['num']
    code = 'P1' if paper == '卷一' else 'P2'
    prev, nxt = pager(year, paper, num)
    html = HEAD.format(year=year, paper=paper, num=num, h1=q['h1'], sub=q['sub'],
                       q=q['q'].strip('\n'), opts=opts_html(q.get('opts')),
                       fig=fig_html(q.get('fig')),
                       steps=steps_html(q['steps']),
                       ans=q['ans'], practice=practice_html(q.get('practice')),
                       prev=prev, next=nxt)
    fn = '%s_%s_Q%d.html' % (year, code, num)
    with open(fn, 'w', encoding='utf8') as fh:
        fh.write(html)
    return fn


def main():
    mod_path = sys.argv[1]
    spec = importlib.util.spec_from_file_location('content', mod_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for q in mod.QUESTIONS:
        print('wrote', render(q))


if __name__ == '__main__':
    main()
