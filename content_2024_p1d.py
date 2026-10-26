#!/usr/bin/env python3
# 2024 卷一 Q16–Q19 內容
SVG_Q17 = """<svg viewBox="0 0 380 370" width="350" role="img" aria-label="圓 C 與由 U 引出的兩條切線">
  <circle cx="196" cy="196" r="129" fill="currentColor" fill-opacity="0.05"
          stroke="currentColor" stroke-width="1.5"/>
  <g fill="none" stroke="currentColor" stroke-width="1.2">
    <line x1="84" y1="260" x2="308" y2="132"/>
    <line x1="308" y1="52" x2="324" y2="180"/>
    <line x1="308" y1="52" x2="180" y2="68"/>
    <line x1="324" y1="180" x2="180" y2="68" stroke-dasharray="5 4" stroke-opacity=".7"/>
    <line x1="196" y1="196" x2="308" y2="52" stroke-dasharray="4 3" stroke-opacity=".55"/>
  </g>
  <g fill="currentColor">
    <circle cx="196" cy="196" r="3"/><circle cx="308" cy="132" r="3.2"/>
    <circle cx="84" cy="260" r="3.2"/><circle cx="308" cy="52" r="3.2"/>
    <circle cx="324" cy="180" r="3.2"/><circle cx="180" cy="68" r="3.2"/>
  </g>
  <g fill="currentColor" font-family="Georgia,serif" font-style="italic" font-size="14">
    <text x="188" y="214" text-anchor="end">G</text>
    <text x="316" y="130">Q</text>
    <text x="76" y="272">R</text>
    <text x="316" y="46">U</text>
    <text x="336" y="184">V</text>
    <text x="168" y="64">W</text>
  </g>
  <g fill="currentColor" font-size="11" font-family="system-ui,sans-serif">
    <text x="196" y="352" text-anchor="middle">QR 為直徑，圓心 G(3, −5)，半徑 √65</text>
  </g>
</svg>"""

P1_D = [
{
 'n': 16,
 'title': 'DSE 2024 卷一 Q16 · 組合與概率',
 'tag': 'DSE 2024 · 卷一 · Q16',
 'h1': '同時抽出 → 用組合，不用排列',
 'sub': '概率 · 組合 · 4 分題',
 'marks': '4 分',
 'q': '袋中有 $16$ 隻紅色杯及 $4$ 隻白色杯。若從袋中同時隨機抽出 $5$ 隻杯，求<br>'
       '(a) 剛好抽出 $1$ 隻白色杯的概率；<br>(b) 最多抽出 $3$ 隻紅色杯的概率。',
 'steps': [
  {'tag': '第 1 步', 'title': '建立計數模型',
   'rule': ('樣本空間', '$C_5^{20}$', '「同時抽出」表示不計次序，用組合數。'),
   'body': '    <p>杯的總數 $=16+4=20$，抽出 $5$ 隻的方法數為</p>\n'
           '    <p>$$C_5^{20}=15504$$</p>'},
  {'tag': '第 2 步', 'title': '(a) 剛好 1 白：1 白 + 4 紅',
   'rule': ('乘法原理', '$C_1^{4}\\times C_4^{16}$', '白色與紅色的選法互相獨立，相乘即可。'),
   'body': '    <p>$$C_1^{4}\\times C_4^{16}=4\\times1820=7280$$</p>\n'
           '    <p>$$P=\\frac{7280}{15504}=\\frac{455}{969}$$</p>'},
  {'tag': '第 3 步', 'title': '(b) 用「餘事件」最快',
   'rule': ('餘概率', '$P(\\text{最多 3 紅})=1-P(4\\text{ 或 }5\\text{ 紅})$', '「最多 3 紅」的反面只有「4 紅」與「5 紅」兩種情況。'),
   'body': '    <p>$$P(5\\text{ 紅})=\\frac{C_5^{16}}{15504}=\\frac{4368}{15504},\\qquad '
           'P(4\\text{ 紅})=\\frac{C_4^{16}C_1^{4}}{15504}=\\frac{7280}{15504}$$</p>'},
  {'tag': '第 4 步', 'title': '(b) 計算答案',
   'body': '    <p>$$P=1-\\frac{4368+7280}{15504}=\\frac{3856}{15504}=\\frac{241}{969}$$</p>\n'
           '    <p>亦可直接數：$C_2^{4}C_3^{16}+C_3^{4}C_2^{16}+C_4^{4}C_1^{16}=3360+480+16=3856$ ✓</p>'}],
 'ans': '(a) $\\dfrac{455}{969}$　(b) $\\dfrac{241}{969}$',
 'practice': {
  'q': '袋中有 $5$ 隻紅球及 $3$ 隻藍球，同時抽出 $4$ 隻。求 (a) 剛好 $2$ 隻藍球的概率；(b) 至少 $1$ 隻藍球的概率。',
  'steps': [('總方法數：', '$C_4^{8}=70$。'),
            ('(a) 2 藍 2 紅：', '$C_2^{3}C_2^{5}=3\\times10=30$，$P=\\dfrac{30}{70}=\\dfrac37$。'),
            ('(b) 餘事件「全紅」：', '$C_4^{5}=5$，$P=1-\\dfrac{5}{70}=\\dfrac{13}{14}$。')],
  'ans': '(a) $\\dfrac37$　(b) $\\dfrac{13}{14}$'}
},
{
 'n': 17,
 'title': 'DSE 2024 卷一 Q17 · 軌跡、圓與切線',
 'tag': 'DSE 2024 · 卷一 · Q17',
 'h1': '垂直平分線，再證四點共圓',
 'sub': '坐標幾何 · 圓方程 · 切線 · 8 分題',
 'marks': '8 分',
 'q': '點 $Q$、$R$ 的坐標分別為 $(10,-1)$ 及 $(-4,-9)$。<br>'
       '(a) 設 $P$ 為直角坐標平面上滿足 $PQ=PR$ 的動點，其軌跡記為 $\\Gamma$。'
       '(i) 描述 $\\Gamma$ 與 $QR$ 的幾何關係；(ii) 求 $\\Gamma$ 的方程。<br>'
       '(b) 設 $C$ 為通過 $Q$、$R$ 及點 $(4,3)$ 的圓。'
       '(i) 求 $C$ 的方程；(ii) 點 $U$ 的坐標為 $(10,4)$，已知 $U$ 在 $C$ 之外。$UV$、$UW$ 分別是 $C$ 於 $V$、$W$ 的切線。$\\triangle UVW$ 的外接圓面積是否大於 $100$？試解釋。',
 'fig': SVG_Q17,
 'cap': '$UV$、$UW$ 為切線，$\\angle UVG=\\angle UWG=90^{\\circ}$',
 'steps': [
  {'tag': '第 1 步', 'title': '(a)(i) 到兩點等距的軌跡',
   'rule': ('軌跡', '$PQ=PR$ 的軌跡是 $QR$ 的垂直平分線', '垂直平分線上的點到 $Q$、$R$ 等距，反之亦然。'),
   'body': '    <p>$\\Gamma$ 是線段 $QR$ 的垂直平分線（一條直線，垂直於 $QR$ 並通過其中點）。</p>'},
  {'tag': '第 2 步', 'title': '(a)(ii) 用距離平方列方程',
   'rule': ('距離公式', '$(x-10)^{2}+(y+1)^{2}=(x+4)^{2}+(y+9)^{2}$', '兩邊都是 $P$ 到定點距離的平方。'),
   'body': '    <p>展開並化簡：</p>\n'
           '    <p>$$x^{2}-20x+100+y^{2}+2y+1=x^{2}+8x+16+y^{2}+18y+81$$</p>\n'
           '    <p>$$-28x-16y+4=0 \\quad\\Longrightarrow\\quad 7x+4y-1=0$$</p>\n'
           '    <p>驗算中點 $(3,-5)$：$21-20-1=0$ ✓</p>'},
  {'tag': '第 3 步', 'title': '(b)(i) 設圓方程並代入三點',
   'rule': ('圓的一般式', '$x^{2}+y^{2}+Dx+Ey+F=0$', '三個點給出三個方程，可解 $D$、$E$、$F$。'),
   'body': '    <p>代入 $Q(10,-1)$：$101+10D-E+F=0$ ⋯ (1)</p>\n'
           '    <p>代入 $R(-4,-9)$：$97-4D-9E+F=0$ ⋯ (2)</p>\n'
           '    <p>代入 $(4,3)$：$25+4D+3E+F=0$ ⋯ (3)</p>\n'
           '    <p>(1) − (2)：$7D+4E=-2$；(1) − (3)：$3D-2E=-38$。解得</p>\n'
           '    <p>$$D=-6,\\quad E=10,\\quad F=-31$$</p>\n'
           '    <p>$$C:\\;x^{2}+y^{2}-6x+10y-31=0$$</p>'},
  {'tag': '第 4 步', 'title': '(b)(i) 讀出圓心與半徑',
   'rule': ('配方法', '$(x-3)^{2}+(y+5)^{2}=65$', '圓心 $(3,-5)$、半徑 $\\sqrt{65}$。'),
   'body': '    <p>圓心 $G=(3,-5)$，半徑 $r=\\sqrt{9+25+31}=\\sqrt{65}$。</p>\n'
           '    <p>留意 $G$ 正是 $QR$ 的中點，所以 $QR$ 是圓 $C$ 的直徑。</p>'},
  {'tag': '第 5 步', 'title': '(b)(ii) 找出 $U$、$V$、$G$、$W$ 的共圓關係',
   'rule': ('半圓上的圓周角', '$UV\\perp VG$，$UW\\perp WG$', '切線垂直於過切點的半徑，因此 $\\angle UVG=\\angle UWG=90^{\\circ}$。'),
   'body': '    <p>$V$ 與 $W$ 都在以 $UG$ 為直徑的圓上（同側看 $UG$ 成直角）。所以 $\\triangle UVW$ 的外接圓就是以 $UG$ 為直徑的圓。</p>'},
  {'tag': '第 6 步', 'title': '(b)(ii) 計算面積並比較',
   'body': '    <p>$$UG=\\sqrt{(10-3)^{2}+(4+5)^{2}}=\\sqrt{49+81}=\\sqrt{130}$$</p>\n'
           '    <p>$$\\text{外接圓面積}=\\pi\\left(\\frac{\\sqrt{130}}{2}\\right)^{2}=\\frac{130}{4}\\pi=32.5\\pi\\approx102.1$$</p>\n'
           '    <p>$102.1>100$，故聲稱正確。</p>'}],
 'ans': '(a)(i) $QR$ 的垂直平分線　(ii) $7x+4y-1=0$　(b)(i) $x^{2}+y^{2}-6x+10y-31=0$　(ii) 是，面積 $=32.5\\pi\\approx102>100$',
 'practice': {
  'q': '點 $A(2,7)$、$B(8,-1)$。求 $AB$ 的垂直平分線方程，並求該直線與 $x$ 軸的交點。',
  'steps': [('中點：', '$(5,3)$；$AB$ 的斜率 $=\\dfrac{-1-7}{8-2}=-\\dfrac43$。'),
            ('垂直平分線斜率 $=\\dfrac34$：', '$y-3=\\dfrac34(x-5)$，即 $3x-4y-3=0$。'),
            ('令 $y=0$：', '$3x=3\\Rightarrow x=1$，交點 $(1,0)$。')],
  'ans': '$3x-4y-3=0$；交點 $(1,0)$'}
},
{
 'n': 18,
 'title': 'DSE 2024 卷一 Q18 · 立體三角學',
 'tag': 'DSE 2024 · 卷一 · Q18',
 'h1': '先解平面，再投影到另一個平面',
 'sub': '三角學 · 兩平面的夾角 · 8 分題',
 'marks': '8 分',
 'q': '(a) $PQRS$ 是一塊薄的四邊形金屬片，其中 $PQ=12\\text{ cm}$、$PS=10\\text{ cm}$、$QR=13\\text{ cm}$、$\\angle QPS=82^{\\circ}$ 及 $\\angle QRS=65^{\\circ}$。求 (i) $QS$ 的長度；(ii) $\\angle RQS$。<br>'
       '(b) 把 (a) 中的金屬片沿 $QS$ 摺起，使平面 $PQS$ 與平面 $QRS$ 的夾角為 $80^{\\circ}$。'
       '(i) 求 $R$ 與平面 $PQS$ 的最短距離。(ii) 設 $X$ 為平面 $QRS$ 上的任意點。有人聲稱 $P$ 與 $X$ 的距離必大於 $8\\text{ cm}$。該聲稱是否正確？試解釋。',
 'steps': [
  {'tag': '第 1 步', 'title': '(a)(i) 在 $\\triangle PQS$ 用餘弦定理',
   'rule': ('餘弦定理', '$QS^{2}=PQ^{2}+PS^{2}-2(PQ)(PS)\\cos\\angle QPS$', '已知兩邊及夾角，求第三邊。'),
   'body': '    <p>$$QS^{2}=12^{2}+10^{2}-2(12)(10)\\cos82^{\\circ}\\approx244-33.40=210.60$$</p>\n'
           '    <p>$$QS\\approx14.5\\text{ cm}$$</p>'},
  {'tag': '第 2 步', 'title': '(a)(ii) 在 $\\triangle QRS$ 用正弦定理',
   'rule': ('正弦定理', '$\\dfrac{QR}{\\sin\\angle QSR}=\\dfrac{QS}{\\sin\\angle QRS}$', '已知 $QR$、$QS$ 及 $\\angle QRS$，先求 $\\angle QSR$。'),
   'body': '    <p>$$\\sin\\angle QSR=\\frac{13\\sin65^{\\circ}}{14.51}\\approx0.8119 \\quad\\Longrightarrow\\quad \\angle QSR\\approx54.3^{\\circ}$$</p>\n'
           '    <p>（$180^{\\circ}-54.3^{\\circ}=125.7^{\\circ}$ 會使內角和大於 $180^{\\circ}$，故捨去。）</p>\n'
           '    <p>$$\\angle RQS\\approx180^{\\circ}-65^{\\circ}-54.3^{\\circ}=60.7^{\\circ}$$</p>'},
  {'tag': '第 3 步', 'title': '(b)(i) 先求 $R$ 到 $QS$ 的距離',
   'rule': ('三角形的高', '$h_R=QR\\sin\\angle RQS$', '在 $\\triangle QRS$ 中，以 $QS$ 為底的高。'),
   'body': '    <p>$$h_R=13\\sin60.7^{\\circ}\\approx11.34\\text{ cm}$$</p>'},
  {'tag': '第 4 步', 'title': '(b)(i) 再把高投影到平面 $PQS$',
   'rule': ('兩平面夾角', '$d=h_R\\sin80^{\\circ}$', '兩個平面沿 $QS$ 相交，$R$ 到 $QS$ 的垂線與其在平面 $PQS$ 上的投影所成角，就是兩平面的夾角。'),
   'body': '    <p>$$d\\approx11.34\\sin80^{\\circ}\\approx11.2\\text{ cm}$$</p>'},
  {'tag': '第 5 步', 'title': '(b)(ii) 求 $P$ 到 $QS$ 的高',
   'rule': ('面積法', '$h_P=\\dfrac{2[PQS]}{QS}$', '$[PQS]=\\tfrac12(12)(10)\\sin82^{\\circ}\\approx59.42$。'),
   'body': '    <p>$$h_P=\\frac{2(59.42)}{14.51}\\approx8.19\\text{ cm}$$</p>'},
  {'tag': '第 6 步', 'title': '(b)(ii) 求 $P$ 到平面 $QRS$ 的最短距離',
   'body': '    <p>$$d_P\\approx8.19\\sin80^{\\circ}\\approx8.06\\text{ cm}$$</p>\n'
           '    <p>對平面 $QRS$ 上任意點 $X$，$PX\\ge d_P\\approx8.06>8$。</p>\n'
           '    <p>故聲稱 <b>正確</b>（$P$ 與平面上任何點的距離都大於 $8\\text{ cm}$）。</p>'}],
 'ans': '(a)(i) $QS\\approx14.5\\text{ cm}$　(ii) $\\angle RQS\\approx60.7^{\\circ}$　(b)(i) $\\approx11.2\\text{ cm}$　(ii) 正確，最短距離 $\\approx8.06>8$',
 'practice': {
  'q': '在 $\\triangle ABC$ 中，$AB=9\\text{ cm}$、$AC=7\\text{ cm}$、$\\angle BAC=70^{\\circ}$。(a) 求 $BC$。(b) 求 $\\angle ABC$。',
  'steps': [('(a) 餘弦定理：', '$BC^{2}=81+49-2(9)(7)\\cos70^{\\circ}\\approx130-43.10=86.90$，$BC\\approx9.32$。'),
            ('(b) 正弦定理：', '$\\sin\\angle ABC=\\dfrac{7\\sin70^{\\circ}}{9.32}\\approx0.706$。'),
            ('取銳角（$AC<BC$ 時 $\\angle B$ 為銳角）：', '$\\angle ABC\\approx44.9^{\\circ}$。')],
  'ans': '$BC\\approx9.32\\text{ cm}$；$\\angle ABC\\approx44.9^{\\circ}$'}
},
{
 'n': 19,
 'title': 'DSE 2024 卷一 Q19 · 配方法與菱形',
 'tag': 'DSE 2024 · 卷一 · Q19',
 'h1': '頂點、數列條件、平行四邊形三連環',
 'sub': '二次函數 · 數列 · 菱形 · 12 分題',
 'marks': '12 分',
 'q': '設 $f(x)=2x^{2}+4mx+8x+2m^{2}+8m+n$，其中 $m$、$n$ 為實常數且 $mn<0$。設 $y=f(x)$ 的圖象的頂點為 $P$。<br>'
       '(a) 用配方法，以 $m$、$n$ 表示 $P$ 的坐標。<br>'
       '(b) 描述由 $f(x)$ 變換成 $f\\!\\left(\\dfrac{x}{5}\\right)+7$ 的幾何意義。<br>'
       '(c) 設 $y=f\\!\\left(\\dfrac{x}{5}\\right)+7$ 的圖象的頂點為 $Q$。設 $(a_1,b_1)$ 及 $(a_2,b_2)$ 分別為 $P$ 及 $Q$ 的坐標。已知 $a_1,\\,1+n,\\,a_2$ 為等差數列，且 $b_1,\\,4-m,\\,b_2$ 為等比數列。'
       '(i) 求 $P$ 及 $Q$ 的坐標。(ii) 點 $R$、$S$ 的坐標分別為 $(3t+27,\\,t)$ 及 $(3t+3,\\,2t-3)$，其中 $t$ 為實數。$PQRS$ 是否可能為菱形？試解釋。',
 'steps': [
  {'tag': '第 1 步', 'title': '(a) 先整理再配方',
   'rule': ('配方法', '$2x^{2}+4(m+2)x=2\\left[(x+m+2)^{2}-(m+2)^{2}\\right]$', '先把 $x$ 的係數合併成 $4(m+2)$，再抽出 $2$。'),
   'body': '    <p>$$f(x)=2\\left[(x+m+2)^{2}-(m+2)^{2}\\right]+2m^{2}+8m+n$$</p>\n'
           '    <p>$$=2(x+m+2)^{2}-2m^{2}-8m-8+2m^{2}+8m+n=2(x+m+2)^{2}+n-8$$</p>'},
  {'tag': '第 2 步', 'title': '(a) 讀出頂點',
   'body': '    <p>$$P=(-m-2,\\;n-8)$$</p>'},
  {'tag': '第 3 步', 'title': '(b) 兩個變換的幾何意義',
   'rule': ('圖象變換', '$f\\!\\left(\\dfrac{x}{5}\\right)$：沿 $x$ 方向放大 $5$ 倍', '$x$ 換成 $\\dfrac{x}{5}$ 時，原本在 $x$ 的點移到 $5x$。'),
   'body': '    <p>$f\\!\\left(\\dfrac{x}{5}\\right)$：把圖象沿 $x$ 方向放大至 $5$ 倍（橫向伸延，縱向不變）；</p>\n'
           '    <p>$+7$：再把圖象向上平移 $7$ 個單位。</p>'},
  {'tag': '第 4 步', 'title': '(c)(i) 求 $Q$ 的坐標',
   'body': '    <p>$$f\\!\\left(\\frac{x}{5}\\right)+7=2\\left(\\frac{x}{5}+m+2\\right)^{2}+n-8+7$$</p>\n'
           '    <p>括號為零時 $x=-5(m+2)$，故</p>\n'
           '    <p>$$Q=(-5m-10,\\;n-1)$$</p>'},
  {'tag': '第 5 步', 'title': '(c)(i) 用等差條件',
   'rule': ('等差數列', '$2(1+n)=a_1+a_2$', '中間項的兩倍等於首尾之和。'),
   'body': '    <p>$$2(1+n)=(-m-2)+(-5m-10)=-6m-12$$</p>\n'
           '    <p>$$n=-3m-7 \\quad\\cdots(1)$$</p>'},
  {'tag': '第 6 步', 'title': '(c)(i) 用等比條件',
   'rule': ('等比數列', '$(4-m)^{2}=b_1b_2$', '中間項的平方等於首尾之積。'),
   'body': '    <p>$$b_1=n-8=-3m-15,\\qquad b_2=n-1=-3m-8$$</p>\n'
           '    <p>$$(4-m)^{2}=(-3m-15)(-3m-8)=9m^{2}+69m+120$$</p>\n'
           '    <p>$$8m^{2}+77m+104=0 \\quad\\Longrightarrow\\quad m=\\frac{-77\\pm51}{16}=-8\\;\\text{或}\\;-\\frac{13}{8}$$</p>'},
  {'tag': '第 7 步', 'title': '(c)(i) 用 $mn<0$ 篩選',
   'body': '    <p>$m=-8$：$n=17$，$mn=-136<0$ ✓</p>\n'
           '    <p>$m=-\\dfrac{13}{8}$：$n=-\\dfrac{17}{8}$，$mn>0$ ✗</p>\n'
           '    <p>故 $m=-8$、$n=17$，得</p>\n'
           '    <p>$$P=(6,9),\\qquad Q=(30,16)$$</p>\n'
           '    <p>驗算：$a_1,1+n,a_2=6,18,30$ 為等差 ✓；$b_1,4-m,b_2=9,12,16$ 為等比 ✓</p>'},
  {'tag': '第 8 步', 'title': '(c)(ii) 菱形首先是平行四邊形',
   'rule': ('平行四邊形', '$\\overrightarrow{PQ}=\\overrightarrow{SR}$', '$PQRS$ 為菱形 $\\Rightarrow$ 必為平行四邊形，對邊相等且平行。'),
   'body': '    <p>$$\\overrightarrow{PQ}=(24,7),\\qquad \\overrightarrow{SR}=R-S=(24,\\;3-t)$$</p>\n'
           '    <p>$$3-t=7 \\quad\\Longrightarrow\\quad t=-4$$</p>'},
  {'tag': '第 9 步', 'title': '(c)(ii) 驗證四邊相等',
   'body': '    <p>當 $t=-4$：$R=(15,-4)$、$S=(-9,-11)$</p>\n'
           '    <p>$$|PQ|=25,\\quad |QR|=\\sqrt{15^{2}+20^{2}}=25,\\quad |RS|=25,\\quad |SP|=25$$</p>\n'
           '    <p>四邊相等，故 $PQRS$ 可以是菱形（不是正方形，因 $\\overrightarrow{PQ}\\cdot\\overrightarrow{QR}\\neq0$）。</p>'}],
 'ans': '(a) $P(-m-2,\\,n-8)$　(b) 沿 $x$ 方向放大 $5$ 倍後上移 $7$ 個單位　(c)(i) $P(6,9)$、$Q(30,16)$　(ii) 可能，$t=-4$',
 'practice': {
  'q': '設 $g(x)=x^{2}-4kx+3$，頂點為 $P$。$g\\!\\left(\\dfrac{x}{2}\\right)-1$ 的頂點為 $Q$。若 $P$ 的 $x$ 坐標、$3$、$Q$ 的 $x$ 坐標成等差數列，求 $k$。',
  'steps': [('配方：', '$g(x)=(x-2k)^{2}+3-4k^{2}$，故 $P=(2k,\\,3-4k^{2})$。'),
            ('$g\\!\\left(\\dfrac{x}{2}\\right)-1=(\\dfrac{x}{2}-2k)^{2}+2-4k^{2}$，', '頂點 $x=4k$，即 $Q=(4k,\\,2-4k^{2})$。'),
            ('等差：', '$2(3)=2k+4k\\Rightarrow k=1$。')],
  'ans': '$k=1$'}
},
]
