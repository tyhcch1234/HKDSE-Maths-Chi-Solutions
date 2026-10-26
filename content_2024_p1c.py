#!/usr/bin/env python3
# 2024 卷一 Q12–Q15 內容
SVG_Q12 = """<svg viewBox="0 0 340 250" width="330" role="img" aria-label="正方形 ABCD 與直線 y=mx">
  <line x1="20" y1="220" x2="320" y2="220" stroke="currentColor" stroke-width="1"/>
  <line x1="40" y1="240" x2="40" y2="30" stroke="currentColor" stroke-width="1"/>
  <line x1="40" y1="220" x2="300" y2="60" stroke="currentColor" stroke-width="1.2" stroke-dasharray="6 4"/>
  <line x1="40" y1="220" x2="280" y2="100" stroke="currentColor" stroke-width="1.2"/>
  <rect x="160" y="100" width="120" height="120" fill="currentColor" fill-opacity="0.08"
        stroke="currentColor" stroke-width="1.4"/>
  <g fill="currentColor">
    <circle cx="40" cy="220" r="3"/><circle cx="160" cy="220" r="3"/>
    <circle cx="280" cy="220" r="3"/><circle cx="160" cy="100" r="3"/><circle cx="280" cy="100" r="3"/>
  </g>
  <g fill="currentColor" font-family="Georgia,serif" font-style="italic" font-size="14">
    <text x="30" y="236" text-anchor="end">O</text>
    <text x="160" y="240" text-anchor="middle">B</text>
    <text x="284" y="240">A</text>
    <text x="150" y="96" text-anchor="end">C</text>
    <text x="288" y="96">D</text>
    <text x="300" y="52" font-size="12">y = mx</text>
  </g>
</svg>"""

SVG_Q13 = """<svg viewBox="0 0 340 270" width="330" role="img" aria-label="正四角錐被平行於底面的平面切開">
  <polygon points="100,160 300,160 260,220 60,220" fill="currentColor" fill-opacity="0.05"
           stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/>
  <polygon points="120,130 270,130 240,175 90,175" fill="currentColor" fill-opacity="0.16"
           stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/>
  <g fill="none" stroke="currentColor" stroke-width="1.2">
    <line x1="60" y1="220" x2="90" y2="175"/><line x1="260" y1="220" x2="240" y2="175"/>
    <line x1="300" y1="160" x2="270" y2="130"/><line x1="100" y1="160" x2="120" y2="130"/>
    <line x1="90" y1="175" x2="180" y2="40"/><line x1="240" y1="175" x2="180" y2="40"/>
    <line x1="120" y1="130" x2="180" y2="40"/><line x1="270" y1="130" x2="180" y2="40"/>
    <line x1="180" y1="40" x2="180" y2="190" stroke-dasharray="4 3"/>
  </g>
  <g fill="currentColor" font-family="Georgia,serif" font-style="italic" font-size="14">
    <text x="184" y="34">頂點</text>
    <text x="248" y="196">X（平截頭體）</text>
    <text x="188" y="118">Y</text>
  </g>
  <g fill="currentColor" font-size="11" font-family="system-ui,sans-serif">
    <text x="176" y="214" text-anchor="end">底邊 64 cm</text>
    <text x="186" y="130">高 24 cm</text>
  </g>
</svg>"""

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
    <text x="200" y="352" text-anchor="middle">C 以 QR 為直徑，半徑 √65</text>
  </g>
</svg>"""

P1_C = [
{
 'n': 12,
 'title': 'DSE 2024 卷一 Q12 · 坐標幾何（正方形）',
 'tag': 'DSE 2024 · 卷一 · Q12',
 'h1': '先設坐標，斜率自然浮現',
 'sub': '坐標幾何 · 直線與正方形 · 7 分題',
 'marks': '7 分',
 'q': '設 $O$ 為原點。<br>'
       '(a) $A$、$B$ 為 $x$ 軸正半軸上的點，且 $A$ 的 $x$ 坐標大於 $B$ 的 $x$ 坐標。過 $B$ 的鉛垂線與直線 $y=mx$ 交於 $C$，使 $AB=BC$，其中 $m$ 為正常數。設 $D$ 為一點使 $ABCD$ 為正方形。以 $m$ 表示 $OD$ 的斜率。<br>'
       '(b) 點 $M$、$N$ 的坐標分別為 $(6,5)$ 及 $(10,0)$。設 $P$、$Q$ 分別位於 $OM$ 與 $MN$ 上，$R$、$S$ 位於 $x$ 軸上。若四邊形 $PQRS$ 為正方形，求 $P$ 的 $x$ 坐標。',
 'fig': SVG_Q12,
 'cap': '取 $B=(b,0)$：$C=(b,mb)$，$AB=BC=mb$，正方形邊長即 $mb$',
 'steps': [
  {'tag': '第 1 步', 'title': '(a) 設 $B$ 的坐標',
   'rule': ('點在直線上', '$C=(b,mb)$', '過 $B$ 的鉛垂線是 $x=b$，代入 $y=mx$ 得 $C$ 的 $y$ 坐標。'),
   'body': '    <p>設 $B=(b,0)$，則 $C=(b,mb)$，故 $BC=mb$。由 $AB=BC$ 且 $A$ 在 $B$ 的右方，</p>\n'
           '    <p>$$A=(b+mb,\\,0)$$</p>'},
  {'tag': '第 2 步', 'title': '(a) 寫出 $D$ 的坐標',
   'rule': ('正方形的性質', '$\\overrightarrow{AD}=\\overrightarrow{BC}$', '$ABCD$ 順序為正方形，$AD$ 與 $BC$ 平行且等長。'),
   'body': '    <p>$$D=A+\\overrightarrow{BC}=(b+mb,\\;mb)$$</p>'},
  {'tag': '第 3 步', 'title': '(a) 求 $OD$ 的斜率',
   'rule': ('斜率', '$\\dfrac{y_D-y_O}{x_D-x_O}$', '$O$ 為原點，直接讀 $D$ 的坐標。'),
   'body': '    <p>$$\\text{斜率}=\\frac{mb-0}{(b+mb)-0}=\\frac{mb}{b(1+m)}=\\frac{m}{1+m}$$</p>'},
  {'tag': '第 4 步', 'title': '(b) 用 (a) 的結果找 $OQ$',
   'rule': ('代入 $m=\\dfrac56$', '$\\text{斜率}=\\dfrac{m}{1+m}$', '$Q$ 在 (a) 中扮演「正方形的遠角」，與 $D$ 的角色相同。'),
   'body': '    <p>$OM$ 的斜率 $=\\dfrac{5-0}{6-0}=\\dfrac56$。由 (a)，</p>\n'
           '    <p>$$OQ\\text{ 的斜率}=\\frac{5/6}{1+5/6}=\\frac{5}{11} \\quad\\Longrightarrow\\quad OQ:\\; y=\\frac{5x}{11}$$</p>'},
  {'tag': '第 5 步', 'title': '(b) 求 $MN$ 的方程及 $Q$',
   'rule': ('兩點式', '$\\dfrac{y-0}{x-10}=\\dfrac{5-0}{6-10}$', '$M(6,5)$、$N(10,0)$ 決定直線 $MN$。'),
   'body': '    <p>$$MN:\\; y=-\\frac54(x-10)$$</p>\n'
           '    <p>解 $\\dfrac{5x}{11}=-\\dfrac54x+\\dfrac{25}{2}$，兩邊乘 $44$：</p>\n'
           '    <p>$$20x=-55x+550 \\quad\\Longrightarrow\\quad x=\\frac{22}{3},\\quad y=\\frac{10}{3}$$</p>\n'
           '    <p>即 $Q=\\left(\\dfrac{22}{3},\\dfrac{10}{3}\\right)$。</p>'},
  {'tag': '第 6 步', 'title': '(b) 由 $Q$ 向左量邊長得 $P$',
   'rule': ('正方形邊長', '$PQ=RS$ 且 $PQ\\parallel RS$', '$RS$ 在 $x$ 軸上，所以 $PQ$ 是水平線；邊長等於 $Q$ 的 $y$ 坐標（即 $SP$）。'),
   'body': '    <p>邊長 $=y_Q=\\dfrac{10}{3}$，$P$ 在 $Q$ 左方同一高度：</p>\n'
           '    <p>$$x_P=\\frac{22}{3}-\\frac{10}{3}=4$$</p>\n'
           '    <p>驗算：$P=\\left(4,\\dfrac{10}{3}\\right)$，而 $\\dfrac56\\times4=\\dfrac{10}{3}$，確在 $OM$ 上 ✓</p>'}],
 'ans': '(a) $\\dfrac{m}{1+m}$　(b) $x_P=4$',
 'practice': {
  'q': '直線 $L$ 通過 $O(0,0)$ 與 $A(8,6)$。點 $B$ 在 $x$ 軸上，過 $B$ 的鉛垂線交 $L$ 於 $C$，且 $AB=BC$，$ABCD$ 為正方形。求 $D$ 的坐標及 $OD$ 的斜率。',
  'steps': [('$m=\\dfrac68=\\dfrac34$，由 (a) 斜率', '$=\\dfrac{3/4}{1+3/4}=\\dfrac37$。'),
            ('設 $B=(b,0)$：$C=\\left(b,\\dfrac34b\\right)$，$AB=\\dfrac34b$，', '$D=\\left(\\dfrac74b,\\dfrac34b\\right)$。'),
            ('$OD$ 的斜率與 $b$ 無關：', '$=\\dfrac{3}{7}$。')],
  'ans': '$OD$ 的斜率為 $\\dfrac37$（$D$ 隨 $b$ 變，但斜率固定）'}
},
{
 'n': 13,
 'title': 'DSE 2024 卷一 Q13 · 平截頭體與相似',
 'tag': 'DSE 2024 · 卷一 · Q13',
 'h1': '先證相似，再用體積與表面積把關',
 'sub': '求積法 · 相似立體 · 8 分題',
 'marks': '8 分',
 'q': '一個直立角錐的底面是邊長 $64\\text{ cm}$ 的正方形，高為 $24\\text{ cm}$。該角錐被一個平行於底面的平面分成平截頭體 $X$ 與角錐 $Y$，已知 $Y$ 的高為 $18\\text{ cm}$。<br>'
       '(a) 求 $X$ 的體積。<br>'
       '(b) 另一個直立角錐的底面是正方形，被平行於底面的平面分成平截頭體 $Z$ 與一個角錐。已知 $Z$ 的高及總表面積分別為 $3\\text{ cm}$ 及 $960\\text{ cm}^{2}$。$X$ 與 $Z$ 是否相似？試解釋。',
 'fig': SVG_Q13,
 'cap': '平行於底面的平面切出與原角錐相似的 $Y$',
 'steps': [
  {'tag': '第 1 步', 'title': '確認 $Y$ 與整個角錐相似',
   'rule': ('相似比', '$k=\\dfrac{18}{24}=\\dfrac34$', '平行於底面的截面必與底面相似，故 $Y$ 與原角錐相似，所有對應長度比同為 $k$。'),
   'body': '    <p>整個角錐：底 $64\\times64$、高 $24$；$Y$ 高 $18$。</p>\n'
           '    <p>$$k=\\frac{18}{24}=\\frac34$$</p>'},
  {'tag': '第 2 步', 'title': '求 $Y$ 的底邊與 $X$ 的高',
   'body': '    <p>$$Y\\text{ 的底邊}=64\\times\\frac34=48\\text{ cm},\\qquad X\\text{ 的高}=24-18=6\\text{ cm}$$</p>'},
  {'tag': '第 3 步', 'title': '(a) 用體積比 $k^{3}$',
   'rule': ('相似立體的體積比', '$V_Y=k^{3}V_{\\text{總}}$', '相似立體對應長度比 $k$，體積比為 $k^{3}$。'),
   'body': '    <p>$$V_{\\text{總}}=\\frac13(64^{2})(24)=32768\\text{ cm}^{3}$$</p>\n'
           '    <p>$$V_Y=\\left(\\frac34\\right)^{3}(32768)=\\frac{27}{64}\\times32768=13824\\text{ cm}^{3}$$</p>'},
  {'tag': '第 4 步', 'title': '(a) 相減得 $X$ 的體積',
   'body': '    <p>$$V_X=V_{\\text{總}}-V_Y=32768-13824=18944\\text{ cm}^{3}$$</p>'},
  {'tag': '第 5 步', 'title': '(b) 求 $X$ 的斜高與側面面積',
   'rule': ('斜高', '$l=\\sqrt{32^{2}+24^{2}}=40$', '由底面中心到邊中點的距離 $32$、高 $24$ 組成直角三角形。'),
   'body': '    <p>$$l_{\\text{總}}=40\\text{ cm},\\qquad l_Y=40\\times\\frac34=30\\text{ cm}$$</p>\n'
           '    <p>側面（梯形）的高 $=40-30=10\\text{ cm}$</p>\n'
           '    <p>$$\\text{每個側面}=\\frac12(64+48)(10)=560\\text{ cm}^{2}$$</p>'},
  {'tag': '第 6 步', 'title': '(b) 求 $X$ 的總表面積',
   'body': '    <p>$$S_X=4(560)+48^{2}+64^{2}=2240+2304+4096=8640\\text{ cm}^{2}$$</p>'},
  {'tag': '第 7 步', 'title': '(b) 用面積比檢驗相似',
   'rule': ('相似立體的表面積比', '$\\dfrac{S_X}{S_Z}=\\left(\\dfrac{h_X}{h_Z}\\right)^{2}$', '若兩立體相似，總表面積比必須等於對應長度比的平方。'),
   'body': '    <p>$$\\frac{h_X}{h_Z}=\\frac{6}{3}=2 \\quad\\Longrightarrow\\quad \\left(\\frac{h_X}{h_Z}\\right)^{2}=4$$</p>\n'
           '    <p>但 $$\\frac{S_X}{S_Z}=\\frac{8640}{960}=9\\neq4$$</p>\n'
           '    <p>故 $X$ 與 $Z$ <b>不相似</b>。</p>'}],
 'ans': '(a) $18944\\text{ cm}^{3}$　(b) 不相似（表面積比 $9\\neq2^{2}$）',
 'practice': {
  'q': '一個直立角錐底為邊長 $20\\text{ cm}$ 的正方形、高 $18\\text{ cm}$，被平行於底面的平面在高 $12\\text{ cm}$ 處（由頂點量起）切開。求上方小角錐的體積及平截頭體的體積。',
  'steps': [('相似比：', '$k=\\dfrac{12}{18}=\\dfrac23$，上方底邊 $=20\\times\\dfrac23=\\dfrac{40}{3}$。'),
            ('小角錐體積：', '$\\left(\\dfrac23\\right)^{3}\\times\\dfrac13(20^{2})(18)=\\dfrac{8}{27}\\times2400=\\dfrac{6400}{9}$。'),
            ('總體積 $=2400$，平截頭體：', '$2400-\\dfrac{6400}{9}=\\dfrac{15200}{9}\\approx1689\\text{ cm}^{3}$。')],
  'ans': '小角錐 $\\dfrac{6400}{9}\\text{ cm}^{3}$；平截頭體 $\\dfrac{15200}{9}\\text{ cm}^{3}$'}
},
{
 'n': 14,
 'title': 'DSE 2024 卷一 Q14 · 多項式（餘式與因式定理）',
 'tag': 'DSE 2024 · 卷一 · Q14',
 'h1': '常數項定 $p$，兩個定理定 $q$、$r$',
 'sub': '多項式 · 餘式定理 · 無理根 · 7 分題',
 'marks': '7 分',
 'q': '設 $F(x)=\\left(6x^{2}+x+p\\right)\\left(qx^{2}+rx-10\\right)$，其中 $p$、$q$、$r$ 為常數。已知 $F(x)$ 的常數項為 $40$。<br>'
       '(a) 寫出 $p$ 的值。<br>'
       '(b) 當 $F(x)$ 除以 $x+1$ 時，餘式為 $-12$。已知 $x-2$ 是 $F(x)$ 的因式。<br>'
       '(i) 求 $q$ 及 $r$。<br>'
       '(ii) 方程 $F(x)=0$ 有多少個無理根？試解釋。',
 'steps': [
  {'tag': '第 1 步', 'title': '(a) 常數項只看兩個常數項',
   'rule': ('乘積的常數項', '$p\\times(-10)$', '$x$ 的各次項相乘都不會產生常數項。'),
   'body': '    <p>$$-10p=40 \\quad\\Longrightarrow\\quad p=-4$$</p>'},
  {'tag': '第 2 步', 'title': '(b)(i) 用餘式定理',
   'rule': ('餘式定理', '除以 $x+1$ 的餘式 $=F(-1)$', '把 $x=-1$ 代入 $F(x)$。'),
   'body': '    <p>當 $x=-1$，$6x^{2}+x-4=6-1-4=1$，故</p>\n'
           '    <p>$$F(-1)=1\\cdot(q-r-10)=-12 \\quad\\Longrightarrow\\quad q-r=-2 \\quad\\cdots(1)$$</p>'},
  {'tag': '第 3 步', 'title': '(b)(i) 用因式定理',
   'rule': ('因式定理', '$x-2$ 為因式 $\\Leftrightarrow F(2)=0$', '把 $x=2$ 代入，第一個括號為 $24+2-4=22\\neq0$，故第二個括號必須為零。'),
   'body': '    <p>$$22(4q+2r-10)=0 \\quad\\Longrightarrow\\quad 2q+r=5 \\quad\\cdots(2)$$</p>\n'
           '    <p>$(1)+(2)$：$3q=3\\Rightarrow q=1$，代回得 $r=3$。</p>'},
  {'tag': '第 4 步', 'title': '(b)(ii) 寫出 $F(x)$ 的兩個二次因式',
   'body': '    <p>$$F(x)=(6x^{2}+x-4)(x^{2}+3x-10)=(6x^{2}+x-4)(x-2)(x+5)$$</p>\n'
           '    <p>$x-2=0$ 及 $x+5=0$ 給出有理根 $2$ 與 $-5$。</p>'},
  {'tag': '第 5 步', 'title': '(b)(ii) 用判別式判斷 $6x^{2}+x-4=0$',
   'rule': ('判別式非完全平方 $\\Rightarrow$ 無理根', '$\\Delta=97$', '二次方程的根含 $\\sqrt{\\Delta}$；$\\Delta$ 不是完全平方數時，兩根均為無理數。'),
   'body': '    <p>$$x=\\frac{-1\\pm\\sqrt{1^{2}-4(6)(-4)}}{2(6)}=\\frac{-1\\pm\\sqrt{97}}{12}$$</p>\n'
           '    <p>$9^{2}=81<97<100=10^{2}$，$\\sqrt{97}$ 不是整數，故這兩根均為無理數。</p>'},
  {'tag': '第 6 步', 'title': '(b)(ii) 數一數',
   'body': '    <p>四個根為 $2$、$-5$、$\\dfrac{-1+\\sqrt{97}}{12}$、$\\dfrac{-1-\\sqrt{97}}{12}$，其中後兩者為無理數。</p>\n'
           '    <p>所以方程共有 <b>2</b> 個無理根。</p>'}],
 'ans': '(a) $p=-4$　(b)(i) $q=1$，$r=3$　(b)(ii) $2$ 個無理根',
 'practice': {
  'q': '設 $G(x)=\\left(2x^{2}-3x+p\\right)\\left(qx^{2}+rx-4\\right)$，其中 $G(x)$ 的常數項為 $12$。已知 $G(x)$ 除以 $x+1$ 的餘式為 $6$，且 $x-2$ 是 $G(x)$ 的因式。求 $p$、$q$、$r$，並求 $G(x)=0$ 的無理根數目。',
  'steps': [('常數項：', '$-4p=12\\Rightarrow p=-3$。'),
            ('因式定理（$x=2$）：$2(4)-6-3=-1$，', '$-1(4q+2r-4)=0\\Rightarrow2q+r=2$。'),
            ('餘式定理（$x=-1$）：$2+3-3=2$，', '$2(q-r-4)=6\\Rightarrow q-r=7$；解得 $q=3$、$r=-4$。'),
            ('因式分解：', '$G(x)=(2x^{2}-3x-3)(3x^{2}-4x-4)=(2x^{2}-3x-3)(3x+2)(x-2)$。'),
            ('$2x^{2}-3x-3=0$ 的判別式 $=9+24=33$ 不是完全平方，', '故有 $2$ 個無理根。')],
  'ans': '$p=-3$，$q=3$，$r=-4$；共 $2$ 個無理根'}
},
{
 'n': 15,
 'title': 'DSE 2024 卷一 Q15 · 對數與直線',
 'tag': 'DSE 2024 · 卷一 · Q15',
 'h1': '換底，把 $\\log_9$ 變成 $\\log_3$',
 'sub': '指數與對數 · 3 分題',
 'marks': '3 分',
 'q': '已知 $\\log_{9}y$ 是 $\\log_{3}x$ 的線性函數。設該線性函數的圖象為 $L$。$L$ 的斜率為 $4$，且 $L$ 通過點 $(5,22)$。以 $x$ 表示 $y$。',
 'steps': [
  {'tag': '第 1 步', 'title': '寫出直線方程',
   'rule': ('點斜式', '$Y-y_1=m(X-x_1)$', '取 $X=\\log_3x$、$Y=\\log_9y$，斜率 $m=4$，過 $(5,22)$。'),
   'body': '    <p>$$\\log_9y-22=4(\\log_3x-5)$$</p>\n'
           '    <p>$$\\log_9y=4\\log_3x-20+22=4\\log_3x+2$$</p>'},
  {'tag': '第 2 步', 'title': '換底：$\\log_9y=\\dfrac12\\log_3y$',
   'rule': ('換底公式', '$\\log_{a^{k}}y=\\dfrac{1}{k}\\log_ay$', '因為 $9=3^{2}$，以 $9$ 為底的對數是 $3$ 為底的一半。'),
   'body': '    <p>$$\\frac12\\log_3y=4\\log_3x+2 \\quad\\Longrightarrow\\quad \\log_3y=8\\log_3x+4$$</p>'},
  {'tag': '第 3 步', 'title': '化成指數形式',
   'rule': ('對數定律', '$\\log_3y=\\log_3x^{8}+\\log_33^{4}=\\log_3(81x^{8})$', '$n\\log_3x=\\log_3x^{n}$，常數 $4=\\log_33^{4}$。'),
   'body': '    <p>$$y=3^{8\\log_3x+4}=3^{4}\\cdot\\left(3^{\\log_3x}\\right)^{8}=81x^{8}$$</p>'}],
 'ans': '$y=81x^{8}$',
 'practice': {
  'q': '已知 $\\log_{4}y$ 是 $\\log_{2}x$ 的線性函數，其圖象斜率為 $3$ 且通過 $(1,5)$。以 $x$ 表示 $y$。',
  'steps': [('直線：', '$\\log_4y-5=3(\\log_2x-1)\\Rightarrow\\log_4y=3\\log_2x+2$。'),
            ('換底：', '$\\log_4y=\\dfrac12\\log_2y$，故 $\\log_2y=6\\log_2x+4$。'),
            ('指數形式：', '$y=2^{4}x^{6}=16x^{6}$。')],
  'ans': '$y=16x^{6}$'}
},
]
