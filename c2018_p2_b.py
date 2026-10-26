# -*- coding: utf-8 -*-
# 2018 卷二 Q9–Q16
QUESTIONS = [
{
 'year': '2018', 'paper': '卷二', 'num': 9,
 'h1': '複利息：月利率與期數要配套',
 'sub': '百分數 · 複利息',
 'q': r'''把 $\$100\,000$ 存入銀行，年利率 $2\%$，為期 $3$ 年，每月複利計算。求利息（準確至最接近的元）。''',
 'opts': [r'$\$6\,000$', r'$\$6\,121$', r'$\$6\,176$', r'$\$6\,178$'],
 'steps': [
   ('抄下三個數量', ('複利息', r'$A=P\left(1+\dfrac{r}{n}\right)^{nt}$，其中 $r$ 是年利率、$n$ 是每年複利次數。'),
    r'''<p>本金 $P=100\,000$，年利率 $r=2\%=0.02$，$t=3$ 年，每月複利即 $n=12$。</p>'''),
   ('每月利率＝年利率 ÷ 12', ('易錯點', r'「每月複利」是每年計 12 次，不是每月 $2\%$。'),
    r'''<p>$$\text{每月利率}=\frac{0.02}{12}=\frac{1}{600}\approx0.1667\%$$</p>'''),
   ('期數＝每年次數 × 年數', None,
    r'''<p>$$nt=12\times3=36\ \text{期}$$</p>'''),
   ('代入求本利和，再減本金', None,
    r'''<p>$$A=100\,000\left(1+\frac{0.02}{12}\right)^{36}\approx106\,178.35$$</p>
<p>$$\text{利息}=A-P\approx106\,178.35-100\,000=6\,178.35$$</p>
<p>準確至最接近的元為 $\$6\,178$。</p>'''),
 ],
 'ans': r'<b>D</b>（$\$6\,178$）',
 'practice': {
   'q': r'把 $\$50\,000$ 存入銀行，年利率 $3\%$，為期 $2$ 年，每季複利計算。求利息（準確至最接近的元）。',
   'opts': [r'$\$3\,000$', r'$\$3\,075$', r'$\$3\,080$', r'$\$3\,120$'],
   'steps': [
     r'每季利率 $=\dfrac{0.03}{4}=0.0075$，期數 $=4\times2=8$。',
     r'$A=50\,000(1.0075)^{8}\approx53\,079.94$。',
     r'利息 $\approx3\,079.94\approx\$3\,080$。',
   ],
   'ans': r'<b>C</b>（$\$3\,080$）',
 },
},
{
 'year': '2018', 'paper': '卷二', 'num': 10,
 'h1': '兩個比併成三項比，再代入求值',
 'sub': '比與比例 · 比的運算',
 'q': r'''設 $a$、$b$、$c$ 為非零數。若 $3a=4b$ 且 $a:c=2:5$，則 $\dfrac{a+3b}{b+3c}=$''',
 'opts': [r'$\dfrac{5}{3}$', r'$\dfrac{13}{33}$', r'$\dfrac{30}{53}$', r'$\dfrac{75}{38}$'],
 'steps': [
   ('由 $3a=4b$ 寫出 $a:b$', ('比的性质', r'$3a=4b\Rightarrow \dfrac{a}{b}=\dfrac{4}{3}$。'),
    r'''<p>$$a:b=4:3$$</p>'''),
   ('$a$ 的部分要對齊', None,
    r'''<p>$a:b=4:3$，而 $a:c=2:5$。把 $a$ 的部分同乘 2：$a:c=4:10$。</p>
<p>$$a:b:c=4:3:10$$</p>'''),
   ('設 $a=4k$、$b=3k$、$c=10k$', None,
    r'''<p>$k$ 會在約分時消去，可設 $k\neq0$。</p>'''),
   ('代入目標分式', None,
    r'''<p>$$\frac{a+3b}{b+3c}=\frac{4k+9k}{3k+30k}=\frac{13k}{33k}=\frac{13}{33}$$</p>'''),
 ],
 'ans': r'<b>B</b>（$\dfrac{13}{33}$）',
 'practice': {
   'q': r'設 $p$、$q$、$r$ 為非零數。若 $2p=5q$ 且 $p:r=3:4$，則 $\dfrac{p+2q}{q+2r}=$',
   'opts': [r'$\dfrac{27}{46}$', r'$\dfrac{13}{23}$', r'$\dfrac{9}{16}$', r'$\dfrac{46}{27}$'],
   'steps': [
     r'$2p=5q\Rightarrow p:q=5:2$；$p:r=3:4$。',
     r'把 $p$ 對齊（LCM 15）：$p:q=15:6$，$p:r=15:20$，故 $p:q:r=15:6:20$。',
     r'$\dfrac{p+2q}{q+2r}=\dfrac{15+12}{6+40}=\dfrac{27}{46}$。',
   ],
   'ans': r'<b>A</b>（$\dfrac{27}{46}$）',
 },
},
{
 'year': '2018', 'paper': '卷二', 'num': 11,
 'h1': '正變與反變：先寫方程，再平方找常數',
 'sub': '變分 · 正變與反變',
 'q': r'''若 $w$ 隨 $u$ 的平方根正變，並隨 $v$ 的平方反變，則下列何者必定是常數？''',
 'opts': [r'$u^{4}vw^{2}$', r'$uv^{4}w^{2}$', r'$\dfrac{vw^{2}}{u^{4}}$', r'$\dfrac{v^{4}w^{2}}{u}$'],
 'steps': [
   ('把文字譯成方程', ('變分', r'正變放分子，反變放分母。'),
    r'''<p>$w$ 隨 $\sqrt{u}$ 正變、隨 $v^{2}$ 反變：</p>
<p>$$w=k\,\frac{\sqrt{u}}{v^{2}}\qquad(k\neq0\ \text{為常數})$$</p>'''),
   ('把 $k$ 單獨留在左邊', None,
    r'''<p>兩邊乘 $\dfrac{v^{2}}{\sqrt{u}}$：</p>
<p>$$k=\frac{wv^{2}}{\sqrt{u}}$$</p>'''),
   ('平方，消去根號', None,
    r'''<p>$$k^{2}=\frac{w^{2}v^{4}}{u}$$</p>
<p>$k$ 是常數，$k^{2}$ 也是常數，故 $\dfrac{v^{4}w^{2}}{u}$ 必定是常數。</p>'''),
 ],
 'ans': r'<b>D</b>（$\dfrac{v^{4}w^{2}}{u}$）',
 'practice': {
   'q': r'若 $y$ 隨 $x$ 的立方正變，並隨 $\sqrt{z}$ 反變，則下列何者必定是常數？',
   'opts': [r'$\dfrac{x^{6}}{y^{2}z}$', r'$\dfrac{y^{2}z}{x^{6}}$', r'$\dfrac{yz^{2}}{x^{3}}$', r'$\dfrac{x^{3}z}{y^{2}}$'],
   'steps': [
     r'$y=k\dfrac{x^{3}}{\sqrt{z}}$。',
     r'$k=\dfrac{y\sqrt{z}}{x^{3}}$。',
     r'平方：$k^{2}=\dfrac{y^{2}z}{x^{6}}$。',
   ],
   'ans': r'<b>B</b>（$\dfrac{y^{2}z}{x^{6}}$）',
 },
},
{
 'year': '2018', 'paper': '卷二', 'num': 12,
 'h1': '遞推數列：由後向前倒推',
 'sub': '數列 · 遞推關係',
 'q': r'''設 $a_{n}$ 為某數列的第 $n$ 項。若 $a_{3}=21$、$a_{6}=89$，且對任意正整數 $n$ 都有 $a_{n+2}=a_{n}+a_{n+1}$，則 $a_{1}=$''',
 'opts': [r'$8$', r'$13$', r'$34$', r'$55$'],
 'steps': [
   ('先求中間的 $a_{4}$', ('遞推關係', r'$a_{n+2}=a_{n}+a_{n+1}$；反過來用 $a_{n}=a_{n+2}-a_{n+1}$。'),
    r'''<p>用兩次關係：</p>
<p>$$a_{6}=a_{4}+a_{5},\qquad a_{5}=a_{3}+a_{4}$$</p>
<p>把第二式代入第一式：</p>
<p>$$89=a_{4}+(21+a_{4})=21+2a_{4}\;\Rightarrow\;a_{4}=34$$</p>'''),
   ('求 $a_{5}$、$a_{2}$', None,
    r'''<p>$$a_{5}=a_{3}+a_{4}=21+34=55$$</p>
<p>$$a_{4}=a_{2}+a_{3}\;\Rightarrow\;a_{2}=34-21=13$$</p>'''),
   ('再退一步求 $a_{1}$', None,
    r'''<p>$$a_{3}=a_{1}+a_{2}\;\Rightarrow\;a_{1}=21-13=8$$</p>'''),
 ],
 'ans': r'<b>A</b>（$8$）',
 'practice': {
   'q': r'設 $b_{n}$ 為某數列的第 $n$ 項。若 $b_{3}=9$、$b_{6}=31$，且 $b_{n+2}=b_{n}+b_{n+1}$，則 $b_{1}=$',
   'opts': [r'$5$', r'$7$', r'$9$', r'$11$'],
   'steps': [
     r'$b_{6}=b_{3}+2b_{4}\Rightarrow31=9+2b_{4}\Rightarrow b_{4}=11$。',
     r'$b_{5}=b_{3}+b_{4}=20$；$b_{2}=b_{4}-b_{3}=2$。',
     r'$b_{1}=b_{3}-b_{2}=9-2=7$。',
   ],
   'ans': r'<b>B</b>（$7$）',
 },
},
{
 'year': '2018', 'paper': '卷二', 'num': 13,
 'h1': '「or」＝取聯集，兩條不等式各自解',
 'sub': '不等式 · 複合不等式',
 'q': r'''不等式 $\dfrac{1-2x}{3}\ge x-3$ 或 $4x+9<1$ 的解是''',
 'opts': [r'$x\ge2$', r'$x<-2$', r'$x\le2$', r'所有實數 $x$'],
 'steps': [
   ('先分清「or」的意思', ('聯集', r'符合其中一條即可，所以解集是兩個解集的<strong>聯集</strong>。'),
    r'''<p>分別解兩條不等式，最後取聯集（覆蓋的範圍合起來）。</p>'''),
   ('解第一條：兩邊乘 3', ('不等式的性質', r'乘正數，不等號方向不變；乘負數才反向。'),
    r'''<p>$$\frac{1-2x}{3}\ge x-3\;\Longrightarrow\;1-2x\ge3x-9$$</p>
<p>$$-5x\ge-10$$</p>
<p>兩邊除以 $-5$（負數，不等號反向）：</p>
<p>$$x\le2$$</p>'''),
   ('解第二條', None,
    r'''<p>$$4x+9<1\;\Longrightarrow\;4x<-8\;\Longrightarrow\;x<-2$$</p>'''),
   ('取聯集', None,
    r'''<p>$x<-2$ 的每一個值都滿足 $x\le2$，所以聯集就是 $x\le2$。</p>
<p>（可用數線檢查：兩段合起來剛好是由 $2$ 向左的全部。）</p>'''),
 ],
 'ans': r'<b>C</b>（$x\le2$）',
 'practice': {
   'q': r'不等式 $\dfrac{2-x}{3}\ge1$ 或 $3x-5<4$ 的解是',
   'opts': [r'$x\le-1$', r'$x<3$', r'$x>3$', r'所有實數 $x$'],
   'steps': [
     r'第一條：$2-x\ge3\Rightarrow x\le-1$。',
     r'第二條：$3x<9\Rightarrow x<3$。',
     r'取聯集：$x\le-1$ 已包含在 $x<3$ 之內，故解為 $x<3$。',
   ],
   'ans': r'<b>B</b>（$x<3$）',
 },
},
{
 'year': '2018', 'paper': '卷二', 'num': 14,
 'h1': '量度誤差：面積取極端值才找到範圍',
 'sub': '估算與誤差 · 面積的誤差',
 'q': r'''圖中 $ABCDEFGH$ 是一個八邊形，所有量度均準確至最接近的 cm。設 $x\text{ cm}^{2}$ 為該八邊形的實際面積，求 $x$ 的範圍。''',
 'opts': [r'$13<x<23$', r'$13<x<27$', r'$17<x<23$', r'$17<x<27$'],
 'fig': r'''<svg viewBox="0 0 420 262" width="420" height="262" role="img" aria-label="八邊形 ABCDEFGH">
  <g fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round">
    <path d="M60,50 L180,50 L180,90 L240,90 L240,50 L360,50 L360,210 L60,210 Z"/>
  </g>
  <g fill="currentColor" font-family="Georgia,serif" font-style="italic" font-size="15">
    <text x="52" y="42" text-anchor="end">A</text>
    <text x="180" y="42" text-anchor="middle">H</text>
    <text x="240" y="42" text-anchor="middle">E</text>
    <text x="368" y="42">D</text>
    <text x="368" y="214">C</text>
    <text x="52" y="214" text-anchor="end">B</text>
    <text x="172" y="106" text-anchor="end">G</text>
    <text x="248" y="106">F</text>
  </g>
  <g fill="currentColor" font-family="Georgia,serif" font-size="13">
    <text x="210" y="228" text-anchor="middle">6 cm</text>
    <text x="210" y="84" text-anchor="middle">2 cm</text>
    <text x="172" y="76" text-anchor="end">2 cm</text>
    <text x="50" y="134" text-anchor="middle" transform="rotate(-90 50 134)">4 cm</text>
  </g>
</svg><figcaption>圖：外框 $6\text{ cm}\times4\text{ cm}$，上方挖去 $2\text{ cm}\times2\text{ cm}$ 的缺口</figcaption>''',
 'steps': [
   ('把面積寫成「大長方形 − 缺口」', ('分割法', r'互不重疊的部分可以直接加減。'),
    r'''<p>名義面積：</p>
<p>$$6\times4-2\times2=24-4=20\text{ cm}^{2}$$</p>'''),
   ('每個量度都有一個範圍', ('量度誤差', r'準確至最接近的 cm $\Rightarrow$ 實際長度 $L$ 滿足 $L-0.5<$ 實際 $<L+0.5$。'),
    r'''<p>例如 $6\text{ cm}$ 的實際值介乎 $5.5$ 與 $6.5$ 之間。</p>'''),
   ('面積最小：大長方形取最小、缺口取最大', None,
    r'''<p>$$(6-0.5)(4-0.5)-(2+0.5)(2+0.5)=5.5\times3.5-2.5\times2.5$$</p>
<p>$$=19.25-6.25=13$$</p>'''),
   ('面積最大：大長方形取最大、缺口取最小', None,
    r'''<p>$$(6+0.5)(4+0.5)-(2-0.5)(2-0.5)=6.5\times4.5-1.5\times1.5$$</p>
<p>$$=29.25-2.25=27$$</p>
<p>實際面積嚴格介乎兩者之間，故 $13<x<27$。</p>'''),
 ],
 'ans': r'<b>B</b>（$13<x<27$）',
 'practice': {
   'q': r'一個長方形長 $8\text{ cm}$、闊 $5\text{ cm}$，量度均準確至最接近的 cm。設 $A\text{ cm}^{2}$ 為實際面積，求 $A$ 的範圍。',
   'opts': [r'$35<A<45$', r'$33.75<A<46.75$', r'$37.5<A<42.5$', r'$39<A<41$'],
   'steps': [
     r'最小：$7.5\times4.5=33.75$。',
     r'最大：$8.5\times5.5=46.75$。',
     r'故 $33.75<A<46.75$。',
   ],
   'ans': r'<b>B</b>（$33.75<A<46.75$）',
 },
},
{
 'year': '2018', 'paper': '卷二', 'num': 15,
 'h1': '柱體體積：先補回截面的第三條邊',
 'sub': '求積法 · 柱體體積',
 'q': r'''圖中直角三角柱的體積是''',
 'opts': [r'$544\text{ cm}^{3}$', r'$600\text{ cm}^{3}$', r'$660\text{ cm}^{3}$', r'$720\text{ cm}^{3}$'],
 'fig': r'''<img src="figures/2018_P2_15.png" alt="直角三角柱" style="max-width:100%;height:auto;"><figcaption>圖：橫截面為直角三角形，斜邊 $17\text{ cm}$、一條直角邊 $8\text{ cm}$，柱長 $12\text{ cm}$</figcaption>''',
 'steps': [
   ('認清「橫截面 × 長度」', ('柱體體積', r'$V=$ 橫截面面積 $\times$ 柱長。'),
    r'''<p>橫截面是直角三角形，柱長 $=12\text{ cm}$。</p>'''),
   ('用畢氏定理求第三條邊', None,
    r'''<p>$$\text{另一條直角邊}=\sqrt{17^{2}-8^{2}}=\sqrt{289-64}=15\text{ cm}$$</p>'''),
   ('求橫截面面積', None,
    r'''<p>$$A=\frac{1}{2}\times15\times8=60\text{ cm}^{2}$$</p>'''),
   ('乘柱長', None,
    r'''<p>$$V=60\times12=720\text{ cm}^{3}$$</p>'''),
 ],
 'ans': r'<b>D</b>（$720\text{ cm}^{3}$）',
 'practice': {
   'q': r'一個直角三角柱的橫截面是直角三角形，兩條直角邊分別為 $6\text{ cm}$ 及 $8\text{ cm}$，柱長 $10\text{ cm}$。求體積。',
   'opts': [r'$240\text{ cm}^{3}$', r'$480\text{ cm}^{3}$', r'$120\text{ cm}^{3}$', r'$300\text{ cm}^{3}$'],
   'steps': [
     r'橫截面面積 $=\dfrac{1}{2}\times6\times8=24$。',
     r'$V=24\times10$。',
     r'$=240\text{ cm}^{3}$。',
   ],
   'ans': r'<b>A</b>（$240\text{ cm}^{3}$）',
 },
},
{
 'year': '2018', 'paper': '卷二', 'num': 16,
 'h1': '平行四邊形內的面積：先找相似三角形',
 'sub': '求積法 · 三角形與四邊形的面積',
 'q': r'''圖中 $ABCD$ 是平行四邊形。$E$ 是 $BC$ 上的一點，使 $BE:EC=5:3$。$AE$ 與 $BD$ 相交於 $F$。若 $\triangle ABF$ 的面積為 $120\text{ cm}^{2}$，則四邊形 $CDFE$ 的面積是''',
 'opts': [r'$237\text{ cm}^{2}$', r'$307\text{ cm}^{2}$', r'$312\text{ cm}^{2}$', r'$429\text{ cm}^{2}$'],
 'fig': r'''<img src="figures/2018_P2_16.png" alt="平行四邊形 ABCD 與點 E、F" style="max-width:100%;height:auto;"><figcaption>圖：$BE:EC=5:3$，$AE$ 與 $BD$ 交於 $F$</figcaption>''',
 'steps': [
   ('用相似三角形定出 $BF:FD$', ('相似三角形', r'$AD\parallel BC\Rightarrow\angle EBF=\angle ADF$（內錯角）。'),
    r'''<p>$\triangle EBF\sim\triangle ADF$（AAA），且 $AD=BC$，故</p>
<p>$$\frac{BF}{FD}=\frac{BE}{AD}=\frac{BE}{BC}=\frac{5}{5+3}=\frac{5}{8}$$</p>'''),
   ('用 $\triangle ABF$ 反推整個平行四邊形面積', ('同高三角形', r'底在同一條線 $BD$ 上時，面積比＝底邊比。'),
    r'''<p>$\triangle ABD$ 中，$F$ 在 $BD$ 上，故</p>
<p>$$\frac{\triangle ABF}{\triangle ABD}=\frac{BF}{BD}=\frac{5}{13}$$</p>
<p>而 $\triangle ABD=\dfrac{1}{2}\times$ 平行四邊形面積 $S$，所以</p>
<p>$$120=\frac{5}{13}\times\frac{S}{2}\;\Rightarrow\;S=624$$</p>'''),
   ('減去兩塊不需要的三角形', None,
    r'''<p>$\triangle ABE$：底 $BE=\dfrac{5}{8}BC$，高與平行四邊形相同，故</p>
<p>$$\triangle ABE=\frac{5}{8}\times\frac{S}{2}=195$$</p>
<p>$\triangle ADF$ 與 $\triangle ABF$ 同高（底都在 $BD$ 上），故 $\triangle ADF=\dfrac{8}{5}\triangle ABF=\dfrac{8}{5}\times120=192$。</p>'''),
   ('求四邊形面積', None,
    r'''<p>$$CDFE=S-\triangle ABE-\triangle ADF=624-195-192=237\text{ cm}^{2}$$</p>'''),
 ],
 'ans': r'<b>A</b>（$237\text{ cm}^{2}$）',
 'practice': {
   'q': r'圖中 $PQRS$ 是平行四邊形，$T$ 在 $QR$ 上使 $QT:TR=3:2$。$PT$ 與 $QS$ 交於 $U$。若 $\triangle PQU$ 的面積為 $60\text{ cm}^{2}$，求四邊形 $SRTU$ 的面積。',
   'opts': [r'$124\text{ cm}^{2}$', r'$160\text{ cm}^{2}$', r'$196\text{ cm}^{2}$', r'$240\text{ cm}^{2}$'],
   'steps': [
     r'$\triangle QTU\sim\triangle PSU$，$QU:US=QT:PS=3:5$。',
     r'$\dfrac{\triangle PQU}{\triangle PQS}=\dfrac{3}{8}$，而 $\triangle PQS=\dfrac{S}{2}$，故 $60=\dfrac{3S}{16}$，$S=320$。',
     r'$\triangle PQT=\dfrac{3}{5}\times160=96$；$\triangle PSU=\dfrac{5}{8}\times160=100$；四邊形 $=320-96-100=124$。',
   ],
   'ans': r'<b>A</b>（$124\text{ cm}^{2}$）',
 },
},
]
