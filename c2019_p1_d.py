# -*- coding: utf-8 -*-
# 2019 卷一 Q15–Q19（題目依官方試卷）
QUESTIONS = [
{
 'year': '2019', 'paper': '卷一', 'num': 15,
 'h1': '「至少一名男生」用總數減去全女生的情況',
 'sub': '組合 · 補集思想',
 'q': r'''某班有 $21$ 名男生及 $11$ 名女生。若從班中選出 $5$ 名學生組成委員會，且委員會須有至少 $1$ 名男生，問可組成多少個不同的委員會？<span class="marks">[3 分]</span>''',
 'steps': [
   ('先算不加限制的總數', ('組合', r'從 $n$ 個選 $r$ 個：$C_{r}^{n}=\dfrac{n!}{r!(n-r)!}$。'),
    r'''<p>全班共 $32$ 人：</p>
<p>$$C_{5}^{32}=201\,376$$</p>'''),
   ('再算「不符合」的情況', None,
    r'''<p>不符合即全為女生（$11$ 人選 $5$ 人）：</p>
<p>$$C_{5}^{11}=462$$</p>'''),
   ('相減', ('補集', r'$P(\text{至少一個})=P(\text{全部})-P(\text{一個都無})$。'),
    r'''<p>$$201\,376-462=200\,914$$</p>'''),
   ('檢查合理性', None,
    r'''<p>答案應略小於 $C_{5}^{32}$，且為整數，符合。</p>'''),
 ],
 'ans': r'$200\,914$ 個',
 'practice': {
   'q': r'某組有 $15$ 名男生及 $9$ 名女生。從中選出 $4$ 人，且須有至少 $1$ 名女生，問有多少種選法？',
   'opts': [r'$9\,261$', r'$10\,626$', r'$1\,365$', r'$9\,000$'],
   'steps': [
     r'總數 $C_{4}^{24}=10\,626$。',
     r'全為男生 $C_{4}^{15}=1\,365$。',
     r'$10\,626-1\,365=9\,261$。',
   ],
   'ans': r'<b>A</b>（$9\,261$）',
 },
},
{
 'year': '2019', 'paper': '卷一', 'num': 16,
 'h1': '先解二次聯立，再把對數化為同底等差',
 'sub': '數列與對數 · 等差數列求和',
 'q': r'''設 $\alpha$ 及 $\beta$ 為實數，使 $\beta=5\alpha-18$ 及 $\beta=\alpha^{2}-13\alpha+63$。<br>
(a) 求 $\alpha$ 及 $\beta$。<br>
(b) 設 $T(n)$ 為一等差數列的第 $n$ 項，其中 $T(1)=\log\alpha$、$T(2)=\log\beta$。求使 $T(1)+T(2)+\cdots+T(n)>888$ 的最小 $n$ 值。<span class="marks">[6 分]</span>''',
 'steps': [
   ('(a) 兩式相等，解二次方程', None,
    r'''<p>$$5\alpha-18=\alpha^{2}-13\alpha+63$$</p>
<p>$$\alpha^{2}-18\alpha+81=0\quad\Longrightarrow\quad(\alpha-9)^{2}=0$$</p>'''),
   ('(a) 求 $\beta$', None,
    r'''<p>$$\alpha=9,\qquad \beta=5(9)-18=27$$</p>'''),
   ('(b) 寫出首兩項與公差', ('對數律', r'$\log 9=2\log 3$，$\log 27=3\log 3$。'),
    r'''<p>$$T(1)=2\log 3,\qquad T(2)=3\log 3$$</p>
<p>$$d=\log 3$$</p>'''),
   ('(b) 用等差求和公式', ('等差數列求和', r'$S_{n}=\dfrac{n}{2}\bigl[2a+(n-1)d\bigr]$。'),
    r'''<p>$$S_{n}=\frac{n}{2}\bigl[4\log3+(n-1)\log3\bigr]=\frac{n(n+3)}{2}\log3$$</p>'''),
   ('(b) 解不等式', None,
    r'''<p>$$\frac{n(n+3)}{2}\log3>888\quad\Longrightarrow\quad n^{2}+3n>\frac{1776}{\log3}\approx3722.3$$</p>
<p>解得 $n>59.53$，故最小整數 $n=60$。</p>
<p>覆核：$S_{59}=\dfrac{59\times62}{2}\log3\approx872.7<888$，$S_{60}=\dfrac{60\times63}{2}\log3\approx901.8>888$ ✓。</p>'''),
 ],
 'ans': r'(a) $\alpha=9,\ \beta=27$；(b) $60$',
 'practice': {
   'q': r'等差數列中 $T(1)=\log 4$、$T(2)=\log 8$。求使 $T(1)+\cdots+T(n)>200$ 的最小 $n$。',
   'opts': [r'$24$', r'$25$', r'$26$', r'$27$'],
   'steps': [
     r'$T(1)=2\log2$，$T(2)=3\log2$，$d=\log2$。',
     r'$S_{n}=\dfrac{n(n+3)}{2}\log2>200\Rightarrow n^{2}+3n>664.4$。',
     r'$n=24$：$648$；$n=25$：$700>664.4$，故最小 $n=25$。',
   ],
   'ans': r'<b>B</b>（$25$）',
 },
},
{
 'year': '2019', 'paper': '卷一', 'num': 17,
 'h1': '內切圓半徑把三角形面積拆成三份；角平分線就是軌跡',
 'sub': '坐標幾何 · 內切圓與軌跡',
 'q': r'''<br>(a) 設 $a$ 及 $p$ 分別為 $\triangle CDE$ 的面積及周界，並以 $r$ 表示 $\triangle CDE$ 的內切圓半徑。證明 $pr=2a$。<br>
(b) 點 $H$ 及 $K$ 的坐標分別為 $(9,12)$ 及 $(14,0)$。設 $P$ 為直角坐標平面上的一個動點，使 $P$ 到 $OH$ 的垂直距離等於 $P$ 到 $HK$ 的垂直距離，其中 $O$ 為原點。記 $P$ 的軌跡為 $\Gamma$。<br>
(i) 描述 $\Gamma$ 與 $\angle OHK$ 的幾何關係。<br>
(ii) 利用 (a)，求 $\Gamma$ 的方程。<span class="marks">[7 分]</span>''',
 'fig': r'''<svg viewBox="0 0 260 210" width="260" height="210" role="img" aria-label="三角形 OHK，O 為原點，H(9,12)，K(14,0)，內切圓圓心 (8,4)">
        <g stroke="currentColor" stroke-width="1" opacity="0.55" fill="none">
          <line x1="20" y1="190" x2="245" y2="190"/><line x1="30" y1="200" x2="30" y2="25"/>
        </g>
        <g fill="currentColor" font-size="11" font-family="Georgia,serif">
          <text x="236" y="203">x</text><text x="36" y="30">y</text><text x="16" y="203">O</text>
        </g>
        <g stroke="currentColor" stroke-width="1.5" fill="none">
          <path d="M30 190 L156 46 L226 190 Z"/>
          <path d="M156 46 L142 142" stroke-dasharray="4 3"/>
        </g>
        <circle cx="142" cy="142" r="6" fill="currentColor"/>
        <g fill="currentColor" font-size="12" font-family="Georgia,serif">
          <text x="152" y="40">H(9,12)</text><text x="214" y="205">K(14,0)</text>
          <text x="148" y="158" font-size="11">I(8,4)</text>
        </g>
      </svg><figcaption>圖：$\triangle OHK$ 與其內切圓圓心 $I(8,4)$</figcaption>''',
 'steps': [
   ('(a) 把三角形分成三個小三角形', ('內切圓', r'圓心到三邊的距離都等於 $r$。'),
    r'''<p>設內心為 $I$，連 $IC$、$ID$、$IE$，得三個高均為 $r$ 的三角形：</p>
<p>$$a=\frac{1}{2}r\cdot CD+\frac{1}{2}r\cdot DE+\frac{1}{2}r\cdot CE=\frac{r}{2}(CD+DE+CE)=\frac{pr}{2}$$</p>
<p>$$\therefore\ pr=2a$$</p>'''),
   ('(b)(i) 認出「到兩邊等距」的軌跡', ('角平分線', r'到一個角的兩邊距離相等的點，必在該角的角平分線上。'),
    r'''<p>$\Gamma$ 是 $\angle OHK$ 的角平分線（$\angle OHK$ 的內角平分線）。</p>'''),
   ('(b)(ii) 先算三邊與面積', ('距離公式、三角形面積', r'$d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$；$A=\dfrac{1}{2}\times\text{底}\times\text{高}$。'),
    r'''<p>$$OH=\sqrt{9^{2}+12^{2}}=15,\qquad HK=\sqrt{(14-9)^{2}+(0-12)^{2}}=13,\qquad OK=14$$</p>
<p>以 $OK$ 為底，高為 $H$ 的 $y$ 坐標 $12$：</p>
<p>$$a=\frac{1}{2}\times14\times12=84,\qquad p=15+13+14=42$$</p>'''),
   ('(b)(ii) 用 (a) 求內切圓半徑', None,
    r'''<p>$$42r=2(84)\quad\Longrightarrow\quad r=4$$</p>'''),
   ('(b)(ii) 定位內心，再寫出直線', ('內心的坐標', r'內心到 $OK$（$x$ 軸）的距離為 $r$，故 $y$ 坐標 $=4$。'),
    r'''<p>設內心為 $(h,4)$。由 $OH=15$、$OK=14$、$HK=13$ 的切線長關係：</p>
<p>$$(15-h)+(14-h)=13\quad\Longrightarrow\quad h=8$$</p>
<p>所以內心為 $I(8,4)$，而 $\Gamma$ 就是直線 $HI$：</p>
<p>$$\text{斜率}=\frac{12-4}{9-8}=8$$</p>
<p>$$y-4=8(x-8)\quad\Longrightarrow\quad 8x-y-60=0$$</p>'''),
 ],
 'ans': r'(b)(i) $\angle OHK$ 的角平分線；(b)(ii) $8x-y-60=0$',
 'practice': {
   'q': r'$\triangle PQR$ 的周界為 $30$，內切圓半徑為 $3$。求其面積。',
   'opts': [r'$30$', r'$45$', r'$60$', r'$90$'],
   'steps': [
     r'$pr=2a$。',
     r'$30\times3=2a\Rightarrow a=45$。',
   ],
   'ans': r'<b>B</b>（$45$）',
 },
},
{
 'year': '2019', 'paper': '卷一', 'num': 18,
 'h1': '先解 $\triangle ABD$，再在 $\triangle ACP$ 用餘弦公式',
 'sub': '三角學 · 立體圖形',
 'q': r'''圖 3 顯示一個四面體 $ABCD$。設 $P$ 為 $AD$ 上的一點，使 $BP$ 垂直於 $AD$。工匠量得 $AC=AD=CD=13\text{ cm}$、$BC=8\text{ cm}$、$BD=12\text{ cm}$ 及 $\angle ABD=72^{\circ}$。<br>
(a) 求 (i) $\angle BAD$；(ii) $CP$。<br>
(b) 工匠聲稱 $\angle BPC$ 是面 $ABD$ 與面 $ACD$ 之間的夾角。該聲稱是否正確？試解釋。<span class="marks">[7 分]</span>''',
 'fig': r'''<svg viewBox="0 0 280 220" width="280" height="220" role="img" aria-label="四面體 ABCD，P 在 AD 上，BP 垂直 AD">
        <g stroke="currentColor" stroke-width="1.4" fill="none">
          <path d="M40 180 L200 180 L150 40 Z"/>
          <path d="M150 40 L120 150"/>
          <path d="M120 150 L40 180" stroke-dasharray="4 3"/>
          <path d="M120 150 L200 180" stroke-dasharray="4 3"/>
          <path d="M120 150 L150 40"/>
          <path d="M120 150 L200 180"/>
        </g>
        <g fill="currentColor" font-size="13" font-family="Georgia,serif">
          <text x="28" y="196">B</text><text x="206" y="196">C</text>
          <text x="146" y="32">A</text><text x="112" y="166">D</text>
          <text x="126" y="142" font-size="11">P</text>
        </g>
      </svg><figcaption>圖 3：四面體 $ABCD$，$P$ 在 $AD$ 上且 $BP\perp AD$</figcaption>''',
 'steps': [
   ('(a)(i) 在 $\triangle ABD$ 用正弦公式', ('正弦公式', r'$\dfrac{\sin A}{a}=\dfrac{\sin B}{b}$，邊與對角要配對。'),
    r'''<p>$$\frac{\sin\angle BAD}{BD}=\frac{\sin\angle ABD}{AD}$$</p>
<p>$$\frac{\sin\angle BAD}{12}=\frac{\sin72^{\circ}}{13}\quad\Longrightarrow\quad\sin\angle BAD\approx0.8778$$</p>'''),
   ('(a)(i) 判斷取哪一個解', ('三角形內角和', r'三角之和為 $180^{\circ}$，故不可能有兩個大角。'),
    r'''<p>$$\angle BAD\approx61.39^{\circ}\ \text{或}\ 118.61^{\circ}$$</p>
<p>$118.61^{\circ}+72^{\circ}>180^{\circ}$，捨去。</p>
<p>$$\angle BAD=61.4^{\circ}$$</p>'''),
   ('(a)(ii) 在直角三角形 $BPD$ 求 $AP$', ('餘弦', r'$\cos\theta=\dfrac{\text{鄰邊}}{\text{斜邊}}$。'),
    r'''<p>$$\angle ADB=180^{\circ}-72^{\circ}-61.39^{\circ}=46.61^{\circ}$$</p>
<p>$BP\perp AD$，故在 $\triangle BPD$ 中：</p>
<p>$$DP=BD\cos46.61^{\circ}\approx8.24\text{ cm}$$</p>
<p>$$AP=13-8.24=4.76\text{ cm}$$</p>'''),
   ('(a)(ii) 在 $\triangle ACP$ 用餘弦公式', ('餘弦公式', r'$c^{2}=a^{2}+b^{2}-2ab\cos C$。'),
    r'''<p>$$\angle CAP=60^{\circ}\ (\triangle ACD\ \text{為等邊三角形})$$</p>
<p>$$CP^{2}=13^{2}+4.76^{2}-2(13)(4.76)\cos60^{\circ}\approx129.8$$</p>
<p>$$CP\approx11.4\text{ cm}$$</p>'''),
   ('(b) 檢查 $CP$ 是否垂直於 $AD$', ('畢氏定理逆定理', r'若 $\angle APC=90^{\circ}$，則 $AP^{2}+CP^{2}=AC^{2}$。'),
    r'''<p>$$AP^{2}+CP^{2}\approx22.6+129.8=152.4\neq169=AC^{2}$$</p>
<p>所以 $\angle APC\neq90^{\circ}$，即 $CP$ **不**垂直於 $AD$。</p>'''),
   ('(b) 下結論', None,
    r'''<p>兩面夾角須由兩條同時垂直於交線 $AD$ 的直線量度。此處 $BP\perp AD$ 成立，但 $CP$ 不垂直於 $AD$，故 $\angle BPC$ 不是該夾角。</p>
<p>∴ 聲稱不正確。</p>'''),
 ],
 'ans': r'(a)(i) $61.4^{\circ}$；(ii) $11.4\text{ cm}$；(b) 不正確',
 'practice': {
   'q': r'在 $\triangle ABC$ 中 $AB=10$、$\angle ABC=40^{\circ}$、$\angle ACB=80^{\circ}$。求 $AC$（準確至 $0.1$）。',
   'opts': [r'$6.5$', r'$7.8$', r'$8.9$', r'$9.6$'],
   'steps': [
     r'$\angle BAC=60^{\circ}$。',
     r'$\dfrac{AC}{\sin40^{\circ}}=\dfrac{10}{\sin80^{\circ}}$。',
     r'$AC=\dfrac{10\sin40^{\circ}}{\sin80^{\circ}}\approx6.5$。',
   ],
   'ans': r'<b>A</b>（$6.5$）',
 },
},
{
 'year': '2019', 'paper': '卷一', 'num': 19,
 'h1': '配方法找頂點，再用「直徑所對圓周角」處理圓面積最小',
 'sub': '函數與圖像 · 配方法與共圓',
 'q': r'''設 $f(x)=\dfrac{1}{1+k}\bigl(x^{2}+(6k-2)x+(9k+25)\bigr)$，其中 $k$ 為正常數。記點 $(4,33)$ 為 $F$。<br>
(a) 證明 $y=f(x)$ 的圖像通過 $F$。<br>
(b) $y=g(x)$ 的圖像由 $y=f(x)$ 的圖像沿 $y$ 軸反射，再把所得圖像向上平移 $4$ 單位而得。設 $U$ 為 $y=g(x)$ 的圖像的頂點，$O$ 為原點。<br>
(i) 用配方法，以 $k$ 表示 $U$ 的坐標。<br>
(ii) 求 $k$，使通過 $F$、$O$ 及 $U$ 的圓的面積最小。<br>
(iii) 對任意正常數 $k$，$y=g(x)$ 的圖像都通過同一點 $G$。設 $V$ 為使通過 $F$、$O$、$V$ 的圓面積最小的頂點。$F$、$G$、$O$、$V$ 是否共圓？試解釋。<span class="marks">[12 分]</span>''',
 'steps': [
   ('(a) 代入 $x=4$', None,
    r'''<p>$$f(4)=\frac{16+4(6k-2)+(9k+25)}{1+k}=\frac{16+24k-8+9k+25}{1+k}=\frac{33+33k}{1+k}=33$$</p>
<p>∴ 圖像通過 $F(4,33)$。</p>'''),
   ('(b)(i) 先寫出 $g(x)$', ('反射與平移', r'沿 $y$ 軸反射：$x\to-x$；向上平移 $4$：$+4$。'),
    r'''<p>$$g(x)=f(-x)+4=\frac{x^{2}-(6k-2)x+(9k+25)}{1+k}+4$$</p>'''),
   ('(b)(i) 配方', ('配方法', r'$x^{2}+bx=\left(x+\dfrac{b}{2}\right)^{2}-\dfrac{b^{2}}{4}$。'),
    r'''<p>$$x^{2}-(6k-2)x=\bigl(x-(3k-1)\bigr)^{2}-(3k-1)^{2}$$</p>
<p>經整理（分子加上 $4(1+k)$）：</p>
<p>$$g(x)=\frac{1}{1+k}\bigl(x-(3k-1)\bigr)^{2}+(28-9k)$$</p>
<p>$$\therefore\ U\bigl(3k-1,\ 28-9k\bigr)$$</p>'''),
   ('(b)(ii) 面積最小的條件', ('圓的直徑', r'過兩定點的圓中，以該兩點連線為直徑時面積最小。'),
    r'''<p>圓通過 $F$、$O$，面積最小時 $FO$ 為直徑，此時圓周角 $\angle FUO=90^{\circ}$。</p>'''),
   ('(b)(ii) 用斜率乘積等於 $-1$', ('垂直條件', r'$m_{1}m_{2}=-1$。'),
    r'''<p>$$\frac{28-9k}{3k-1}\times\frac{33-(28-9k)}{4-(3k-1)}=-1$$</p>
<p>$$\frac{(28-9k)(5+9k)}{(3k-1)(5-3k)}=-1$$</p>
<p>化簡得 $2k^{2}-5k-3=0$，即 $k=3$ 或 $k=-\dfrac{1}{2}$（捨去，$k>0$）。</p>
<p>$$\therefore\ k=3$$</p>'''),
   ('(b)(iii) 找出 $G$ 與檢驗共圓', ('定點', r'若對所有 $k$ 都通過 $G$，可比較係數得 $G(-4,37)$。'),
    r'''<p>取 $k=3$ 時 $V=U=(8,1)$。檢驗直角：</p>
<p>$$m_{VF}\times m_{VO}=\frac{1-33}{8-4}\times\frac{1-0}{8-0}=(-8)\times\frac{1}{8}=-1$$</p>
<p>∴ $\angle FVO=90^{\circ}$，即 $FO$ 是圓的直徑。</p>
<p>再看 $G$：</p>
<p>$$m_{FG}\times m_{GO}=\frac{37-33}{-4-4}\times\frac{37-0}{-4-0}=\left(-\frac{1}{2}\right)\left(-\frac{37}{4}\right)=\frac{37}{8}\neq-1$$</p>
<p>∴ $\angle FGO\neq90^{\circ}$。若四點共圓，因 $FO$ 為直徑，$\angle FGO$ 也必須是 $90^{\circ}$；矛盾。</p>
<p>∴ $F$、$G$、$O$、$V$ 不共圓。</p>'''),
 ],
 'ans': r'(b)(i) $U(3k-1,\,28-9k)$；(ii) $k=3$；(iii) 不共圓',
 'practice': {
   'q': r'設 $g(x)=x^{2}-4kx+3$。求 $y=g(x)$ 的頂點坐標。',
   'opts': [r'$(2k,\,3-4k^{2})$', r'$(2k,\,3+4k^{2})$', r'$(4k,\,3-4k^{2})$', r'$(2k,\,3-2k^{2})$'],
   'steps': [
     r'$g(x)=(x-2k)^{2}+3-4k^{2}$。',
     r'頂點 $(2k,\,3-4k^{2})$。',
   ],
   'ans': r'<b>A</b>',
 },
},
]
