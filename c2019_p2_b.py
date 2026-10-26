# -*- coding: utf-8 -*-
# 2019 卷二 Q9、Q10、Q12–Q19（題目與選項依官方試卷）
QUESTIONS = [
{
 'year': '2019', 'paper': '卷二', 'num': 9,
 'h1': '因式定理：令 $2x+k=0$，代入餘式為零',
 'sub': '多項式 · 因式定理',
 'q': r'''設 $k$ 為常數，且 $2x^{4}+kx^{3}-4x-16$ 可被 $2x+k$ 整除。求 $k$。''',
 'opts': [r'$-2$', r'$2$', r'$4$', r'$8$'],
 'steps': [
   ('把「整除」翻譯成餘式為零', ('因式定理', r'若 $px+q$ 是 $f(x)$ 的因式，則 $f\!\left(-\dfrac{q}{p}\right)=0$。'),
    r'''<p>由 $2x+k=0$ 得 $x=-\dfrac{k}{2}$，所以 $f\!\left(-\dfrac{k}{2}\right)=0$。</p>'''),
   ('代入並逐項化簡', None,
    r'''<p>$$2\left(-\frac{k}{2}\right)^{4}+k\left(-\frac{k}{2}\right)^{3}-4\left(-\frac{k}{2}\right)-16=0$$</p>
<p>$$2\cdot\frac{k^{4}}{16}+k\cdot\left(-\frac{k^{3}}{8}\right)+2k-16=0$$</p>'''),
   ('留意 $k^{4}$ 項互相消去', None,
    r'''<p>$$\frac{k^{4}}{8}-\frac{k^{4}}{8}+2k-16=0$$</p>
<p>四次項剛好對消，只剩一次方程——這是本題的關鍵。</p>'''),
   ('解出 $k$', None,
    r'''<p>$$2k=16\quad\Longrightarrow\quad k=8$$</p>
<p>覆核：$f(-4)=512-512+16-16=0$，確實整除。</p>'''),
 ],
 'ans': r'<b>D</b>（$k=8$）',
 'practice': {
   'q': r'設 $k$ 為常數，且 $2x^{4}+kx^{3}-6x-54$ 可被 $2x+k$ 整除。求 $k$。',
   'opts': [r'$6$', r'$12$', r'$18$', r'$24$'],
   'steps': [
     r'令 $x=-\dfrac{k}{2}$：$2\cdot\dfrac{k^{4}}{16}+k\left(-\dfrac{k^{3}}{8}\right)+3k-54=0$。',
     r'$\dfrac{k^{4}}{8}-\dfrac{k^{4}}{8}+3k-54=0$，四次項對消。',
     r'$3k=54$，故 $k=18$。',
   ],
   'ans': r'<b>C</b>（$k=18$）',
 },
},
{
 'year': '2019', 'paper': '卷二', 'num': 10,
 'h1': '先展開成 $y=-x^{2}+x+12$，再逐句核對',
 'sub': '二次函數 · 圖像特徵',
 'q': r'''下列關於 $y=(3-x)(x+2)+6$ 的圖像的陳述，哪些正確？<br>
I. 圖像開口向下。<br>
II. 圖像通過點 $(1,10)$。<br>
III. 圖像的 $x$ 截距為 $-2$ 及 $3$。''',
 'opts': [r'只有 I', r'只有 II', r'只有 I 及 III', r'只有 II 及 III'],
 'steps': [
   ('展開成標準式', None,
    r'''<p>$$y=(3-x)(x+2)+6=-x^{2}+x+6+6=-x^{2}+x+12$$</p>'''),
   ('判斷 I：開口方向', ('二次函數的開口', r'$x^{2}$ 的係數 $a<0$ 開口向下；$a>0$ 開口向上。'),
    r'''<p>此處 $a=-1<0$，圖像開口向下，I 正確。</p>'''),
   ('判斷 II：代入 $x=1$', None,
    r'''<p>$$y(1)=-1+1+12=12\neq10$$</p>
<p>圖像不通過 $(1,10)$，II 錯誤。</p>'''),
   ('判斷 III：解 $y=0$', ('因式分解', r'$-x^{2}+x+12=0\iff x^{2}-x-12=0$。'),
    r'''<p>$$x^{2}-x-12=(x+3)(x-4)=0\quad\Longrightarrow\quad x=-3\ \text{或}\ 4$$</p>
<p>$x$ 截距是 $-3$ 與 $4$，不是 $-2$ 與 $3$，III 錯誤。</p>'''),
   ('結論', None,
    r'''<p>只有 I 正確，故選 A。易錯：把括號內的 $3$ 與 $-2$ 直接當成截距，忘了先展開常數項。</p>'''),
 ],
 'ans': r'<b>A</b>（只有 I）',
 'practice': {
   'q': r'''下列關於 $y=(2-x)(x+3)+6$ 的圖像的陳述，哪些正確？<br>
I. 圖像開口向下。<br>
II. 圖像通過點 $(1,10)$。<br>
III. 圖像的 $x$ 截距為 $-4$ 及 $3$。''',
   'opts': [r'只有 I', r'只有 II', r'只有 I 及 III', r'I、II 及 III'],
   'steps': [
     r'展開：$y=-x^{2}-x+6+6=-x^{2}-x+12$，$a=-1<0$，I 正確。',
     r'$y(1)=-1-1+12=10$，II 正確。',
     r'$-x^{2}-x+12=0\Rightarrow x^{2}+x-12=0\Rightarrow(x+4)(x-3)=0$，截距 $-4$、$3$，III 正確。',
   ],
   'ans': r'<b>D</b>（I、II 及 III）',
 },
},
{
 'year': '2019', 'paper': '卷二', 'num': 12,
 'h1': '混合均價＝總價除以總重量',
 'sub': '百分數與應用題 · 混合物',
 'q': r'''品牌 $A$ 與品牌 $B$ 的茶葉售價分別為 $\$140/\text{kg}$ 及 $\$315/\text{kg}$。若把 $x\text{ kg}$ 品牌 $A$ 與 $y\text{ kg}$ 品牌 $B$ 混合，使混合茶售價為 $\$210/\text{kg}$，則 $x:y=$''',
 'opts': [r'$2:3$', r'$3:2$', r'$4:9$', r'$9:4$'],
 'steps': [
   ('寫出總價與總重', ('平均價', r'$\text{平均價}=\dfrac{\text{總價}}{\text{總重量}}$，不可把兩個價格直接平均。'),
    r'''<p>總價 $=140x+315y$，總重 $=x+y$。</p>
<p>$$\frac{140x+315y}{x+y}=210$$</p>'''),
   ('去分母並整理', None,
    r'''<p>$$140x+315y=210x+210y$$</p>
<p>$$315y-210y=210x-140x\quad\Longrightarrow\quad 105y=70x$$</p>'''),
   ('化簡比', None,
    r'''<p>$$\frac{x}{y}=\frac{105}{70}=\frac{3}{2}$$</p>
<p>即 $x:y=3:2$。</p>'''),
   ('用一個數字覆核', None,
    r'''<p>取 $x=3,y=2$：總價 $=420+630=1050$，總重 $=5$，平均 $=\$210$ ✓。</p>'''),
 ],
 'ans': r'<b>B</b>（$3:2$）',
 'practice': {
   'q': r'品牌 $A$、$B$ 的售價分別為 $\$120/\text{kg}$ 及 $\$300/\text{kg}$。若把 $x\text{ kg}$ 的 $A$ 與 $y\text{ kg}$ 的 $B$ 混合成售價 $\$200/\text{kg}$ 的混合茶，則 $x:y=$',
   'opts': [r'$4:5$', r'$5:4$', r'$2:3$', r'$3:2$'],
   'steps': [
     r'$\dfrac{120x+300y}{x+y}=200$。',
     r'$120x+300y=200x+200y\Rightarrow100y=80x$。',
     r'$x:y=100:80=5:4$。',
   ],
   'ans': r'<b>B</b>（$5:4$）',
 },
},
{
 'year': '2019', 'paper': '卷二', 'num': 13,
 'h1': '把百分數改寫成乘數，直接比較新舊比值',
 'sub': '變分 · 正變與反變',
 'q': r'''已知 $z$ 隨 $x$ 的平方正變，並隨 $y$ 的平方根反變。若 $x$ 減少 $40\%$，而 $y$ 增加 $44\%$，則 $z$''',
 'opts': [r'減少 $70\%$', r'增加 $70\%$', r'減少 $76\%$', r'增加 $76\%$'],
 'steps': [
   ('寫出變分關係', ('聯合變分', r'$z=\dfrac{kx^{2}}{\sqrt{y}}$，$k$ 為非零常數。'),
    r'''<p>$$z=\frac{kx^{2}}{\sqrt{y}}$$</p>'''),
   ('把「增減百分數」變成乘數', ('百分數乘數', r'減少 $40\%$ 即乘 $0.6$；增加 $44\%$ 即乘 $1.44$。'),
    r'''<p>$$x'=0.6x,\qquad y'=1.44y$$</p>'''),
   ('代入新值，與原式比較', None,
    r'''<p>$$z'=\frac{k(0.6x)^{2}}{\sqrt{1.44y}}=\frac{0.36kx^{2}}{1.2\sqrt{y}}=0.3\cdot\frac{kx^{2}}{\sqrt{y}}=0.3z$$</p>'''),
   ('化成百分數變化', None,
    r'''<p>$$\frac{z'-z}{z}\times100\%=(0.3-1)\times100\%=-70\%$$</p>
<p>即減少 $70\%$，選 A。易錯：把 $40\%$ 與 $44\%$ 直接相減，或忘記平方根要開方。</p>'''),
 ],
 'ans': r'<b>A</b>（減少 $70\%$）',
 'practice': {
   'q': r'已知 $z$ 隨 $x$ 的平方正變，並隨 $y$ 的平方根反變。若 $x$ 增加 $20\%$，而 $y$ 減少 $36\%$，則 $z$',
   'opts': [r'增加 $80\%$', r'減少 $80\%$', r'增加 $44\%$', r'減少 $44\%$'],
   'steps': [
     r'新的 $x$ 乘 $1.2$，新的 $y$ 乘 $0.64$。',
     r'$z=\dfrac{k(1.44x^{2})}{0.8\sqrt{y}}=1.8\times$ 原值。',
     r'$(1.8-1)\times100\%=+80\%$，即增加 $80\%$。',
   ],
   'ans': r'<b>A</b>（增加 $80\%$）',
 },
},
{
 'year': '2019', 'paper': '卷二', 'num': 14,
 'h1': '由「每次加 4」寫出通項，再代 $n=9$',
 'sub': '數列 · 等差數列',
 'q': r'''圖中第 1 個圖案由 6 點組成。對任意正整數 $n$，第 $(n+1)$ 個圖案由第 $n$ 個圖案加上 4 點而成。求第 9 個圖案的點數。''',
 'opts': [r'$30$', r'$34$', r'$38$', r'$42$'],
 'steps': [
   ('寫出首幾項', None,
    r'''<p>第 1 個：$6$；第 2 個：$6+4=10$；第 3 個：$14$……</p>
<p>每次加 $4$，是等差數列，首項 $6$、公差 $4$。</p>'''),
   ('用通項公式', ('等差數列通項', r'$T(n)=a+(n-1)d$。'),
    r'''<p>$$T(n)=6+(n-1)\times4=4n+2$$</p>'''),
   ('代入 $n=9$', None,
    r'''<p>$$T(9)=4(9)+2=38$$</p>'''),
   ('另一種看法：由第 1 個起加了 8 次', None,
    r'''<p>$$6+8\times4=38$$</p>
<p>易錯：誤把「第 9 個」當成加 9 次，得 $42$。</p>'''),
 ],
 'ans': r'<b>C</b>（$38$）',
 'practice': {
   'q': r'某圖案第 1 個由 5 點組成，之後每一個圖案由前一個加上 3 點而成。求第 10 個圖案的點數。',
   'opts': [r'$29$', r'$32$', r'$35$', r'$38$'],
   'steps': [
     r'等差數列，首項 $5$、公差 $3$。',
     r'$T(n)=5+3(n-1)=3n+2$。',
     r'$T(10)=32$。',
   ],
   'ans': r'<b>B</b>（$32$）',
 },
},
{
 'year': '2019', 'paper': '卷二', 'num': 15,
 'h1': '斜高要用「半邊底＋高」求，不是直接用高',
 'sub': '度量 · 稜錐的表面面積',
 'q': r'''一個正四角錐的底是邊長 $18\text{ cm}$ 的正方形。若該角錐的高為 $12\text{ cm}$，則其總表面面積是''',
 'opts': [r'$432\text{ cm}^{2}$', r'$540\text{ cm}^{2}$', r'$756\text{ cm}^{2}$', r'$864\text{ cm}^{2}$'],
 'steps': [
   ('分清「高」與「斜高」', ('斜高', r'側面的三角形以斜高為高；斜高、角錐高、半邊底組成直角三角形。'),
    r'''<p>半邊底 $=9\text{ cm}$，角錐高 $=12\text{ cm}$，斜高 $l$ 滿足</p>
<p>$$l=\sqrt{12^{2}+9^{2}}=15\text{ cm}$$</p>'''),
   ('算底面積', None,
    r'''<p>$$18\times18=324\text{ cm}^{2}$$</p>'''),
   ('算四個側面', ('三角形面積', r'$A=\dfrac{1}{2}\times\text{底}\times\text{高}$，此處的高是斜高。'),
    r'''<p>每個側面 $=\dfrac{1}{2}\times18\times15=135\text{ cm}^{2}$，四個共 $540\text{ cm}^{2}$。</p>'''),
   ('相加', None,
    r'''<p>$$324+540=864\text{ cm}^{2}$$</p>
<p>易錯：用 $12$ 當側面高，會得 $324+432=756$（選項 C 的陷阱）。</p>'''),
 ],
 'ans': r'<b>D</b>（$864\text{ cm}^{2}$）',
 'practice': {
   'q': r'一個正四角錐的底是邊長 $12\text{ cm}$ 的正方形，高為 $8\text{ cm}$。其總表面面積是',
   'opts': [r'$336\text{ cm}^{2}$', r'$384\text{ cm}^{2}$', r'$432\text{ cm}^{2}$', r'$480\text{ cm}^{2}$'],
   'steps': [
     r'斜高 $=\sqrt{8^{2}+6^{2}}=10\text{ cm}$。',
     r'底面積 $=144$；四個側面 $=4\times\dfrac{1}{2}\times12\times10=240$。',
     r'總表面面積 $=384\text{ cm}^{2}$。',
   ],
   'ans': r'<b>B</b>（$384\text{ cm}^{2}$）',
 },
},
{
 'year': '2019', 'paper': '卷二', 'num': 16,
 'h1': '先設比例，再用相似三角形的面積比',
 'sub': '幾何 · 相似三角形與面積',
 'q': r'''圖中 $ABCD$ 為平行四邊形，$AEFG$ 為正方形。已知 $BE:EF:FC=2:7:3$。$BD$ 分別與 $AE$、$FG$ 相交於 $X$、$Y$。若 $\triangle ABX$ 的面積為 $24\text{ cm}^{2}$，則四邊形 $CDYF$ 的面積是''',
 'opts': [r'$54\text{ cm}^{2}$', r'$77\text{ cm}^{2}$', r'$81\text{ cm}^{2}$', r'$87\text{ cm}^{2}$'],
 'fig': r'''<img src="figures/2019_P2_Q16.png" alt="平行四邊形 ABCD 與正方形 AEFG，BD 交 AE 於 X、交 FG 於 Y"><figcaption>圖：$ABCD$ 為平行四邊形，$AEFG$ 為正方形，$BE:EF:FC=2:7:3$</figcaption>''',
 'steps': [
   ('設比例並讀出邊長', ('正方形與平行四邊形', r'正方形四邊相等；平行四邊形對邊相等，故 $AD=BC$。'),
    r'''<p>設 $BE=2k$、$EF=7k$、$FC=3k$。正方形邊長 $=EF=7k$，所以 $AE=7k$。</p>
<p>$$BC=BE+EF+FC=12k\quad\Longrightarrow\quad AD=12k$$</p>'''),
   ('用 $BE\parallel AD$ 找 $EX:AX$', ('相似三角形', r'$BE\parallel AD$，故 $\triangle BEX\sim\triangle DAX$，對應邊成比例。'),
    r'''<p>$$EX:AX=BE:AD=2k:12k=1:6$$</p>
<p>配合 $AE=7k$ 得 $EX=k$、$AX=6k$。</p>'''),
   ('由同高三角形求 $\triangle BEX$', ('同高三角形', r'兩個三角形若高相同，面積比等於底邊比。'),
    r'''<p>$\triangle ABX$ 與 $\triangle BEX$ 同高（由 $B$ 到 $AE$ 的距離），底分別是 $AX=6k$、$EX=k$：</p>
<p>$$\frac{[BEX]}{[ABX]}=\frac{1}{6}\quad\Longrightarrow\quad [BEX]=24\times\frac{1}{6}=4\text{ cm}^{2}$$</p>'''),
   ('再用相似求 $\triangle BFY$', ('面積比＝邊長比的平方', r'相似三角形：$\dfrac{[BEX]}{[BFY]}=\left(\dfrac{EX}{FY}\right)^{2}$。'),
    r'''<p>$BF=BE+EF=9k$，$AD=12k$，由 $\triangle BEX\sim\triangle BFY$ 得</p>
<p>$$EX:FY=BE:BF=2k:9k=2:9$$</p>
<p>$$\frac{4}{[BFY]}=\left(\frac{2}{9}\right)^{2}=\frac{4}{81}\quad\Longrightarrow\quad [BFY]=81\text{ cm}^{2}$$</p>'''),
   ('用平行四邊形面積作差', None,
    r'''<p>由 $[ABX]=6k^{2}=24$ 得 $k=2$，平行四邊形面積 $=AD\times AE=12k\times7k=84k^{2}=336$。</p>
<p>對角線 $BD$ 把平行四邊形平分：$[BCD]=168$。</p>
<p>$$[CDYF]=[BCD]-[BFY]=168-81=87\text{ cm}^{2}$$</p>'''),
 ],
 'ans': r'<b>D</b>（$87\text{ cm}^{2}$）',
 'practice': {
   'q': r'圖中 $DE\parallel BC$，$AD:DB=1:2$。若 $\triangle ADE$ 的面積為 $5\text{ cm}^{2}$，則 $\triangle ABC$ 的面積是',
   'opts': [r'$15\text{ cm}^{2}$', r'$20\text{ cm}^{2}$', r'$45\text{ cm}^{2}$', r'$60\text{ cm}^{2}$'],
   'steps': [
     r'$AD:AB=1:3$。',
     r'$\triangle ADE\sim\triangle ABC$，面積比 $=1^{2}:3^{2}=1:9$。',
     r'$[ABC]=5\times9=45\text{ cm}^{2}$。',
   ],
   'ans': r'<b>C</b>（$45\text{ cm}^{2}$）',
 },
},
{
 'year': '2019', 'paper': '卷二', 'num': 17,
 'h1': '設一個未知角，把等腰與外角串起來',
 'sub': '幾何 · 等腰三角形與外角',
 'q': r'''圖中 $ABC$ 與 $ADE$ 均為直線。已知 $AB=BD$ 且 $BC=CD$。若 $\angle CDE=66^{\circ}$，則 $\angle ACD=$''',
 'opts': [r'$28^{\circ}$', r'$33^{\circ}$', r'$36^{\circ}$', r'$38^{\circ}$'],
 'fig': r'''<img src="figures/2019_P2_Q17.png" alt="三角形 ABC，D 在 AC 延線上，AB=BD、BC=CD，∠CDE=66°"><figcaption>圖：$ABC$、$ADE$ 為直線，$AB=BD$，$BC=CD$，$\angle CDE=66^{\circ}$</figcaption>''',
 'steps': [
   ('在等腰 $\triangle ABD$ 設未知角', ('等腰三角形底角相等', r'$AB=BD\Rightarrow\angle BAD=\angle BDA$。'),
    r'''<p>設 $\angle BAD=\angle BDA=x$。</p>'''),
   ('用外角求 $\angle CBD$', ('三角形的外角', r'外角等於兩個內對角之和。'),
    r'''<p>$\angle CBD$ 是 $\triangle ABD$ 在 $B$ 的外角：</p>
<p>$$\angle CBD=\angle BAD+\angle BDA=2x$$</p>'''),
   ('在等腰 $\triangle BCD$ 得 $\angle CDB$', ('等腰三角形', r'$BC=CD\Rightarrow\angle CBD=\angle CDB=2x$。'),
    r'''<p>$$\angle CDB=2x$$</p>'''),
   ('用直線上的角解 $x$', ('直線上的鄰角', r'$A$、$D$、$E$ 共線，$\angle BDA+\angle CDB+\angle CDE=180^{\circ}$。'),
    r'''<p>$$x+2x+66^{\circ}=180^{\circ}\quad\Longrightarrow\quad x=38^{\circ}$$</p>'''),
   ('最後用外角求 $\angle ACD$', ('外角', r'$\angle CDE$ 是 $\triangle ACD$ 在 $D$ 的外角：$\angle CAD+\angle ACD=\angle CDE$。'),
    r'''<p>$$38^{\circ}+\angle ACD=66^{\circ}\quad\Longrightarrow\quad \angle ACD=28^{\circ}$$</p>'''),
 ],
 'ans': r'<b>A</b>（$28^{\circ}$）',
 'practice': {
   'q': r'圖中 $ABC$、$ADE$ 為直線，$AB=BD$，$BC=CD$。若 $\angle CDE=72^{\circ}$，則 $\angle ACD=$',
   'opts': [r'$24^{\circ}$', r'$30^{\circ}$', r'$36^{\circ}$', r'$42^{\circ}$'],
   'steps': [
     r'設 $\angle BAD=\angle BDA=x$，則 $\angle CBD=\angle CDB=2x$。',
     r'$x+2x+72^{\circ}=180^{\circ}\Rightarrow x=36^{\circ}$。',
     r'$\angle ACD=72^{\circ}-36^{\circ}=36^{\circ}$。',
   ],
   'ans': r'<b>C</b>（$36^{\circ}$）',
 },
},
{
 'year': '2019', 'paper': '卷二', 'num': 18,
 'h1': '先證 $\angle AEC=90^{\circ}$，再用直角三角形斜邊中點',
 'sub': '幾何 · 相似、畢氏定理與中點定理',
 'q': r'''圖中 $ABC$ 為等腰三角形，$AB=AC$。$D$、$E$ 為 $AB$ 上的點，使 $AD=DE=2EB$；$F$ 為 $AC$ 上的點，使 $DF\parallel EC$。若 $\angle ADF=90^{\circ}$ 且 $CE=60\text{ cm}$，則 $EF=$''',
 'opts': [r'$40\text{ cm}$', r'$45\text{ cm}$', r'$48\text{ cm}$', r'$50\text{ cm}$'],
 'fig': r'''<img src="figures/2019_P2_Q18.png" alt="等腰三角形 ABC，D、E 在 AB 上，F 在 AC 上，DF∥EC"><figcaption>圖：$AB=AC$，$AD=DE=2EB$，$DF\parallel EC$，$\angle ADF=90^{\circ}$，$CE=60\text{ cm}$</figcaption>''',
 'steps': [
   ('設 $EB=x$，把各段寫成 $x$', None,
    r'''<p>$$EB=x,\quad AD=DE=2x,\quad AE=4x,\quad AB=AD+DE+EB=5x$$</p>
<p>因 $AB=AC$，故 $AC=5x$。</p>'''),
   ('由平行線得直角', ('同位角', r'$DF\parallel EC$，$AD$ 為截線，同位角相等。'),
    r'''<p>$$\angle AEC=\angle ADF=90^{\circ}$$</p>'''),
   ('在 $\triangle AEC$ 用畢氏定理求 $x$', ('畢氏定理', r'$AE^{2}+EC^{2}=AC^{2}$。'),
    r'''<p>$$(4x)^{2}+60^{2}=(5x)^{2}$$</p>
<p>$$16x^{2}+3600=25x^{2}\quad\Longrightarrow\quad x^{2}=400,\ x=20$$</p>'''),
   ('用中點定理定位 $F$', ('中點定理', r'在 $\triangle AEC$ 中，$D$ 為 $AE$ 中點且 $DF\parallel EC$，故 $F$ 為 $AC$ 中點。'),
    r'''<p>$$AF=FC=\frac{AC}{2}=\frac{100}{2}=50\text{ cm}$$</p>'''),
   ('直角三角形斜邊中點到三頂點等距', ('斜邊中點性質', r'$\angle AEC=90^{\circ}$，$F$ 為斜邊 $AC$ 的中點，則 $FA=FE=FC$。'),
    r'''<p>$$EF=FA=50\text{ cm}$$</p>
<p>易錯：只算出 $AF=50$ 便停手；要再利用直角三角形的斜邊中點性質，才知 $EF$ 同樣是 $50$。</p>'''),
 ],
 'ans': r'<b>D</b>（$50\text{ cm}$）',
 'practice': {
   'q': r'圖中 $ABC$ 為等腰三角形，$AB=AC$。$AD=DE=2EB$，$DF\parallel EC$，$\angle ADF=90^{\circ}$，$CE=48\text{ cm}$。則 $EF=$',
   'opts': [r'$32\text{ cm}$', r'$40\text{ cm}$', r'$45\text{ cm}$', r'$50\text{ cm}$'],
   'steps': [
     r'$AE=4x$，$AC=5x$，$\angle AEC=90^{\circ}$。',
     r'$16x^{2}+48^{2}=25x^{2}\Rightarrow x^{2}=256\Rightarrow x=16$，$AC=80$。',
     r'$F$ 為 $AC$ 中點，$EF=FA=\dfrac{80}{2}=40\text{ cm}$。',
   ],
   'ans': r'<b>B</b>（$40\text{ cm}$）',
 },
},
{
 'year': '2019', 'paper': '卷二', 'num': 19,
 'h1': '補上高 $BD$，把梯形拆成兩個直角三角形',
 'sub': '度量 · 梯形面積',
 'q': r'''圖中 $ABCD$ 為梯形，$AB\parallel DC$ 且 $\angle ABD=90^{\circ}$。若 $AB=18\text{ cm}$、$BC=26\text{ cm}$ 及 $AD=30\text{ cm}$，求梯形 $ABCD$ 的面積。''',
 'opts': [r'$336\text{ cm}^{2}$', r'$400\text{ cm}^{2}$', r'$504\text{ cm}^{2}$', r'$552\text{ cm}^{2}$'],
 'fig': r'''<img src="figures/2019_P2_Q19.png" alt="梯形 ABCD，AB∥DC，∠ABD=90°，AB=18，BC=26，AD=30"><figcaption>圖：$AB\parallel DC$，$\angle ABD=90^{\circ}$，$AB=18\text{ cm}$，$BC=26\text{ cm}$，$AD=30\text{ cm}$</figcaption>''',
 'steps': [
   ('在 $\triangle ABD$ 求 $BD$', ('畢氏定理', r'$\angle ABD=90^{\circ}$，$AD$ 是斜邊。'),
    r'''<p>$$18^{2}+BD^{2}=30^{2}\quad\Longrightarrow\quad BD=\sqrt{900-324}=24\text{ cm}$$</p>'''),
   ('用平行線找 $\angle CDB$', ('內錯角', r'$AB\parallel DC$，$BD$ 為截線，$\angle CDB=\angle ABD=90^{\circ}$。'),
    r'''<p>所以 $\triangle BCD$ 在 $D$ 為直角。</p>'''),
   ('在 $\triangle BCD$ 求 $DC$', ('畢氏定理', r'$DC^{2}+BD^{2}=BC^{2}$。'),
    r'''<p>$$DC^{2}+24^{2}=26^{2}\quad\Longrightarrow\quad DC=10\text{ cm}$$</p>'''),
   ('把梯形拆成兩個三角形', None,
    r'''<p>$BD$ 把梯形分成 $\triangle ABD$ 與 $\triangle BCD$：</p>
<p>$$\frac{1}{2}\times18\times24+\frac{1}{2}\times10\times24=216+120=336\text{ cm}^{2}$$</p>'''),
   ('或用梯形公式覆核', ('梯形面積', r'$A=\dfrac{1}{2}(a+b)h$，兩平行邊為 $AB=18$、$DC=10$，高為 $BD=24$。'),
    r'''<p>$$\frac{1}{2}(18+10)\times24=336\text{ cm}^{2}$$</p>'''),
 ],
 'ans': r'<b>A</b>（$336\text{ cm}^{2}$）',
 'practice': {
   'q': r'梯形 $ABCD$ 中 $AB\parallel DC$，$\angle ABD=90^{\circ}$，$AB=12\text{ cm}$，$AD=20\text{ cm}$，$BC=20\text{ cm}$。其面積是',
   'opts': [r'$156\text{ cm}^{2}$', r'$192\text{ cm}^{2}$', r'$210\text{ cm}^{2}$', r'$240\text{ cm}^{2}$'],
   'steps': [
     r'$BD=\sqrt{20^{2}-12^{2}}=16\text{ cm}$。',
     r'$DC=\sqrt{20^{2}-16^{2}}=12\text{ cm}$。',
     r'面積 $=\dfrac{1}{2}(12+12)\times16=192\text{ cm}^{2}$。',
   ],
   'ans': r'<b>B</b>（$192\text{ cm}^{2}$）',
 },
},
]
