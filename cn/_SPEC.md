# 中文版練習頁：製作規格

## 你的產出
一個檔案：`cn/<slug>.body.html`。它是中文練習頁的 `<body>` 內容（不含 `<head>`、CSS、JS）。
建置腳本會自動加上 `<head>`、`assets/cn.css`、`assets/cn.js`，然後輸出成 `<slug>.html`。

## 檔案開頭必須有前置資料
```
<!--PAGE
{"title":"香港中學文憑試 數學（必修）· 百分數 — 7 種題型 50 題（附詳解）","desc":"100–160 字中文簡介，用於 meta description","file":"DSE_Percentages_50_Questions.html"}
PAGE-->
```
`title` 用於 `<title>`，`desc` 用於 meta description，`file` 是最終輸出檔名（由我指定，必須原樣照填）。

## 主體結構（必須完全一致）
```
<div class="typebar">
  <div class="typebar__inner"><a href="#t1" data-t="t1">類型 1 · 百分數增減</a>…（共 7 個，t1–t7）</div>
  <div class="progress"><div class="progress__fill" id="pfill"></div></div>
</div>

<div class="container">
  <header class="hero">
    <p class="hero__eyebrow">香港中學文憑試 數學（必修部分）· 百分數</p>
    <h1 class="hero__title">百分數 — 7 種題型，50 題練習</h1>
    <p class="hero__subtitle">…（一至兩句，說明題型來源與編排）</p>
    <div class="hero__stats">
      <span class="stat"><b>7</b> 種題型</span>
      <span class="stat"><b>50</b> 道題目</span>
      <span class="stat"><b>30</b> 道歷年試題來源</span>
      <span class="stat"><b>100%</b> 附詳解</span>
    </div>
    <p class="hero__back"><a href="DSE_Maths_By_Topic.html">← 按課題索引</a>　·　<a href="index.html">按年份索引</a></p>
  </header>

  <div class="note-card">
    <h2>如何使用這 50 題</h2>
    <ol><li><b>先做後看。</b>…</li>…（4 點）</ol>
    <p class="legend">難度：★ 熱身　★★ 鞏固　★★★ 考試程度　★★★★ 挑戰（DSE 4 分以上題型）</p>
  </div>

  <div class="card" style="padding:1.1rem 1.2rem;">
    <h2 class="card__title" style="margin-top:0;">七種題型</h2>
    <div class="toc-table-wrap">
    <table class="table toc-table">
      <thead><tr><th>類型</th><th>名稱</th><th>重點</th><th style="text-align:center">題數</th></tr></thead>
      <tbody>…7 行…</tbody>
    </table>
    </div>
  </div>

  <div class="toolbar">
    <button id="expandAll">全部展開</button>
    <button id="collapseAll">全部收起</button>
    <span class="spacer"></span>
    <span id="ptext">已展開 0 / 50 題</span>
  </div>

  <section class="type-section" id="t1">…</section>
  …t2–t7…

  <footer class="footer">
    <p>香港中學文憑試 數學（必修部分）· 百分數 — 7 種題型，50 題練習</p>
    <p><a href="DSE_Maths_By_Topic.html">按課題索引</a> · <a href="index.html">按年份索引</a> · 題目改編自 2012–2026 年 DSE；詳解供教學使用。</p>
  </footer>
</div>
```

## 每個 type-section
```
<section class="type-section" id="t1">
  <div class="type-head">
    <div class="type-head__no">類型 1</div>
    <h2>百分數增減 <span class="count">· 7 題</span></h2>
    <p>一句話說明這個題型考甚麼</p>
  </div>
  <div class="concept">
    <p><b>核心概念：</b>…（2–4 句）</p>
    <div class="formula"><span>\(…\)</span><span>\(…\)</span></div>
  </div>

  <article class="q" id="q1">
    <div class="q__head"><span class="q__no">Q1</span><span class="q__stars" title="難度 1/4"><span>★</span><span class="off">☆</span><span class="off">☆</span><span class="off">☆</span></span><span class="badge badge--mark">2 分</span></div>
    <div class="q__body"><p>題目文字…</p></div>
    <button class="q__toggle" aria-expanded="false" aria-controls="q1-sol" data-target="q1-sol">顯示答案及詳解</button>
    <div class="q__sol tex2jax_ignore" id="q1-sol" hidden>
      <div class="answer"><span class="answer__label">答案</span>(a) \(…\)　(b) \(…\)</div>
      <ol class="steps">
        <li>第一步…</li><li>第二步…</li>
      </ol>
      <div class="hint"><span class="hint__label">常犯錯誤</span><p>…</p></div>
    </div>
  </article>
  …q2–q7…
  <div class="type-foot"><a href="#top">↑ 返回目錄</a></div>
</section>
```

## 已完成範例
`DSE_Percentages_50_Questions.html`（同資料夾上一層）是已通過驗證的完成品，可開來對照版式與語氣；只參考，不要照抄內容。

## 硬性規則
1. **題號連續**：`id="q1"` … `id="q50"`，每個 `article` 的 `aria-controls` / `data-target` / `id` 三者要對應（`q7` → `q7-sol`）。
2. **每題必須有**：`q__stars`（難度星，與原文相同）、`badge badge--mark`（幾分）、`answer`、`<ol class="steps">`（≥2 步）、`hint`（原文有就保留，沒有可省）。
3. **數學式一律原樣照抄**：所有 `\(…\)`、`\[…\]` 內容不要翻譯、不要改寫、不要改數字；變數、運算符、單位（cm、m²、\$、%）保持原樣。只翻譯公式以外的中文字。
3b. **公式內的 `\text{…}`**：若是英文詞語，譯成中文（`\text{profit}` → `\text{盈利}`、`\text{old}` → `\text{原值}`）；單位（cm、kg、m²）及人名保留英文。
4. **圖形原樣照抄**：原文的 `<figure class="figure">…</figure>`（連 `<svg>`）整個複製到同一題的 `q__body` 內，只把 `<figcaption>` 譯成中文（例如「Q31 附圖」）。
5. **星級與分數不可改**：`★`／`☆` 結構、`title="難度 n/4"`、`2 分`／`4 分` 等與原文一致（marks 譯成「分」）。
6. **所有英文正文都要譯成繁體中文**（香港數學用語），包括題目、答案、步驟、提示、圖表說明、按鈕以外的一切。按鈕文字/工具列文字照上面範本。
7. **不要**加 `<head>`、`<style>`、`<script>`、`<link>`。
8. 保留段落中的 `<b>`、`<br>`、`&amp;` 等行內標記。
9. 繁體中文、香港用語；句末用「。」；數學式前後不要加多餘空格。

## 寫入方式（重要）
檔案較大（約 70–90 KB），**不要一次寫完**。用 `write` 寫第一批（前置資料＋typebar＋hero＋note＋toc＋toolbar＋t1），再用 `write append=true` 續寫 t2–t4、t5–t7、footer。每次 append 前先確認上一段已完整結束（`</section>`）。

## 完成前自檢
- [ ] 7 個 `type-section`（t1–t7）、50 個 `article`（q1–q50）
- [ ] 每個 `article` 有 answer / steps / 對應的 `-sol` id
- [ ] 全文再無英文句子（數學符號、單位、專有名詞縮寫如 DSE、S.A.S. 可保留）
- [ ] `<svg>` 數量與英文原文相同
- [ ] 檔案可由 `python3 build_cn.py <slug>` 通過驗證
