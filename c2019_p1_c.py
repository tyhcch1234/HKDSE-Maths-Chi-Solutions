# -*- coding: utf-8 -*-
# 2019 卷一 Q11–Q14（題目依官方試卷）
QUESTIONS = [
{
 'year': '2019', 'paper': '卷一', 'num': 11,
 'h1': '設商為 $ax+b$，用餘式定理反求係數',
 'sub': '多項式 · 餘式定理與除法',
 'q': r'''設 $p(x)$ 為三次多項式。當 $p(x)$ 除以 $x-1$ 時，餘數為 $50$；當 $p(x)$ 除以 $x+2$ 時，餘數為 $-52$。已知 $p(x)$ 可被 $2x^{2}+9x+14$ 整除。<br>
(a) 求 $p(x)$ 除以 $2x^{2}+9x+14$ 時的商。<br>
(b) 方程 $p(x)=0$ 有多少個有理根？試解釋。<span class="marks">[6 分]</span>''',
 'steps': [
   ('(a) 設商並寫出除法關係', ('除法算式', r'三次 ÷ 二次 ⇒ 商為一次式 $ax+b$：$p(x)=(ax+b)(2x^{2}+9x+14)$。'),
    r'''<p>$$p(x)=(ax+b)(2x^{2}+9x+14)$$</p>'''),
   ('(a) 用餘式定理代入 $x=1$、$x=-2$', ('餘式定理', r'$p(x)$ 除以 $x-c$ 的餘數為 $p(c)$。'),
    r'''<p>$$p(1)=(a+b)(25)=50\quad\Longrightarrow\quad a+b=2$$</p>
<p>$$p(-2)=(-2a+b)(8-18+14)=(-2a+b)(4)=-52\quad\Longrightarrow\quad -2a+b=-13$$</p>'''),
   ('(a) 解聯立方程', None,
    r'''<p>兩式相減：$3a=15\Rightarrow a=5$，代回得 $b=-3$。</p>
<p>所求商為 $5x-3$。</p>'''),
   ('(b) 把 $p(x)=0$ 拆成兩個因式', None,
    r'''<p>$$(5x-3)(2x^{2}+9x+14)=0$$</p>
<p>故 $5x-3=0$ 或 $2x^{2}+9x+14=0$。</p>'''),
   ('(b) 用判別式檢查二次因式', ('判別式', r'$\Delta=b^{2}-4ac$；$\Delta<0$ 表示沒有實根。'),
    r'''<p>$$\Delta=9^{2}-4(2)(14)=81-112=-31<0$$</p>
<p>所以 $2x^{2}+9x+14=0$ 沒有實根（更不可能是有理根）。</p>'''),
   ('(b) 數有理根', None,
    r'''<p>只剩 $x=\dfrac{3}{5}$，是有理數。</p>
<p>∴ $p(x)=0$ 有 $1$ 個有理根。</p>'''),
 ],
 'ans': r'(a) $5x-3$；(b) $1$ 個有理根',
 'practice': {
   'q': r'設 $p(x)$ 為三次多項式，$p(1)=30$、$p(-1)=6$，且 $p(x)$ 可被 $x^{2}+x+3$ 整除。求 $p(x)$ 除以 $x^{2}+x+3$ 的商。',
   'opts': [r'$2x+4$', r'$4x+2$', r'$6x$', r'$3x+3$'],
   'steps': [
     r'設 $p(x)=(ax+b)(x^{2}+x+3)$。',
     r'$p(1)=5(a+b)=30\Rightarrow a+b=6$；$p(-1)=3(b-a)=6\Rightarrow b-a=2$。',
     r'解得 $a=2,b=4$，商為 $2x+4$。',
   ],
   'ans': r'<b>A</b>（$2x+4$）',
 },
},
{
 'year': '2019', 'paper': '卷一', 'num': 12,
 'h1': '先數清 $n$，再定四分位位置；平均數用來鎖定 $a+b$',
 'sub': '統計 · 莖葉圖、四分位數與標準差',
 'q': r'''下面的莖葉圖顯示一些男生在 $400\text{ m}$ 賽跑中的成績（以秒為單位）。已知該分佈的四分位數間距為 $8$ 秒。<br>
(a) 求 $c$。<br>
(b) 已知該分佈的分佈域超過 $34$ 秒，且平均數為 $69$ 秒。求<br>
(i) $a$ 及 $b$；<br>(ii) 該分佈的最小可能標準差。<span class="marks">[8 分]</span>''',
 'fig': r'''<table class="data-table">
        <thead><tr><th>莖（十位）</th><th>葉（個位）</th></tr></thead>
        <tbody>
          <tr><td>5</td><td>$a$</td></tr>
          <tr><td>6</td><td>$0\quad0\quad3\quad c\quad c\quad8\quad9\quad9\quad9$</td></tr>
          <tr><td>7</td><td>$0\quad1\quad1\quad1\quad2\quad2\quad5\quad6\quad9$</td></tr>
          <tr><td>8</td><td>$b$</td></tr>
        </tbody>
      </table><figcaption>圖：莖葉圖（共 $20$ 個數據）</figcaption>''',
 'steps': [
   ('先數數據個數', None,
    r'''<p>莖 5：$1$ 個；莖 6：$9$ 個；莖 7：$9$ 個；莖 8：$1$ 個。</p>
<p>$$n=20$$</p>'''),
   ('(a) 定位四分位數', ('四分位數位置', r'$n=20$ 時，下四分位數取第 $5$、$6$ 個值的平均，上四分位數取第 $15$、$16$ 個值的平均。'),
    r'''<p>排序後：莖 6 的九個值佔第 $2$ 至 $10$ 位，其中第 $5$、$6$ 位都是 $60+c$；第 $15$、$16$ 位都是 $72$。</p>
<p>$$Q_{1}=60+c,\qquad Q_{3}=72$$</p>'''),
   ('(a) 用四分位數間距求 $c$', ('四分位數間距', r'$\text{IQR}=Q_{3}-Q_{1}$。'),
    r'''<p>$$72-(60+c)=8\quad\Longrightarrow\quad c=4$$</p>'''),
   ('(b)(i) 由分佈域寫出第一個條件', ('分佈域', r'分佈域 $=$ 最大值 $-$ 最小值。'),
    r'''<p>$$(80+b)-(50+a)>34\quad\Longrightarrow\quad b-a>4$$</p>'''),
   ('(b)(i) 由平均數寫出第二個條件', ('平均數', r'$\sum x=n\bar{x}=20\times69=1380$。'),
    r'''<p>莖 6 之和 $=586$，莖 7 之和 $=657$，故</p>
<p>$$(50+a)+586+657+(80+b)=1380\quad\Longrightarrow\quad a+b=7$$</p>
<p>配合 $b-a>4$，得 $(a,b)=(0,7)$ 或 $(1,6)$。</p>'''),
   ('(b)(ii) 比較兩個情況的標準差', ('標準差', r'$\sigma=\sqrt{\dfrac{\sum(x-\bar{x})^{2}}{n}}$（整組數據）。'),
    r'''<p>情況一 $(a,b)=(0,7)$：$\sigma\approx7.58$ 秒。</p>
<p>情況二 $(a,b)=(1,6)$：$\sigma\approx7.34$ 秒。</p>
<p>最小可能標準差為 $7.34$ 秒（即 $a=1$、$b=6$）。</p>
<p>直觀解釋：$(a,b)=(1,6)$ 令兩端數據更靠近平均數 $69$，離差平方和較小。</p>'''),
 ],
 'ans': r'(a) $c=4$；(b)(i) $(a,b)=(0,7)$ 或 $(1,6)$；(ii) $7.34$ 秒',
 'practice': {
   'q': r'''某組 $12$ 個數據排序後為 $3,5,7,8,9,11,12,14,15,16,18,20$。求其四分位數間距。''',
   'opts': [r'$6$', r'$7$', r'$8$', r'$9$'],
   'steps': [
     r'$n=12$：$Q_{1}$ 取第 $3$、$4$ 個值的平均 $=(7+8)/2=7.5$。',
     r'$Q_{3}$ 取第 $9$、$10$ 個值的平均 $=(15+16)/2=15.5$。',
     r'$\text{IQR}=15.5-7.5=8$。',
   ],
   'ans': r'<b>C</b>（$8$）',
 },
},
{
 'year': '2019', 'paper': '卷一', 'num': 13,
 'h1': '圓內接四邊形補角，直徑所對圓周角是直角',
 'sub': '圓形幾何 · 圓內接四邊形與扇形',
 'q': r'''圖 1 中，$O$ 為圓 $ABCDE$ 的圓心。$AC$ 為該圓的一條直徑。$BD$ 與 $OC$ 相交於點 $F$。已知 $\angle AED=115^{\circ}$。<br>
(a) 求 $\angle CBF$。<br>
(b) 設 $BC\parallel OD$ 且 $OB=18\text{ cm}$。扇形 $OBC$ 的周界是否小於 $60\text{ cm}$？試解釋。<span class="marks">[8 分]</span>''',
 'fig': r'''<svg viewBox="0 0 280 250" width="280" height="250" role="img" aria-label="圓 ABCDE，AC 為直徑，BD 與 OC 交於 F">
        <circle cx="140" cy="130" r="95" fill="none" stroke="currentColor" stroke-width="1.5"/>
        <g stroke="currentColor" stroke-width="1.2" fill="none">
          <line x1="45" y1="130" x2="235" y2="130"/>
          <path d="M112 51 L206 159"/>
          <path d="M112 51 L45 130"/>
          <path d="M112 51 L235 130"/>
          <path d="M206 159 L45 130"/>
          <path d="M140 130 L206 159"/>
          <path d="M140 130 L112 51"/>
          <path d="M140 130 L168 43"/>
          <path d="M168 43 L45 130"/>
        </g>
        <g fill="currentColor" font-size="13" font-family="Georgia,serif">
          <text x="136" y="146" font-size="11">O</text>
          <text x="34" y="126">C</text>
          <text x="238" y="126">A</text>
          <text x="104" y="44">D</text>
          <text x="170" y="36">E</text>
          <text x="211" y="176">B</text>
          <text x="128" y="150" font-size="11">F</text>
        </g>
      </svg><figcaption>圖 1：$O$ 為圓心，$AC$ 為直徑，$BD$ 與 $OC$ 交於 $F$</figcaption>''',
 'steps': [
   ('(a) 認出圓內接四邊形 $ABED$', ('圓內接四邊形', r'圓內接四邊形的對角互補：$\angle ABF+\angle AED=180^{\circ}$。'),
    r'''<p>$$\angle ABF=180^{\circ}-115^{\circ}=65^{\circ}$$</p>'''),
   ('(a) 用直徑所對的圓周角', ('半圓上的圓周角', r'$AC$ 為直徑 $\Rightarrow\angle ABC=90^{\circ}$。'),
    r'''<p>$$\angle CBF=90^{\circ}-65^{\circ}=25^{\circ}$$</p>'''),
   ('(b) 由平行線與等腰三角形找角', ('內錯角、等腰三角形', r'$BC\parallel OD\Rightarrow\angle ODF=\angle CBF$；$OB=OD$（半徑）$\Rightarrow\angle OBF=\angle ODF$。'),
    r'''<p>$$\angle ODF=\angle OBF=25^{\circ}$$</p>'''),
   ('(b) 求圓心角 $\angle BOC$', ('圓心角是圓周角的兩倍', r'同弧所對的圓心角 $=2\times$ 圓周角。'),
    r'''<p>$$\angle DOF=2\angle CBF=50^{\circ}$$</p>
<p>在 $\triangle OBF$ 中：$\angle BOF=180^{\circ}-25^{\circ}-25^{\circ}=130^{\circ}$，故</p>
<p>$$\angle BOC=130^{\circ}-50^{\circ}=80^{\circ}$$</p>'''),
   ('(b) 計算扇形周界', ('扇形周界', r'周界 $=\dfrac{\theta}{360^{\circ}}(2\pi r)+2r$。'),
    r'''<p>$$\frac{80}{360}(2\pi\times18)+2(18)=8\pi+36\approx61.13\text{ cm}$$</p>
<p>$61.13>60$，所以扇形 $OBC$ 的周界**不**小於 $60\text{ cm}$。</p>'''),
 ],
 'ans': r'(a) $25^{\circ}$；(b) 否，周界約 $61.1\text{ cm}>60\text{ cm}$',
 'practice': {
   'q': r'圓內接四邊形 $PQRS$ 中 $\angle PQR=105^{\circ}$。求 $\angle PSR$。',
   'opts': [r'$55^{\circ}$', r'$65^{\circ}$', r'$75^{\circ}$', r'$105^{\circ}$'],
   'steps': [
     r'圓內接四邊形對角互補。',
     r'$\angle PSR=180^{\circ}-105^{\circ}=75^{\circ}$。',
   ],
   'ans': r'<b>C</b>（$75^{\circ}$）',
 },
},
{
 'year': '2019', 'paper': '卷一', 'num': 14,
 'h1': '先證全等與相似，再把 $\ell$ 與 $\sqrt{2}\ell$ 放上同一條對角線',
 'sub': '幾何 · 全等、相似與正方形',
 'q': r'''圖 2 中，$ABCD$ 為正方形。已知 $E$ 為 $AD$ 上的一點。$BD$ 與 $CE$ 相交於點 $F$。設 $G$ 為一點使 $BG\parallel EC$ 及 $CG\parallel DB$。<br>
(a) 證明 (i) $\triangle BCG\cong\triangle CBF$；(ii) $\triangle BCF\sim\triangle DEF$。<br>
(b) 設 $\angle BCF=\angle BGC$。<br>
(i) 設 $BC=\ell$，以 $\ell$ 表示 $DF$。<br>
(ii) 有人聲稱 $AE>DF$。你是否同意？試解釋。<span class="marks">[8 分]</span>''',
 'fig': r'''<svg viewBox="0 0 300 210" width="300" height="210" role="img" aria-label="正方形 ABCD，E 在 AD 上，BD 與 CE 交於 F，G 使 BG 平行 EC、CG 平行 DB">
        <g stroke="currentColor" stroke-width="1.4" fill="none">
          <rect x="45" y="30" width="150" height="150"/>
          <path d="M45 30 L195 180"/>
          <path d="M45 105 L195 180"/>
          <path d="M195 30 L245 95 L195 180"/>
        </g>
        <g fill="currentColor" font-size="13" font-family="Georgia,serif">
          <text x="36" y="26">A</text><text x="197" y="24">B</text>
          <text x="36" y="196">D</text><text x="197" y="196">C</text>
          <text x="30" y="108">E</text><text x="96" y="112" font-size="11">F</text>
          <text x="249" y="99">G</text>
        </g>
      </svg><figcaption>圖 2：$ABCD$ 為正方形，$BG\parallel EC$，$CG\parallel DB$</figcaption>''',
 'steps': [
   ('(a)(i) 列出三組相等條件', ('A.S.A. 全等', r'兩角及其夾邊分別相等。'),
    r'''<p>$BC=BC$（公共邊）；</p>
<p>$\angle BCG=\angle CBF$（內錯角，$CG\parallel DB$）；</p>
<p>$\angle CBG=\angle BCF$（內錯角，$BG\parallel EC$）。</p>
<p>$$\therefore\ \triangle BCG\cong\triangle CBF\quad(\text{A.S.A.})$$</p>'''),
   ('(a)(ii) 用平行線找三組等角', ('A.A.A. 相似', r'三個角分別相等即相似。'),
    r'''<p>$\angle CBF=\angle EDF$（內錯角，$BC\parallel ED$）；</p>
<p>$\angle BFC=\angle DFE$（對頂角）；</p>
<p>$\angle BCF=\angle DEF$（三角形內角和）。</p>
<p>$$\therefore\ \triangle BCF\sim\triangle DEF\quad(\text{A.A.A.})$$</p>'''),
   ('(b)(i) 由全等與題設得等腰', ('等腰三角形判定', r'兩底角相等 $\Rightarrow$ 對邊相等。'),
    r'''<p>由 (a)(i) 得 $\angle BGC=\angle BFC$；題設 $\angle BCF=\angle BGC$，故 $\angle BCF=\angle BFC$。</p>
<p>$$\therefore\ BF=BC=\ell$$</p>'''),
   ('(b)(i) 用正方形對角線求 $DF$', ('正方形對角線', r'邊長 $\ell$ 的正方形，對角線 $=\sqrt{2}\ell$。'),
    r'''<p>$$BD=\sqrt{2}\,\ell$$</p>
<p>$$DF=BD-BF=\sqrt{2}\,\ell-\ell=(\sqrt{2}-1)\ell$$</p>'''),
   ('(b)(ii) 比較 $AE$ 與 $DF$', None,
    r'''<p>由 (a)(ii) 相似及 (b)(i) 的等腰關係，$DE=DF=(\sqrt{2}-1)\ell$。</p>
<p>$$AE=AD-DE=\ell-(\sqrt{2}-1)\ell=(2-\sqrt{2})\ell$$</p>
<p>比較係數：$2-\sqrt{2}\approx0.586$，$\sqrt{2}-1\approx0.414$，故 $AE>DF$。</p>
<p>∴ 同意該聲稱。</p>'''),
 ],
 'ans': r'(b)(i) $DF=(\sqrt{2}-1)\ell$；(b)(ii) 同意，因 $2-\sqrt{2}>\sqrt{2}-1$',
 'practice': {
   'q': r'正方形 $ABCD$ 的邊長為 $8\text{ cm}$，對角線 $BD$ 上有一點 $P$ 使 $BP=8\text{ cm}$。求 $DP$。',
   'opts': [r'$8(\sqrt{2}-1)\text{ cm}$', r'$8\sqrt{2}\text{ cm}$', r'$8\text{ cm}$', r'$4\sqrt{2}\text{ cm}$'],
   'steps': [
     r'對角線 $BD=8\sqrt{2}$。',
     r'$DP=8\sqrt{2}-8=8(\sqrt{2}-1)$。',
   ],
   'ans': r'<b>A</b>',
 },
},
]
