# -*- coding: utf-8 -*-
# 2018 卷一 Q11–Q15
QUESTIONS = [
{
 'year': '2018', 'paper': '卷一', 'num': 11,
 'h1': '眾數、中位數、平均數：逐個條件迫出 $k$',
 'sub': '統計學 · 集中趨勢',
 'q': r'''下表顯示一些家庭子女數目的分佈：
<table class="dtable">
<tr><th>子女數目</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr>
<tr><th>家庭數目</th><td>$k$</td><td>2</td><td>9</td><td>6</td><td>7</td></tr>
</table>
已知 $k$ 為正整數。
<br>(a) 若該分佈的眾數是 2，寫出 (i) $k$ 的最小可能值；(ii) $k$ 的最大可能值。
<br>(b) 若該分佈的中位數是 2，寫出 (i) $k$ 的最小可能值；(ii) $k$ 的最大可能值。
<br>(c) 若該分佈的平均數是 2，求 $k$。<span class="marks">[6 分]</span>''',
 'steps': [
   ('先算總家庭數', None,
    r'''<p>$$k+2+9+6+7=k+24$$</p>
<p>因為 $k$ 是正整數，$k\ge1$。</p>'''),
   ('(a) 眾數是 2：9 要最大', ('眾數', r'出現次數最多的數值。'),
    r'''<p>「2」的次數是 9；其他最多是 7。要 2 成為眾數，只須 $k\le9$（$k=9$ 時 0 與 2 同時是眾數）。</p>
<p>故 (i) 最小 $k=1$；(ii) 最大 $k=9$。</p>'''),
   ('(b) 中位數是 2：中間位置要落在「2」那一段', ('中位數', r'把數據由小至大排列，取中間的一個（或兩個的平均）。'),
    r'''<p>累積家庭數：$k$、$k+2$、$k+11$、$k+17$、$k+24$。</p>
<p>$k+24$ 是奇數時，中位數是第 $\dfrac{k+25}{2}$ 個。要在「2」的範圍內：</p>
<p>$$k+2<\frac{k+25}{2}\le k+11\;\Longrightarrow\;k<21\ \text{且}\ k\ge3$$</p>
<p>$k$ 為偶數時，中位數是第 $\dfrac{k+24}{2}$ 與 $\dfrac{k+26}{2}$ 個的平均，兩個都要是 2，得 $k\ge4$ 且 $k<20$。</p>
<p>故 (i) 最小 $k=3$（$k=3$ 時第 14 個是 2）；(ii) 最大 $k=19$（$k=20$ 時中位數會變成 $1.5$）。</p>'''),
   ('(c) 平均數是 2', ('平均數', r'$\bar{x}=\dfrac{\sum fx}{\sum f}$。'),
    r'''<p>$$\frac{0(k)+1(2)+2(9)+3(6)+4(7)}{k+24}=2$$</p>
<p>$$\frac{66}{k+24}=2\;\Longrightarrow\;k+24=33\;\Longrightarrow\;k=9$$</p>'''),
 ],
 'ans': r'<b>(a) $1$ 及 $9$　(b) $3$ 及 $19$　(c) $9$</b>',
 'practice': {
   'q': r'''下表顯示某班學生兄弟姐妹數目的分佈：
<table class="dtable">
<tr><th>數目</th><td>0</td><td>1</td><td>2</td><td>3</td></tr>
<tr><th>人數</th><td>4</td><td>$m$</td><td>8</td><td>3</td></tr>
</table>
若平均數是 $1.5$，求 $m$。''',
   'opts': [r'$3$', r'$4$', r'$5$', r'$6$'],
   'steps': [
     r'總和 $=0(4)+1(m)+2(8)+3(3)=m+25$。',
     r'總人數 $=m+15$，$\dfrac{m+25}{m+15}=1.5$。',
     r'$m+25=1.5m+22.5\Rightarrow0.5m=2.5\Rightarrow m=5$。',
   ],
   'ans': r'<b>C</b>（$5$）',
 },
},
{
 'year': '2018', 'paper': '卷一', 'num': 12,
 'h1': '因式定理＋餘式定理：兩個條件解兩個未知數',
 'sub': '多項式 · 因式與餘式定理',
 'q': r'''設 $f(x)=4x(x+1)^{2}+ax+b$，其中 $a$、$b$ 為常數。已知 $x-3$ 是 $f(x)$ 的因式。當 $f(x)$ 除以 $x+2$ 時，餘數是 $2b+165$。
<br>(a) 求 $a$ 及 $b$。
<br>(b) 有人聲稱方程 $f(x)=0$ 至少有一個無理根。你是否同意？試解釋。<span class="marks">[7 分]</span>''',
 'steps': [
   ('(a) 用因式定理：$f(3)=0$', ('因式定理', r'$x-c$ 是因式 $\Leftrightarrow f(c)=0$。'),
    r'''<p>$$4(3)(4)^{2}+3a+b=0\;\Longrightarrow\;192+3a+b=0$$</p>
<p>$$3a+b=-192\quad\cdots(1)$$</p>'''),
   ('(a) 用餘式定理：$f(-2)=2b+165$', ('餘式定理', r'除以 $x+2$ 的餘數是 $f(-2)$。'),
    r'''<p>$$4(-2)(-1)^{2}-2a+b=2b+165$$</p>
<p>$$-8-2a+b=2b+165\;\Longrightarrow\;2a+b=-173\quad\cdots(2)$$</p>'''),
   ('(a) 解聯立方程', None,
    r'''<p>$(1)-(2)$：$a=-19$。</p>
<p>代入 $(1)$：$b=-192+57=-135$。</p>
<p>故 $a=-19$、$b=-135$。</p>'''),
   ('(b) 展開並用 $x-3$ 除', None,
    r'''<p>$$f(x)=4x^{3}+8x^{2}-15x-135=(x-3)(4x^{2}+20x+45)$$</p>'''),
   ('(b) 檢查二次因式的判別式', ('判別式', r'$\Delta=b^{2}-4ac$；$\Delta<0$ 表示無實根。'),
    r'''<p>$$\Delta=20^{2}-4(4)(45)=400-720=-320<0$$</p>
<p>故 $4x^{2}+20x+45=0$ 沒有實根。</p>'''),
   ('(b) 結論', None,
    r'''<p>$f(x)=0$ 唯一的實根是 $x=3$，而 $3$ 是有理數。</p>
<p>因此沒有無理根，<strong>不同意</strong>該聲稱。</p>'''),
 ],
 'ans': r'<b>(a) $a=-19$，$b=-135$　(b) 不同意（只有實根 $x=3$）</b>',
 'practice': {
   'q': r'設 $g(x)=2x^{3}+ax+b$。已知 $x-1$ 是 $g(x)$ 的因式，且 $g(x)$ 除以 $x+1$ 的餘數是 $-12$。求 $a$ 及 $b$。',
   'opts': [r'$a=3$，$b=-5$', r'$a=-3$，$b=5$', r'$a=5$，$b=-3$', r'$a=-5$，$b=3$'],
   'steps': [
     r'$g(1)=2+a+b=0\Rightarrow a+b=-2$。',
     r'$g(-1)=-2-a+b=-12\Rightarrow -a+b=-10$。',
     r'兩式相加：$2b=-12\Rightarrow b=-6$；代回 $a+b=-2$ 得 $a=4$。',
   ],
   'ans': r'<b>A</b>（$a=4$、$b=-6$）',
 },
},
{
 'year': '2018', 'paper': '卷一', 'num': 13,
 'h1': '梯形中的相似三角形：一直用「餘角」找相等角',
 'sub': '平面幾何 · 相似三角形',
 'q': r'''圖 2 中 $ABCD$ 是梯形，$AB\parallel DC$ 且 $\angle ABC=90^{\circ}$。$E$ 是 $BC$ 上的一點，使 $\angle AED=90^{\circ}$。
<br>(a) 證明 $\triangle ABE\sim\triangle ECD$。
<br>(b) 已知 $AB=15\text{ cm}$、$AE=25\text{ cm}$ 及 $CE=36\text{ cm}$。
<br>　(i) 求 $CD$ 的長度。
<br>　(ii) 求 $\triangle ADE$ 的面積。
<br>　(iii) 是否存在 $AD$ 上的一點 $F$，使 $E$ 與 $F$ 的距離小於 $23\text{ cm}$？試解釋。<span class="marks">[8 分]</span>''',
 'fig': r'''<svg viewBox="0 0 400 260" width="400" height="260" role="img" aria-label="梯形 ABCD 與點 E">
 <g fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round">
  <polygon points="60,60 220,60 220,210 340,210"/>
  <line x1="60" y1="60" x2="220" y2="150"/>
  <line x1="220" y1="150" x2="340" y2="210"/>
  <line x1="220" y1="150" x2="220" y2="210" stroke-dasharray="4 3" stroke-width="1.1"/>
 </g>
 <g fill="currentColor" font-family="Georgia,serif" font-style="italic" font-size="15">
  <text x="50" y="54">A</text>
  <text x="226" y="54">B</text>
  <text x="222" y="228">C</text>
  <text x="348" y="228">D</text>
  <text x="228" y="146">E</text>
 </g>
</svg><figcaption>圖：$AB\parallel DC$，$\angle ABC=90^{\circ}$，$E$ 在 $BC$ 上且 $\angle AED=90^{\circ}$</figcaption>''',
 'steps': [
   ('(a) 先證 $\angle ABE=\angle ECD=90^{\circ}$', ('平行線同旁內角', r'$AB\parallel DC\Rightarrow\angle ABC+\angle BCD=180^{\circ}$。'),
    r'''<p>$\angle ABC=90^{\circ}$，故 $\angle BCD=90^{\circ}$，即 $\angle ECD=90^{\circ}=\angle ABE$。</p>'''),
   ('(a) 用餘角證另一對角相等', ('餘角', r'$B$、$E$、$C$ 共線，$\angle AEB+\angle AED+\angle CED=180^{\circ}$。'),
    r'''<p>$$\angle AEB+\angle CED=90^{\circ}$$</p>
<p>在 $\triangle ABE$：$\angle BAE=90^{\circ}-\angle AEB=\angle CED$。</p>
<p>故 $\triangle ABE\sim\triangle ECD$（AAA）。</p>'''),
   ('(b)(i) 先求 $BE$', ('畢氏定理', r'$\triangle ABE$ 在 $B$ 成直角。'),
    r'''<p>$$BE=\sqrt{25^{2}-15^{2}}=\sqrt{625-225}=20\text{ cm}$$</p>'''),
   ('(b)(i) 用相似比求 $CD$', ('對應邊', r'$A\leftrightarrow E$、$B\leftrightarrow C$、$E\leftrightarrow D$。'),
    r'''<p>$$\frac{CD}{BE}=\frac{CE}{AB}\;\Longrightarrow\;\frac{CD}{20}=\frac{36}{15}$$</p>
<p>$$CD=48\text{ cm}$$</p>'''),
   ('(b)(ii) 用兩條直角邊求面積', ('直角三角形面積', r'$\angle AED=90^{\circ}$，故 $AE$、$ED$ 是兩條直角邊。'),
    r'''<p>$$\frac{AE}{ED}=\frac{AB}{EC}=\frac{15}{36}=\frac{5}{12}\;\Longrightarrow\;ED=\frac{12}{5}\times25=60\text{ cm}$$</p>
<p>$$\text{面積}=\frac{1}{2}(25)(60)=750\text{ cm}^{2}$$</p>'''),
   ('(b)(iii) 最短距離是由 $E$ 到 $AD$ 的垂距', ('垂距', r'點到直線的最短距離就是垂直距離。'),
    r'''<p>$$AD=\sqrt{BC^{2}+(CD-AB)^{2}}=\sqrt{56^{2}+33^{2}}=65\text{ cm}$$</p>
<p>設垂距為 $h$：</p>
<p>$$h=\frac{2\times750}{65}=\frac{300}{13}\approx23.08\text{ cm}$$</p>'''),
   ('(b)(iii) 結論', None,
    r'''<p>因為最短距離 $23.08>23$，所以不存在這樣的點 $F$。答案：<strong>不存在</strong>。</p>'''),
 ],
 'ans': r'<b>(a) 見題解　(b)(i) $48\text{ cm}$　(ii) $750\text{ cm}^{2}$　(iii) 不存在</b>',
 'practice': {
   'q': r'梯形 $PQRS$ 中 $PQ\parallel SR$、$\angle PQR=90^{\circ}$，$T$ 在 $QR$ 上使 $\angle PTS=90^{\circ}$。若 $PQ=12\text{ cm}$、$PT=15\text{ cm}$、$TS=20\text{ cm}$，求 $SR$。',
   'opts': [r'$12\text{ cm}$', r'$15\text{ cm}$', r'$18\text{ cm}$', r'$20\text{ cm}$'],
   'steps': [
     r'$QT=\sqrt{15^{2}-12^{2}}=9$。',
     r'$\triangle PQT\sim\triangle TSR$（$P\leftrightarrow T$、$Q\leftrightarrow S$、$T\leftrightarrow R$）。',
     r'$\dfrac{SR}{QT}=\dfrac{TS}{PQ}=\dfrac{20}{12}$，故 $SR=9\times\dfrac{5}{3}=15\text{ cm}$。',
   ],
   'ans': r'<b>B</b>（$15\text{ cm}$）',
 },
},
{
 'year': '2018', 'paper': '卷一', 'num': 14,
 'h1': '圓柱倒水入倒圓錐：體積守恆＋相似三角形',
 'sub': '求積法 · 圓柱與圓錐',
 'q': r'''一個底半徑 $8\text{ cm}$、高 $64\text{ cm}$ 的直立圓柱形容器，與一個底半徑 $20\text{ cm}$、高 $60\text{ cm}$ 的倒立圓錐形容器，均垂直放置。圓柱容器注滿水，然後把水倒入圓錐容器。
<br>(a) 求圓錐容器內水的體積（以 $\pi$ 表示）。
<br>(b) 求圓錐容器內水的深度。
<br>(c) 若把一個半徑 $14\text{ cm}$ 的實心金屬球放入容器，且球完全浸在水中，水會否溢出？試解釋。<span class="marks">[9 分]</span>''',
 'fig': r'''<svg viewBox="0 0 400 240" width="400" height="240" role="img" aria-label="圓柱與倒圓錐">
 <g fill="none" stroke="currentColor" stroke-width="1.5">
  <rect x="40" y="50" width="90" height="150"/>
  <ellipse cx="85" cy="50" rx="45" ry="12"/>
  <path d="M250,60 L330,60 L290,210 Z"/>
  <ellipse cx="290" cy="60" rx="40" ry="11"/>
  <path d="M262,160 L318,160" stroke-dasharray="4 3"/>
 </g>
 <g fill="currentColor" font-family="Georgia,serif" font-size="12">
  <text x="85" y="225" text-anchor="middle">半徑 8、高 64</text>
  <text x="290" y="232" text-anchor="middle">半徑 20、高 60</text>
  <text x="326" y="166">水深 h</text>
 </g>
</svg><figcaption>圖：左為圓柱，右為倒立圓錐（水形成下方的小圓錐）</figcaption>''',
 'steps': [
   ('(a) 圓柱容積就是水的體積', ('圓柱體積', r'$V=\pi r^{2}h$。'),
    r'''<p>$$V=\pi(8)^{2}(64)=4096\pi\text{ cm}^{3}$$</p>'''),
   ('(b) 水深 $h$ 時，水面半徑用相似三角形', ('相似三角形', r'圓錐半徑與深度成正比：$\dfrac{r}{h}=\dfrac{20}{60}=\dfrac{1}{3}$。'),
    r'''<p>$$r=\frac{h}{3}$$</p>'''),
   ('(b) 列方程求 $h$', ('圓錐體積', r'$V=\dfrac{1}{3}\pi r^{2}h$。'),
    r'''<p>$$\frac{1}{3}\pi\left(\frac{h}{3}\right)^{2}h=4096\pi$$</p>
<p>$$\frac{h^{3}}{27}=4096\;\Longrightarrow\;h^{3}=110592\;\Longrightarrow\;h=48\text{ cm}$$</p>'''),
   ('(c) 比較球體積與剩餘空間', ('球體積', r'$V=\dfrac{4}{3}\pi r^{3}$。'),
    r'''<p>整個圓錐：$\dfrac{1}{3}\pi(20)^{2}(60)=8000\pi$。</p>
<p>剩餘空間：$8000\pi-4096\pi=3904\pi$。</p>
<p>球體積：$\dfrac{4}{3}\pi(14)^{3}=\dfrac{10976}{3}\pi\approx3658.7\pi$。</p>'''),
   ('(c) 結論', None,
    r'''<p>因為 $3658.7\pi<3904\pi$，球可以完全浸入而不會令水位超出容器，故<strong>水不會溢出</strong>。</p>'''),
 ],
 'ans': r'<b>(a) $4096\pi\text{ cm}^{3}$　(b) $48\text{ cm}$　(c) 不會溢出</b>',
 'practice': {
   'q': r'一個底半徑 $5\text{ cm}$、高 $40\text{ cm}$ 的圓柱注滿水，倒入底半徑 $15\text{ cm}$、高 $45\text{ cm}$ 的倒立圓錐。求水深。',
   'opts': [r'$24\text{ cm}$', r'$27\text{ cm}$', r'$30\text{ cm}$', r'$36\text{ cm}$'],
   'steps': [
     r'水體積 $=\pi(5)^{2}(40)=1000\pi$。',
     r'水深 $h$ 時水面半徑 $=\dfrac{h}{45}\times15=\dfrac{h}{3}$。',
     r'$\dfrac{1}{3}\pi\left(\dfrac{h}{3}\right)^{2}h=1000\pi\Rightarrow\dfrac{h^{3}}{27}=1000\Rightarrow h=30\text{ cm}$。',
   ],
   'ans': r'<b>C</b>（$30\text{ cm}$）',
 },
},
{
 'year': '2018', 'paper': '卷一', 'num': 15,
 'h1': '排列：先處理有條件的兩個位置',
 'sub': '排列與組合 · 排列',
 'q': r'''一個八位電話號碼由 $2,3,4,5,6,7,8,9$ 這八個數字排列而成。
<br>(a) 可組成多少個不同的八位電話號碼？
<br>(b) 若首個數字與最後一個數字都是奇數，可組成多少個不同的八位電話號碼？<span class="marks">[3 分]</span>''',
 'steps': [
   ('(a) 八個數字全用，求排列數', ('排列', r'$n$ 個不同物件排成 $n$ 個位置，共 $n!$ 種。'),
    r'''<p>$$8!=40\,320$$</p>'''),
   ('(b) 先數奇數字的數目', None,
    r'''<p>奇數有 $3,5,7,9$，共 $4$ 個。</p>'''),
   ('(b) 安排首尾兩個位置', ('有序選取', r'$P_{2}^{4}=4\times3=12$。'),
    r'''<p>$$P_{2}^{4}=12$$</p>'''),
   ('(b) 其餘六個位置任意排', None,
    r'''<p>$$6!=720$$</p>
<p>相乘：$12\times720=8\,640$。</p>'''),
 ],
 'ans': r'<b>(a) $40\,320$　(b) $8\,640$</b>',
 'practice': {
   'q': r'用 $1,2,3,4,5,6$ 六個數字排成六位數（每個數字用一次）。若首尾兩位都是偶數，可組成多少個不同的六位數？',
   'opts': [r'$144$', r'$120$', r'$96$', r'$72$'],
   'steps': [
     r'偶數有 $2,4,6$ 共 3 個，首尾有序選取：$P_{2}^{3}=6$。',
     r'中間四位排列：$4!=24$。',
     r'$6\times24=144$。',
   ],
   'ans': r'<b>A</b>（$144$）',
 },
},
]
