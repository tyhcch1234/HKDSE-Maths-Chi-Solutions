# -*- coding: utf-8 -*-
# 2018 卷一 Q6–Q10
QUESTIONS = [
{
 'year': '2018', 'paper': '卷一', 'num': 6,
 'h1': '兩條不等式同時成立：取交集',
 'sub': '不等式 · 複合不等式',
 'q': r'''<br>(a) 求滿足 $\dfrac{3-x}{2}>2x+7$ 及 $x+8\ge0$ 的 $x$ 的範圍。
<br>(b) 寫出同時滿足 (a) 中兩條不等式的最大整數。<span class="marks">[4 分]</span>''',
 'steps': [
   ('解第一條：兩邊乘 2', ('不等式性質', r'乘正數，不等號方向不變。'),
    r'''<p>$$\frac{3-x}{2}>2x+7\;\Longrightarrow\;3-x>4x+14$$</p>'''),
   ('移項後除以負數，符號反向', ('注意', r'兩邊除以 $-5$ 時，不等號要反轉。'),
    r'''<p>$$-5x>11\;\Longrightarrow\;x<-\frac{11}{5}=-2.2$$</p>'''),
   ('解第二條', None,
    r'''<p>$$x+8\ge0\;\Longrightarrow\;x\ge-8$$</p>'''),
   ('取交集', ('交集', r'兩條要<strong>同時</strong>成立，取重疊部分。'),
    r'''<p>$$-8\le x<-2.2$$</p>'''),
   ('(b) 找最大整數', None,
    r'''<p>在 $-8\le x<-2.2$ 之中，最大的整數是 $-3$。</p>'''),
 ],
 'ans': r'<b>(a) $-8\le x<-2.2$　(b) $-3$</b>',
 'practice': {
   'q': r'求滿足 $\dfrac{5-x}{3}<x+1$ 及 $x-2\le4$ 的 $x$ 的範圍，並寫出最大的整數 $x$。',
   'opts': [r'$0.5<x\le6$，最大整數 $6$', r'$x<6$，最大整數 $5$',
            r'$0.5<x<6$，最大整數 $5$', r'$x>-2$，最大整數 $6$'],
   'steps': [
     r'第一條乘 3：$5-x<3x+3$，即 $2<4x$，$x>0.5$。',
     r'第二條：$x\le6$。',
     r'交集為 $0.5<x\le6$，最大整數是 $6$。',
   ],
   'ans': r'<b>A</b>（$0.5<x\le6$，最大整數 $6$）',
 },
},
{
 'year': '2018', 'paper': '卷一', 'num': 7,
 'h1': '折扣與虧蝕：用成本連起兩個百分數',
 'sub': '百分數 · 折扣與盈利',
 'q': r'''某花瓶的標價比成本高 $30\%$。若以標價的六折（即 $40\%$ 折扣）售出，則虧蝕 $\$88$。求花瓶的標價。<span class="marks">[5 分]</span>''',
 'steps': [
   ('設標價為 $\$x$，反求成本', ('成本與標價', r'標價 $=$ 成本 $\times(1+30\%)$。'),
    r'''<p>$$\text{成本}=\frac{x}{1.3}=\frac{10x}{13}$$</p>'''),
   ('寫出售價', ('折扣', r'售價 $=(1-40\%)\times$ 標價 $=0.6x$。'),
    r'''<p>$$\text{售價}=0.6x=\frac{3x}{5}$$</p>'''),
   ('虧蝕＝成本 − 售價', None,
    r'''<p>$$\frac{10x}{13}-\frac{3x}{5}=88$$</p>'''),
   ('通分求解', None,
    r'''<p>$$\frac{50x-39x}{65}=88\;\Longrightarrow\;\frac{11x}{65}=88$$</p>
<p>$$x=\frac{88\times65}{11}=8\times65=520$$</p>'''),
   ('驗算', None,
    r'''<p>成本 $=\dfrac{10(520)}{13}=\$400$，售價 $=0.6(520)=\$312$，虧蝕 $=\$88$ ✓</p>'''),
 ],
 'ans': r'<b>標價為 $\$520$</b>',
 'practice': {
   'q': r'某外套的標價比成本高 $60\%$。若以標價的七折售出，則盈利 $\$36$。求成本。',
   'opts': [r'$\$300$', r'$\$360$', r'$\$420$', r'$\$480$'],
   'steps': [
     r'設成本 $\$c$，標價 $=1.6c$，售價 $=0.7\times1.6c=1.12c$。',
     r'盈利 $=1.12c-c=0.12c=36$。',
     r'$c=300$。',
   ],
   'ans': r'<b>A</b>（$\$300$）',
 },
},
{
 'year': '2018', 'paper': '卷一', 'num': 8,
 'h1': '圓中平行弦：內錯角、同弓形、三角形內角和',
 'sub': '平面幾何 · 圓與平行線',
 'q': r'''圖 1 中 $ABCDE$ 是一個圓。已知 $AB\parallel ED$，$AD$ 與 $BE$ 相交於 $F$。以 $\theta$ 表示 $x$ 及 $y$。<span class="marks">[5 分]</span>''',
 'fig': r'''<svg viewBox="0 0 300 300" width="300" height="300" role="img" aria-label="圓 ABCDE，AB 平行 ED">
 <g fill="none" stroke="currentColor" stroke-width="1.5">
  <circle cx="150" cy="130" r="92"/>
  <line x1="70" y1="85" x2="230" y2="85"/>
  <line x1="70" y1="175" x2="230" y2="175"/>
  <line x1="70" y1="85" x2="230" y2="175"/>
  <line x1="230" y1="85" x2="70" y2="175"/>
 </g>
 <g fill="currentColor" font-family="Georgia,serif" font-style="italic" font-size="14">
  <text x="60" y="79">A</text>
  <text x="238" y="79">B</text>
  <text x="250" y="134">C</text>
  <text x="238" y="192">D</text>
  <text x="60" y="192">E</text>
  <text x="156" y="126">F</text>
  <text x="86" y="104">x</text>
  <text x="160" y="146">y</text>
  <text x="232" y="152">θ</text>
 </g>
</svg><figcaption>圖：$AB\parallel ED$，$AD$ 與 $BE$ 交於 $F$；$x$ 在 $A$、$y$ 在 $F$、$\theta$ 在 $C$</figcaption>''',
 'steps': [
   ('用平行線的同旁內角', ('同旁內角', r'$AB\parallel ED$，截線 $AD$ 所成的同旁內角互補。'),
    r'''<p>$$x+\theta=180^{\circ}\;\Longrightarrow\;x=180^{\circ}-\theta$$</p>'''),
   ('內錯角給出 $\angle ADE$', ('內錯角', r'$AB\parallel ED$，截線 $AD$。'),
    r'''<p>$$\angle ADE=\angle DAB=x=180^{\circ}-\theta$$</p>'''),
   ('同弓形內的圓周角', ('同弓形', r'弦 $BD$ 所對的圓周角相等。'),
    r'''<p>$$\angle BED=\angle BAD=x=180^{\circ}-\theta$$</p>'''),
   ('在 $\triangle FED$ 用內角和', ('三角形內角和', r'三角之和 $=180^{\circ}$。'),
    r'''<p>$$y=180^{\circ}-(180^{\circ}-\theta)-(180^{\circ}-\theta)=2\theta-180^{\circ}$$</p>'''),
 ],
 'ans': r'<b>$x=180^{\circ}-\theta$，$y=2\theta-180^{\circ}$</b>',
 'practice': {
   'q': r'圖中 $PQRS$ 是一個圓，$PQ\parallel SR$，$PR$ 與 $QS$ 交於 $T$。若 $\angle PSR=105^{\circ}$，求 $\angle PTQ$。',
   'opts': [r'$30^{\circ}$', r'$45^{\circ}$', r'$60^{\circ}$', r'$75^{\circ}$'],
   'steps': [
     r'同旁內角：$\angle PQS+105^{\circ}=180^{\circ}$，故 $\angle PQS=75^{\circ}$。',
     r'同弓形：$\angle QPR=\angle QSR=75^{\circ}$。',
     r'$\triangle PQT$ 中 $\angle PTQ=180^{\circ}-75^{\circ}-75^{\circ}=30^{\circ}$。',
   ],
   'ans': r'<b>A</b>（$30^{\circ}$）',
 },
},
{
 'year': '2018', 'paper': '卷一', 'num': 9,
 'h1': '行程問題：時間單位要統一',
 'sub': '方程 · 速度、時間與距離',
 'q': r'''某汽車由城市 $P$ 以平均速度 $72\text{ km/h}$ 駛往城市 $Q$，再以平均速度 $90\text{ km/h}$ 由 $Q$ 駛往城市 $R$。已知全程 $210\text{ km}$，共用了 $161$ 分鐘。求由 $P$ 往 $Q$ 所需的時間。<span class="marks">[5 分]</span>''',
 'steps': [
   ('設未知數', None,
    r'''<p>設由 $P$ 往 $Q$ 需 $x$ 分鐘，則由 $Q$ 往 $R$ 需 $(161-x)$ 分鐘。</p>'''),
   ('把分鐘化為小時', ('單位', r'速度以 km/h 為單位，時間要用小時。'),
    r'''<p>$$\frac{x}{60}\ \text{h}\quad\text{及}\quad\frac{161-x}{60}\ \text{h}$$</p>'''),
   ('距離＝速度 × 時間', ('行程公式', r'$d=vt$。'),
    r'''<p>$$72\left(\frac{x}{60}\right)+90\left(\frac{161-x}{60}\right)=210$$</p>'''),
   ('解方程', None,
    r'''<p>全式乘 $60$：</p>
<p>$$72x+90(161-x)=12600$$</p>
<p>$$72x+14490-90x=12600$$</p>
<p>$$-18x=-1890\;\Rightarrow\;x=105$$</p>'''),
   ('驗算', None,
    r'''<p>$72\times\dfrac{105}{60}=126$ km，$90\times\dfrac{56}{60}=84$ km，合共 $210$ km ✓</p>'''),
 ],
 'ans': r'<b>$105$ 分鐘（即 1 小時 45 分）</b>',
 'practice': {
   'q': r'某人先以 $60\text{ km/h}$ 行駛 $t$ 分鐘，再以 $80\text{ km/h}$ 行駛 $45$ 分鐘，全程 $95\text{ km}$。求 $t$。',
   'opts': [r'$35$', r'$40$', r'$45$', r'$50$'],
   'steps': [
     r'$60\cdot\dfrac{t}{60}+80\cdot\dfrac{45}{60}=95$。',
     r'$t+60=95$。',
     r'$t=35$。',
   ],
   'ans': r'<b>A</b>（$35$）',
 },
},
{
 'year': '2018', 'paper': '卷一', 'num': 10,
 'h1': '箱形圖讀數＋合併後範圍的判斷',
 'sub': '統計學 · 箱形圖與範圍',
 'q': r'''以下的箱形圖顯示某公司 $X$ 組職員年齡的分佈。已知該分佈的範圍及四分位數間距分別為 $43$ 及 $21$。圖中下四分位數為 $27$、中位數為 $38$、上四分位數為 $a$、下極值為 $19$、上極值為 $b$（單位：歲）。
<br>(a) 求 $a$ 及 $b$。
<br>(b) 公司 $Y$ 組有 5 名職員，其中 3 人的年齡為 $38$。已知 $Y$ 組年齡的範圍為 $20$。現把 $X$ 組與 $Y$ 組合併成一部門。經理聲稱：該部門年齡的範圍必定與 $X$ 組的年齡範圍相同。你是否同意？試解釋。<span class="marks">[5 分]</span>''',
 'fig': r'''<svg viewBox="0 0 380 130" width="380" height="130" role="img" aria-label="箱形圖">
  <g stroke="currentColor" stroke-width="1.4" fill="none">
    <line x1="40" y1="90" x2="350" y2="90"/>
    <line x1="70" y1="55" x2="70" y2="70"/>
    <line x1="70" y1="70" x2="120" y2="70"/>
    <rect x="120" y="50" width="130" height="40"/>
    <line x1="185" y1="50" x2="185" y2="90"/>
    <line x1="250" y1="70" x2="300" y2="70"/>
    <line x1="300" y1="55" x2="300" y2="70"/>
  </g>
  <g fill="currentColor" font-family="Georgia,serif" font-size="12">
    <text x="66" y="106" text-anchor="middle">19</text>
    <text x="120" y="106" text-anchor="middle">27</text>
    <text x="185" y="106" text-anchor="middle">38</text>
    <text x="250" y="106" text-anchor="middle">a</text>
    <text x="300" y="106" text-anchor="middle">b</text>
    <text x="330" y="106">年齡</text>
  </g>
</svg><figcaption>圖：$X$ 組年齡的箱形圖</figcaption>''',
 'steps': [
   ('(a) 用四分位數間距求 $a$', ('四分位數間距', r'$\text{IQR}=Q_{3}-Q_{1}$。'),
    r'''<p>$$a-27=21\;\Rightarrow\;a=48$$</p>'''),
   ('(a) 用範圍求 $b$', ('範圍', r'範圍 $=$ 最大值 $-$ 最小值。'),
    r'''<p>$$b-19=43\;\Rightarrow\;b=62$$</p>'''),
   ('(b) $Y$ 組年齡的極端值', None,
    r'''<p>$Y$ 組有三人同為 $38$ 歲，範圍為 $20$。若 $38$ 是最大值，則最小值可低至 $38-20=18$。</p>'''),
   ('合併後範圍最大可以是 $44$', None,
    r'''<p>合併後最小值可為 $\min(19,18)=18$，最大值為 $\max(62,38)=62$，故範圍最大可達</p>
<p>$$62-18=44\neq43$$</p>'''),
   ('結論', None,
    r'''<p>既然可出現 $44$，經理的說法不成立，故<strong>不同意</strong>。</p>'''),
 ],
 'ans': r'<b>(a) $a=48$，$b=62$　(b) 不同意（合併後範圍可為 $62-18=44$）</b>',
 'practice': {
   'q': r'某組數據的箱形圖顯示：最小值 $12$、下四分位數 $18$、中位數 $25$、上四分位數 $32$、最大值 $45$。求該分佈的四分位數間距及範圍。',
   'opts': [r'IQR $=14$，範圍 $=33$', r'IQR $=14$，範圍 $=27$',
            r'IQR $=21$，範圍 $=33$', r'IQR $=7$，範圍 $=20$'],
   'steps': [
     r'IQR $=Q_{3}-Q_{1}=32-18=14$。',
     r'範圍 $=45-12=33$。',
     r'故 IQR $=14$、範圍 $=33$。',
   ],
   'ans': r'<b>A</b>（IQR $=14$，範圍 $=33$）',
 },
},
]
