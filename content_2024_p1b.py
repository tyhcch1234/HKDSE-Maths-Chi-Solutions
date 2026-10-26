#!/usr/bin/env python3
# 2024 卷一 Q7–Q11 內容（含 SVG 圖）
SVG_Q7 = """<svg viewBox="0 0 420 380" width="400" role="img" aria-label="極坐標系中 P、Q、R 三點">
  <g fill="none" stroke="currentColor" stroke-width="1.1">
    <line x1="200" y1="190" x2="392" y2="190"/>
    <line x1="200" y1="190" x2="230.9" y2="138.6"/>
    <line x1="200" y1="190" x2="105.7" y2="133.3"/>
    <line x1="200" y1="190" x2="122.8" y2="318.6"/>
    <path d="M200,190 m 42,0 a 42,42 0 0 0 -21.6,-36" stroke-opacity=".45"/>
    <path d="M200,190 m -40,0 a 40,40 0 0 0 19,-35.5" stroke-opacity=".0"/>
  </g>
  <polygon points="230.9,138.6 105.7,133.3 122.8,318.6" fill="currentColor" fill-opacity="0.06"
           stroke="currentColor" stroke-width="1.1" stroke-dasharray="5 4" stroke-opacity=".6"/>
  <g fill="currentColor">
    <circle cx="200" cy="190" r="3"/>
    <circle cx="230.9" cy="138.6" r="3.4"/>
    <circle cx="105.7" cy="133.3" r="3.4"/>
    <circle cx="122.8" cy="318.6" r="3.4"/>
  </g>
  <g fill="currentColor" font-family="Georgia,serif" font-style="italic" font-size="14">
    <text x="192" y="208" text-anchor="end">O</text>
    <text x="238" y="132">P</text>
    <text x="96" y="126" text-anchor="end">Q</text>
    <text x="114" y="334" text-anchor="end">R</text>
    <text x="392" y="184" text-anchor="end" font-style="normal" font-size="11">極軸</text>
  </g>
  <g fill="currentColor" font-size="11" font-family="system-ui,sans-serif">
    <text x="243" y="167">11</text>
    <text x="143" y="170">60</text>
    <text x="168" y="262">144</text>
    <text x="221" y="176">59°</text>
    <text x="141" y="183">149°</text>
    <text x="169" y="230">239°</text>
  </g>
</svg>"""

SVG_Q8 = """<svg viewBox="0 0 420 360" width="400" role="img" aria-label="五邊形 ADBCE，AC 與 BD 交於 E">
  <polygon points="40,40 40,208 376,208 241.6,308.8 166,208" fill="currentColor" fill-opacity="0.10"
           stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>
  <g fill="none" stroke="currentColor" stroke-width="1.1">
    <path d="M40,196 L52,196 L52,208"/>
    <path d="M233.2,297.6 L244.4,289.2 L252.8,300.4"/>
  </g>
  <g fill="currentColor">
    <circle cx="40" cy="40" r="3"/><circle cx="40" cy="208" r="3"/><circle cx="376" cy="208" r="3"/>
    <circle cx="241.6" cy="308.8" r="3"/><circle cx="166" cy="208" r="3"/>
  </g>
  <g fill="currentColor" font-family="Georgia,serif" font-style="italic" font-size="14">
    <text x="32" y="34" text-anchor="end">A</text>
    <text x="30" y="212" text-anchor="end">D</text>
    <text x="384" y="212">B</text>
    <text x="247" y="327">C</text>
    <text x="166" y="201" text-anchor="middle" font-size="13">E</text>
  </g>
  <g fill="currentColor" font-size="11" font-family="system-ui,sans-serif">
    <text x="26" y="128" text-anchor="middle" transform="rotate(-90 26 128)">12 cm</text>
    <text x="314" y="268" transform="rotate(-36.9 314 268)">12 cm</text>
    <text x="103" y="222" text-anchor="middle">9 cm</text>
  </g>
</svg>"""

TBL_Q9 = """<table class="dtable">
  <tr><th>鎖匙數目</th><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr>
  <tr><th>家庭主婦人數</th><td>10</td><td>9</td><td>4</td><td>3</td><td>4</td><td>$k$</td></tr>
</table>"""

TBL_Q11 = """<table class="dtable">
  <tr><th>幹（十位）</th><th>葉（個位）</th></tr>
  <tr><td class="rowhead">2</td><td>0&nbsp;&nbsp;0&nbsp;&nbsp;1&nbsp;&nbsp;a&nbsp;&nbsp;a&nbsp;&nbsp;a&nbsp;&nbsp;8&nbsp;&nbsp;8&nbsp;&nbsp;9</td></tr>
  <tr><td class="rowhead">3</td><td>0&nbsp;&nbsp;0&nbsp;&nbsp;2&nbsp;&nbsp;3&nbsp;&nbsp;4&nbsp;&nbsp;4&nbsp;&nbsp;7&nbsp;&nbsp;9</td></tr>
  <tr><td class="rowhead">4</td><td>0&nbsp;&nbsp;b</td></tr>
</table>"""

P1_B = [
{
 'n': 7,
 'title': 'DSE 2024 卷一 Q7 · 極坐標與三角形',
 'tag': 'DSE 2024 · 卷一 · Q7',
 'h1': '三點繞原點排成直角',
 'sub': '極坐標 · 距離與周界 · 4 分題',
 'marks': '4 分',
 'q': '在極坐標系中，$O$ 為極點。點 $P$、$Q$、$R$ 的極坐標分別為 $(11,59^{\\circ})$、$(60,149^{\\circ})$ 及 $(144,239^{\\circ})$。<br>'
       '(a) 求 $\\angle POQ$。<br>'
       '(b) $P$、$O$、$R$ 三點是否共線？試解釋你的答案。<br>'
       '(c) 求 $\\triangle PQR$ 的周界。',
 'fig': SVG_Q7,
 'cap': '極坐標系（示意圖，非按比例）',
 'steps': [
  {'tag': '第 1 步', 'title': '(a) 同一極點，角度直接相減',
   'rule': ('極角', '$\\angle POQ=\\theta_Q-\\theta_P$', '兩射線由同一極軸量起，夾角就是極角之差。'),
   'body': '    <p>$$\\angle POQ=149^{\\circ}-59^{\\circ}=90^{\\circ}$$</p>'},
  {'tag': '第 2 步', 'title': '(b) 相差 $180^{\\circ}$ 即反向共線',
   'rule': ('共線條件', '$\\theta_R-\\theta_P=180^{\\circ}$', '由同一點出發、方向相反的兩條射線，合起來就是一條直線。'),
   'body': '    <p>$$239^{\\circ}-59^{\\circ}=180^{\\circ}$$</p>\n'
           '    <p>所以 $OP$ 與 $OR$ 是同一條直線上的相反射線，且 $O$ 位於 $P$ 與 $R$ 之間，故 $P$、$O$、$R$ 共線。</p>'},
  {'tag': '第 3 步', 'title': '(c) 求 $PQ$',
   'rule': ('勾股定理', '$PQ=\\sqrt{OP^{2}+OQ^{2}}$', '已知 $\\angle POQ=90^{\\circ}$，$\\triangle POQ$ 是直角三角形。'),
   'body': '    <p>$$PQ=\\sqrt{11^{2}+60^{2}}=\\sqrt{121+3600}=\\sqrt{3721}=61$$</p>'},
  {'tag': '第 4 步', 'title': '(c) 求 $QR$',
   'body': '    <p>同理 $\\angle QOR=239^{\\circ}-149^{\\circ}=90^{\\circ}$，故</p>\n'
           '    <p>$$QR=\\sqrt{60^{2}+144^{2}}=\\sqrt{3600+20736}=\\sqrt{24336}=156$$</p>'},
  {'tag': '第 5 步', 'title': '(c) 求 $PR$ 與周界',
   'rule': ('共線三點', '$PR=OP+OR$', '由 (b) 知 $O$ 在 $P$、$R$ 之間，兩段可直接相加。'),
   'body': '    <p>$$PR=11+144=155$$</p>\n'
           '    <p>$$\\text{周界}=61+156+155=372$$</p>'}],
 'ans': '(a) $90^{\\circ}$　(b) 共線（$239^{\\circ}-59^{\\circ}=180^{\\circ}$）　(c) $372$',
 'practice': {
  'q': '在極坐標系中，$A$、$B$ 的極坐標分別為 $(5,40^{\\circ})$ 及 $(5,130^{\\circ})$。求 $\\angle AOB$ 及 $AB$ 的長度。',
  'steps': [('夾角：', '$130^{\\circ}-40^{\\circ}=90^{\\circ}$。'),
            ('直角三角形，兩腰均為 $5$：', '$AB=\\sqrt{5^{2}+5^{2}}=\\sqrt{50}=5\\sqrt{2}$。')],
  'ans': '$\\angle AOB=90^{\\circ}$，$AB=5\\sqrt{2}$'}
},
{
 'n': 8,
 'title': 'DSE 2024 卷一 Q8 · 全等三角形與五邊形面積',
 'tag': 'DSE 2024 · 卷一 · Q8',
 'h1': 'RHS 全等，再把五邊形切開',
 'sub': '全等與相似 · 面積 · 5 分題',
 'marks': '5 分',
 'q': '圖中 $E$ 為 $AC$ 與 $BD$ 的交點。已知 $\\angle ACB=\\angle ADB=90^{\\circ}$ 及 $BC=AD$。<br>'
       '(a) 證明 $\\triangle ABC\\cong\\triangle BAD$。<br>'
       '(b) 若 $AD=12\\text{ cm}$ 及 $DE=9\\text{ cm}$，求五邊形 $ADBCE$ 的面積。',
 'fig': SVG_Q8,
 'cap': '$AC$ 與 $BD$ 交於 $E$；$\\angle ACB=\\angle ADB=90^{\\circ}$，$BC=AD$',
 'steps': [
  {'tag': '第 1 步', 'title': '(a) 找出三個全等條件',
   'rule': ('RHS 全等', '直角 + 斜邊 + 一股', '兩個直角三角形只要斜邊及其中一股分別相等，便全等。'),
   'body': '    <p>在 $\\triangle ABC$ 與 $\\triangle BAD$ 中：</p>\n'
           '    <p>$\\angle ACB=\\angle ADB=90^{\\circ}$（已知）</p>\n'
           '    <p>$AB=BA$（公共邊，同為斜邊）</p>\n'
           '    <p>$BC=AD$（已知）</p>\n'
           '    <p>$$\\therefore\\;\\triangle ABC\\cong\\triangle BAD\\quad(\\text{RHS})$$</p>'},
  {'tag': '第 2 步', 'title': '(a) 全等帶來的有用結論',
   'rule': ('全等三角形的對應部分', '$AC=BD$，$\\angle ABE=\\angle BAE$', '對應邊相等、對應角相等，是後面計算的關鍵。'),
   'body': '    <p>由全等得 $AC=BD$，且 $\\angle ABE=\\angle BAE$。</p>'},
  {'tag': '第 3 步', 'title': '(b) 在 $\\triangle ADE$ 求 $AE$',
   'rule': ('勾股定理', '$AE^{2}=AD^{2}+DE^{2}$', '$\\angle ADE=90^{\\circ}$（因 $\\angle ADB=90^{\\circ}$ 且 $E$ 在 $BD$ 上）。'),
   'body': '    <p>$$AE=\\sqrt{12^{2}+9^{2}}=\\sqrt{144+81}=15\\text{ cm}$$</p>'},
  {'tag': '第 4 步', 'title': '(b) 求 $BE$、$BD$、$AC$、$CE$',
   'rule': ('等角對等邊', '$\\angle ABE=\\angle BAE\\Rightarrow AE=BE$', '在同一個三角形中，兩個底角相等，對應的兩邊也相等。'),
   'body': '    <p>$$BE=AE=15\\text{ cm}$$</p>\n'
           '    <p>$$BD=BE+DE=15+9=24\\text{ cm}$$</p>\n'
           '    <p>由 $AC=BD$ 得 $AC=24\\text{ cm}$，故</p>\n'
           '    <p>$$CE=AC-AE=24-15=9\\text{ cm}$$</p>'},
  {'tag': '第 5 步', 'title': '(b) 把五邊形分成兩個三角形',
   'rule': ('分割求面積', '$[ADBCE]=[ADB]+[BCE]$', '$BD$ 把五邊形分成上方與下方兩個三角形。'),
   'body': '    <p>$$\\begin{aligned}\\text{面積}&=\\tfrac12(AD)(BD)+\\tfrac12(BC)(CE)\\\\'
           '&=\\tfrac12(12)(24)+\\tfrac12(12)(9)\\\\&=144+54=198\\text{ cm}^{2}\\end{aligned}$$</p>'}],
 'ans': '(a) 見題解（RHS）　(b) $198\\text{ cm}^{2}$',
 'practice': {
  'q': '在 $\\triangle ABC$ 中，$\\angle ACB=90^{\\circ}$，$AC=8\\text{ cm}$、$BC=15\\text{ cm}$。$D$ 為 $AB$ 上的點使 $CD\\perp AB$。求 $CD$。',
  'steps': [('斜邊：', '$AB=\\sqrt{8^{2}+15^{2}}=17$。'),
            ('用面積的兩種算法：', '$\\tfrac12(8)(15)=\\tfrac12(17)(CD)$。'),
            ('解出：', '$CD=\\dfrac{120}{17}\\approx7.06\\text{ cm}$。')],
  'ans': '$CD=\\dfrac{120}{17}\\text{ cm}$'}
},
{
 'n': 9,
 'title': 'DSE 2024 卷一 Q9 · 統計與概率',
 'tag': 'DSE 2024 · 卷一 · Q9',
 'h1': '由概率反求 $k$，再讀平均數、眾數、中位數',
 'sub': '統計 · 概率 · 5 分題',
 'marks': '5 分',
 'q': '下表顯示一組家庭主婦擁有鎖匙數目的分佈。' + TBL_Q9 +
       '若從該組中隨機選出一名家庭主婦，則她擁有超過 6 條鎖匙的概率為 $\\dfrac{5}{18}$。<br>'
       '(a) 求 $k$。<br>(b) 寫出該分佈的平均數、眾數及中位數。',
 'steps': [
  {'tag': '第 1 步', 'title': '數清有利情況與總數',
   'rule': ('概率', '$P=\\dfrac{\\text{有利情況數目}}{\\text{總數}}$', '「超過 6 條」即 7 條或 8 條。'),
   'body': '    <p>擁有超過 6 條鎖匙的人數為 $4+k$，總人數為 $10+9+4+3+4+k=30+k$。</p>'},
  {'tag': '第 2 步', 'title': '(a) 解方程求 $k$',
   'rule': ('交叉相乘', '$\\dfrac{4+k}{30+k}=\\dfrac{5}{18}$', '分式方程先去分母，再整理同類項。'),
   'body': '    <p>$$18(4+k)=5(30+k)$$</p>\n    <p>$$72+18k=150+5k \\quad\\Longrightarrow\\quad 13k=78 \\quad\\Longrightarrow\\quad k=6$$</p>'},
  {'tag': '第 3 步', 'title': '(b) 平均數',
   'rule': ('加權平均', '$\\bar x=\\dfrac{\\sum fx}{\\sum f}$', '每個數據值乘以其次數，再除以總人數。'),
   'body': '    <p>總鎖匙數 $=3(10)+4(9)+5(4)+6(3)+7(4)+8(6)=30+36+20+18+28+48=180$</p>\n'
           '    <p>總人數 $=30+6=36$</p>\n'
           '    <p>$$\\text{平均數}=\\frac{180}{36}=5$$</p>'},
  {'tag': '第 4 步', 'title': '(b) 眾數',
   'rule': ('眾數', '次數最大的數據值', '比較各次數 $10,9,4,3,4,6$。'),
   'body': '    <p>最大次數為 $10$，對應 $3$ 條鎖匙，故眾數為 $3$。</p>'},
  {'tag': '第 5 步', 'title': '(b) 中位數',
   'rule': ('累積頻數', '第 $\\dfrac{n}{2}$ 與 $\\dfrac{n}{2}+1$ 個數據的平均', '$n=36$ 為偶數，中位數取第 18、19 個數據的平均。'),
   'body': '    <p>累積頻數：$10,\\;19,\\;23,\\;26,\\;30,\\;36$。第 18 及第 19 個數據都落在「4 條」一組（$10<18,19\\le19$）。</p>\n'
           '    <p>$$\\text{中位數}=4$$</p>'}],
 'ans': '(a) $k=6$　(b) 平均數 $=5$，眾數 $=3$，中位數 $=4$',
 'practice': {
  'q': '某組數據 $1,2,3,4$ 的次數分別為 $5,8,k,4$。若平均數為 $2.5$，求 $k$ 及眾數。',
  'steps': [('總和：', '$5+16+3k+16=37+3k$；總數 $=17+k$。'),
            ('列方程：', '$37+3k=2.5(17+k)\\Rightarrow 0.5k=5.5\\Rightarrow k=11$。'),
            ('找眾數：', '次數最大為 $11$，對應數據值 $3$。')],
  'ans': '$k=11$，眾數 $=3$'}
},
{
 'n': 10,
 'title': 'DSE 2024 卷一 Q10 · 變分與判別式',
 'tag': 'DSE 2024 · 卷一 · Q10',
 'h1': '部分常數、部分隨 $x$ 變 → 直線方程',
 'sub': '變分 · 二次方程 · 6 分題',
 'marks': '6 分',
 'q': '已知 $g(x)$ 部分為常數，部分隨 $x$ 正變。設 $g(-3)=-21$ 及 $g(7)=9$。<br>'
       '(a) 求 $g(x)$。<br>'
       '(b) 設 $h(x)=x\\,g(x)+k$，其中 $k$ 為實常數。若方程 $h(x)=0$ 的所有根均為實數，求 $k$ 的取值範圍。',
 'steps': [
  {'tag': '第 1 步', 'title': '(a) 把文字條件寫成模型',
   'rule': ('部分常數、部分正變', '$g(x)=a+bx$', '「部分為常數」是常數項 $a$，「部分隨 $x$ 正變」是 $bx$。'),
   'body': '    <p>設 $g(x)=a+bx$，其中 $a$、$b$ 為常數。</p>'},
  {'tag': '第 2 步', 'title': '(a) 代入兩點得聯立方程',
   'body': '    <p>$$g(-3)=-21:\\; a-3b=-21 \\quad\\cdots(1)$$</p>\n'
           '    <p>$$g(7)=9:\\; a+7b=9 \\quad\\cdots(2)$$</p>'},
  {'tag': '第 3 步', 'title': '(a) 解聯立方程',
   'rule': ('消去 $a$', '$(2)-(1)$', '兩式的 $a$ 係數相同，相減即可消去 $a$。'),
   'body': '    <p>$$10b=30 \\quad\\Longrightarrow\\quad b=3$$</p>\n'
           '    <p>代入 (2)：$a+21=9 \\Rightarrow a=-12$</p>\n'
           '    <p>$$\\therefore\\; g(x)=3x-12$$</p>\n'
           '    <p>驗算：$g(-3)=-9-12=-21$ ✓，$g(7)=21-12=9$ ✓</p>'},
  {'tag': '第 4 步', 'title': '(b) 寫出二次方程',
   'body': '    <p>$$h(x)=x(3x-12)+k=3x^{2}-12x+k$$</p>\n'
           '    <p>方程 $h(x)=0$ 即 $3x^{2}-12x+k=0$。</p>'},
  {'tag': '第 5 步', 'title': '(b) 「所有根均為實數」→ 判別式 $\\ge0$',
   'rule': ('判別式', '$\\Delta=b^{2}-4ac\\ge0$', '二次方程的根為實數（包括重根）的充要條件是判別式非負。'),
   'body': '    <p>$$\\Delta=(-12)^{2}-4(3)(k)=144-12k\\ge0$$</p>\n'
           '    <p>$$12k\\le144 \\quad\\Longrightarrow\\quad k\\le12$$</p>'},
  {'tag': '第 6 步', 'title': '(b) 圖象意義',
   'body': '    <p>$k\\le12$ 時，拋物線 $y=3x^{2}-12x+k$ 與 $x$ 軸相交（$k=12$ 時只有一個重根，仍屬實數根）；$k>12$ 時整條拋物線在 $x$ 軸上方，沒有實根。</p>'}],
 'ans': '(a) $g(x)=3x-12$　(b) $k\\le12$',
 'practice': {
  'q': '已知 $g(x)$ 部分為常數、部分隨 $x$ 正變，且 $g(1)=5$、$g(3)=11$。設 $h(x)=x\\,g(x)+k$，若 $h(x)=0$ 的所有根均為實數，求 $k$ 的取值範圍。',
  'steps': [('設 $g(x)=a+bx$：', '$a+b=5$，$a+3b=11\\Rightarrow b=3,\\;a=2$，即 $g(x)=3x+2$。'),
            ('二次方程：', '$3x^{2}+2x+k=0$。'),
            ('判別式：', '$4-12k\\ge0\\Rightarrow k\\le\\dfrac13$。')],
  'ans': '$g(x)=3x+2$；$k\\le\\dfrac13$'}
},
{
 'n': 11,
 'title': 'DSE 2024 卷一 Q11 · 葉幹圖與離差',
 'tag': 'DSE 2024 · 卷一 · Q11',
 'h1': '平均數定出 $a$、$b$，再挑最極端的組合',
 'sub': '統計 · 葉幹圖 · 分佈域與四分位距 · 7 分題',
 'marks': '7 分',
 'q': '以下的葉幹圖顯示一組研究員在一個月內閱讀期刊所花時數（小時）的分佈。' + TBL_Q11 +
       '該分佈的平均數為 $30$。<br>(a) 求 $a$ 及 $b$。<br>(b) 寫出該分佈的最小可能分佈域。<br>'
       '(c) 求該分佈的最大可能四分位距。',
 'steps': [
  {'tag': '第 1 步', 'title': '數清數據並寫出總和',
   'rule': ('葉幹圖讀法', '$3\\,|\\,2$ 代表 $32$ 小時', '每片葉的值 = 幹 $\\times10$ + 葉。'),
   'body': '    <p>共有 $9+8+2=19$ 個數據。以幹 ×10 + 葉計算總和：</p>\n'
           '    <p>幹 2：$9\\times20+(0+0+1+3a+8+8+9)=180+26+3a=206+3a$</p>\n'
           '    <p>幹 3：$8\\times30+(0+0+2+3+4+4+7+9)=240+29=269$</p>\n'
           '    <p>幹 4：$2\\times40+(0+b)=80+b$</p>'},
  {'tag': '第 2 步', 'title': '(a) 用平均數列方程',
   'rule': ('平均數', '$\\dfrac{\\text{總和}}{19}=30$', '平均數乘以數據個數，就是總和。'),
   'body': '    <p>$$(206+3a)+269+(80+b)=30\\times19=570$$</p>\n'
           '    <p>$$3a+b=15$$</p>'},
  {'tag': '第 3 步', 'title': '(a) 列出所有單數字組合',
   'body': '    <p>$a$、$b$ 都是 $0$ 至 $9$ 的數字，故</p>\n'
           '    <p>$$(a,b)=(2,9),\\;(3,6),\\;(4,3),\\;(5,0)$$</p>'},
  {'tag': '第 4 步', 'title': '(b) 最小可能分佈域',
   'rule': ('分佈域', '最大值 $-$ 最小值', '最小值固定為 $20$，只有 $b$ 會影響最大值 $40+b$。'),
   'body': '    <p>$b$ 越小，最大值越接近 $40$。取 $b=0$：</p>\n'
           '    <p>$$\\text{分佈域}=40-20=20$$</p>'},
  {'tag': '第 5 步', 'title': '(c) 比較四個組合的四分位數',
   'rule': ('四分位數位置', '$Q_1$ 為第 5 個、$Q_3$ 為第 15 個數據', '$19$ 個數據的中位數是第 10 個；上下半各 9 個，取各半的中位（第 5、15 個）。'),
   'body': '    <p>幹 3 與幹 4 的數據不變，故 $Q_3$ 恆為第 15 個數據 $=34$。$Q_1$ 只受 $a$ 影響：</p>\n'
           '    <p>$a=2$：$20,20,21,22,22,22,28,28,29\\Rightarrow Q_1=22$</p>\n'
           '    <p>$a=3$：$Q_1=23$；$a=4$：$Q_1=24$；$a=5$：$Q_1=25$</p>\n'
           '    <p>$a$ 越小，$Q_1$ 越小，四分位距越大。</p>'},
  {'tag': '第 6 步', 'title': '(c) 最大四分位距',
   'body': '    <p>取 $a=2$（此時 $b=9$）：</p>\n'
           '    <p>$$\\text{四分位距}=Q_3-Q_1=34-22=12$$</p>'}],
 'ans': '(a) $(a,b)=(2,9),(3,6),(4,3)$ 或 $(5,0)$　(b) $20$　(c) $12$',
 'practice': {
  'q': '以下 19 個數據已由小至大排列：$12,15,18,20,22,25,28,30,32,35,38,40,42,45,48,50,52,55,58$。求四分位距。',
  'steps': [('中位數：', '$n=19$，第 10 個數據 $=35$。'),
            ('下半 9 個的中位為第 5 個：', '$Q_1=22$。'),
            ('上半 9 個的中位為第 15 個：', '$Q_3=48$。')],
  'ans': '四分位距 $=48-22=26$'}
},
]
