# -*- coding: utf-8 -*-
# 2019 卷二 Q20 / Q21 / Q31 / Q34：依官方試卷更正選項與答案
QUESTIONS = [
{
 'year': '2019', 'paper': '卷二', 'num': 20,
 'h1': '先由等腰三角形求出 $62^{\\circ}$，再逐層推到菱形',
 'sub': '幾何 · 菱形與等腰三角形',
 'q': r'''圖中 $ABCD$ 為菱形。$ABE$ 與 $BCF$ 均為直線，且 $BE=EF$。若 $\angle BEF=56^{\circ}$，則 $\angle BDC=$''',
 'opts': [r'$48^{\circ}$', r'$56^{\circ}$', r'$59^{\circ}$', r'$62^{\circ}$'],
 'fig': r'''<img src="figures/2019_P2_Q20.png" alt="菱形 ABCD，A、B、E 共線，B、C、F 共線，BE=EF"><figcaption>圖：菱形 $ABCD$，$ABE$、$BCF$ 為直線，$BE=EF$，$\angle BEF=56^{\circ}$</figcaption>''',
 'steps': [
   ('先看等腰三角形 $BEF$', ('等腰三角形底角相等', r'$BE=EF\Rightarrow\angle EBF=\angle BFE$；三角形內角和 $180^{\circ}$。'),
    r'''<p>頂角 $\angle BEF=56^{\circ}$，兩個底角平分餘下的 $124^{\circ}$：</p>
<p>$$\angle EBF=\angle BFE=\frac{180^{\circ}-56^{\circ}}{2}=62^{\circ}$$</p>'''),
   ('把 $62^{\circ}$ 搬到 $\angle EBC$', ('同一射線', r'$B$、$C$、$F$ 共線且 $F$ 在 $C$ 之外，所以射線 $BF$ 與射線 $BC$ 是同一條。'),
    r'''<p>$\angle EBF$ 的兩邊是 $BE$ 與 $BF$；既然 $BF$ 就是 $BC$，</p>
<p>$$\angle EBC=\angle EBF=62^{\circ}$$</p>'''),
   ('用直線上的鄰角求 $\angle ABC$', ('直線上的鄰角', r'$A$、$B$、$E$ 共線，$\angle ABC+\angle EBC=180^{\circ}$。'),
    r'''<p>$$\angle ABC=180^{\circ}-62^{\circ}=118^{\circ}$$</p>
<p>易錯：$A$ 與 $E$ 在 $B$ 的兩側，$BA$ 與 $BE$ 是相反射線，所以兩角互補而不是相等。</p>'''),
   ('用平行線的同旁內角求 $\angle BCD$', ('同旁內角互補', r'菱形中 $AB\parallel DC$，$BC$ 為截線，$\angle ABC+\angle BCD=180^{\circ}$。'),
    r'''<p>$$\angle BCD=180^{\circ}-118^{\circ}=62^{\circ}$$</p>'''),
   ('在等腰三角形 $BCD$ 求 $\angle BDC$', ('等腰三角形', r'$BC=CD$（菱形四邊相等），故 $\angle CBD=\angle BDC$。'),
    r'''<p>$$2\angle BDC+62^{\circ}=180^{\circ}\quad\Longrightarrow\quad \angle BDC=\frac{118^{\circ}}{2}=59^{\circ}$$</p>'''),
 ],
 'ans': r'<b>C</b>（$59^{\circ}$）',
 'practice': {
   'q': r'圖中 $ABCD$ 為菱形，$ABE$、$BCF$ 為直線，$BE=EF$。若 $\angle BEF=44^{\circ}$，則 $\angle BDC=$',
   'opts': [r'$28^{\circ}$', r'$56^{\circ}$', r'$62^{\circ}$', r'$68^{\circ}$'],
   'steps': [
     r'等腰 $\triangle BEF$：底角 $=\dfrac{180^{\circ}-44^{\circ}}{2}=68^{\circ}$，即 $\angle EBC=68^{\circ}$。',
     r'直線上的鄰角：$\angle ABC=180^{\circ}-68^{\circ}=112^{\circ}$。',
     r'同旁內角：$\angle BCD=180^{\circ}-112^{\circ}=68^{\circ}$。',
     r'等腰 $\triangle BCD$：$\angle BDC=\dfrac{180^{\circ}-68^{\circ}}{2}=56^{\circ}$。',
   ],
   'ans': r'<b>B</b>（$56^{\circ}$）',
 },
},
{
 'year': '2019', 'paper': '卷二', 'num': 21,
 'h1': '等弦截等弧，扣去公共弧再分半',
 'sub': '圓形性質 · 等弦、圓周角',
 'q': r'''圖中 $O$ 為半圓 $ABCD$ 的圓心。若 $AC=BD$ 且 $\angle COD=48^{\circ}$，則 $\angle ABD=$''',
 'opts': [r'$31^{\circ}$', r'$33^{\circ}$', r'$42^{\circ}$', r'$48^{\circ}$'],
 'fig': r'''<img src="figures/2019_P2_Q21.png" alt="半圓 ABCD，圓心 O，A、B 為直徑兩端"><figcaption>圖：$AB$ 為直徑，$D$、$C$ 依次在半圓上，$AC=BD$，$\angle COD=48^{\circ}$</figcaption>''',
 'steps': [
   ('讀圖：認清次序與半圓', None,
    r'''<p>$AOB$ 成一直線，$AB$ 是直徑；沿半圓由 $A$ 到 $B$ 的次序是 $A\to D\to C\to B$。</p>
<p>整個半圓的圓心角是 $180^{\circ}$，即弧 $AD+$ 弧 $DC+$ 弧 $CB=180^{\circ}$。</p>'''),
   ('等弦截等弧，扣去公共弧', ('等弦對等弧', r'同圓中 $AC=BD\Rightarrow$ 弧 $AC=$ 弧 $BD$。'),
    r'''<p>弧 $AC=$ 弧 $AD+$ 弧 $DC$，弧 $BD=$ 弧 $BC+$ 弧 $CD$。兩者相等而弧 $DC$ 是公共部分，故</p>
<p>$$\text{弧 }AD=\text{弧 }BC$$</p>'''),
   ('用半圓的 $180^{\circ}$ 求弧 $AD$', ('圓心角與弧', r'弧 $DC$ 對 $\angle COD=48^{\circ}$，即弧 $DC=48^{\circ}$。'),
    r'''<p>設弧 $AD=$ 弧 $BC=y$：</p>
<p>$$y+48^{\circ}+y=180^{\circ}\quad\Longrightarrow\quad y=66^{\circ}$$</p>'''),
   ('弧化為圓周角', ('圓周角是圓心角的一半', r'$\angle ABD$ 的頂點在圓周，兩邊截出弧 $AD$。'),
    r'''<p>$$\angle ABD=\frac{66^{\circ}}{2}=33^{\circ}$$</p>'''),
   ('用等腰三角形 $OBD$ 覆核', ('半徑相等', r'$OB=OD$，$\triangle OBD$ 為等腰。'),
    r'''<p>弧 $BD=66^{\circ}+48^{\circ}=114^{\circ}$，故 $\angle BOD=114^{\circ}$，</p>
<p>$$\angle OBD=\frac{180^{\circ}-114^{\circ}}{2}=33^{\circ}$$</p>
<p>與第 4 步一致。易錯：直接把 $48^{\circ}$ 減半得 $24^{\circ}$——$48^{\circ}$ 對的是弧 $CD$，不是弧 $AD$。</p>'''),
 ],
 'ans': r'<b>B</b>（$33^{\circ}$）',
 'practice': {
   'q': r'圖中 $O$ 為半圓 $ABCD$ 的圓心。若 $AC=BD$ 且 $\angle COD=60^{\circ}$，則 $\angle ABD=$',
   'opts': [r'$24^{\circ}$', r'$30^{\circ}$', r'$48^{\circ}$', r'$60^{\circ}$'],
   'steps': [
     r'$AC=BD\Rightarrow$ 弧 $AD=$ 弧 $BC$（扣去公共弧 $CD$）。',
     r'$2y+60^{\circ}=180^{\circ}\Rightarrow y=60^{\circ}$。',
     r'$\angle ABD=\dfrac{60^{\circ}}{2}=30^{\circ}$。',
   ],
   'ans': r'<b>B</b>（$30^{\circ}$）',
 },
},
{
 'year': '2019', 'paper': '卷二', 'num': 31,
 'h1': '留意縱軸是 $\\log_{9}y$，不是 $\\log_{3}y$',
 'sub': '對數 · 對數圖像與對數律',
 'q': r'''已知 $\log_{9}y$ 是 $\log_{3}x$ 的線性函數。該線性函數圖像的縱軸截距及橫軸截距分別為 $7$ 及 $8$。下列哪項必定正確？''',
 'opts': [r'$x^{4}y^{7}=3^{56}$', r'$x^{7}y^{4}=3^{56}$', r'$x^{7}y^{8}=3^{56}$', r'$x^{8}y^{7}=3^{56}$'],
 'fig': r'''<svg viewBox="0 0 300 240" width="300" height="240" role="img" aria-label="log9 y 對 log3 x 的直線圖像，縱軸截距 7、橫軸截距 8">
        <g fill="none" stroke="currentColor" stroke-width="1.3">
          <line x1="45" y1="200" x2="275" y2="200"/>
          <line x1="45" y1="200" x2="45" y2="35"/>
          <line x1="45" y1="75" x2="225" y2="200"/>
        </g>
        <g fill="currentColor" font-size="12" font-family="Georgia,serif">
          <text x="40" y="60" text-anchor="end">7</text>
          <text x="225" y="216" text-anchor="middle">8</text>
          <text x="270" y="216" text-anchor="middle">log₃x</text>
          <text x="52" y="32">log₉y</text>
          <text x="80" y="120" font-style="italic">斜率 = −7/8</text>
        </g>
        <circle cx="45" cy="75" r="2.6" fill="currentColor"/>
        <circle cx="225" cy="200" r="2.6" fill="currentColor"/>
      </svg><figcaption>圖：直線過 $(0,\,7)$ 與 $(8,\,0)$；橫軸 $\log_{3}x$、縱軸 $\log_{9}y$</figcaption>''',
 'steps': [
   ('寫出直線方程', ('兩點式', r'縱軸截距 $7$ 即點 $(0,7)$；橫軸截距 $8$ 即點 $(8,0)$。'),
    r'''<p>設 $X=\log_{3}x$、$Y=\log_{9}y$，則</p>
<p>$$Y=-\frac{7}{8}X+7$$</p>'''),
   ('把 $Y$ 換成以 3 為底', ('換底', r'$\log_{9}y=\dfrac{\log_{3}y}{\log_{3}9}=\dfrac{\log_{3}y}{2}$。'),
    r'''<p>$$\frac{\log_{3}y}{2}=-\frac{7}{8}\log_{3}x+7$$</p>
<p>易錯：題目的縱軸是 $\log_{9}y$，若當成 $\log_{3}y$，最後會多出一個 $y$ 的次方（誤選 C）。</p>'''),
   ('乘 2 清分母，再把含對數的項排好', None,
    r'''<p>$$\log_{3}y=-\frac{7}{4}\log_{3}x+14$$</p>
<p>乘 4 並移項：</p>
<p>$$7\log_{3}x+4\log_{3}y=56$$</p>'''),
   ('用對數律合併、還原成指數式', ('對數律', r'$k\log_{3}a=\log_{3}a^{k}$，$\log_{3}A+\log_{3}B=\log_{3}(AB)$，$\log_{3}A=k\iff A=3^{k}$。'),
    r'''<p>$$\log_{3}x^{7}+\log_{3}y^{4}=56\;\Longrightarrow\;\log_{3}(x^{7}y^{4})=56$$</p>
<p>$$x^{7}y^{4}=3^{56}$$</p>'''),
   ('對照選項', None,
    r'''<p>即選項 B。$x$ 的次方是 $7$（縱軸截距）、$y$ 的次方是 $4$（由除以 2 換底而來），與直覺相反。</p>'''),
 ],
 'ans': r'<b>B</b>（$x^{7}y^{4}=3^{56}$）',
 'practice': {
   'q': r'已知 $\log_{4}y$ 是 $\log_{2}x$ 的線性函數，其縱軸截距及橫軸截距分別為 $6$ 及 $4$。下列哪項必定正確？',
   'opts': [r'$x^{3}y=2^{12}$', r'$x^{6}y^{4}=2^{12}$', r'$x^{3}y^{2}=2^{12}$', r'$x^{2}y^{3}=2^{12}$'],
   'steps': [
     r'設 $X=\log_{2}x$、$Y=\log_{4}y$：$Y=-\dfrac{6}{4}X+6=-\dfrac{3}{2}X+6$。',
     r'$\log_{4}y=\dfrac{\log_{2}y}{2}$，故 $\log_{2}y=-3\log_{2}x+12$。',
     r'$3\log_{2}x+\log_{2}y=12\Rightarrow x^{3}y=2^{12}$。',
   ],
   'ans': r'<b>A</b>（$x^{3}y=2^{12}$）',
 },
},
{
 'year': '2019', 'paper': '卷二', 'num': 34,
 'h1': '先化 $i$ 的次方，再做分母實數化',
 'sub': '複數 · 實部與共軛',
 'q': r'''若 $a$ 為實數，則 $\dfrac{4+i^{5}}{a+i}-i^{6}$ 的實部是''',
 'opts': [r'$\dfrac{4a+1}{a^{2}-1}$', r'$\dfrac{4a+1}{a^{2}+1}$', r'$\dfrac{a^{2}+4a+2}{a^{2}-1}$', r'$\dfrac{a^{2}+4a+2}{a^{2}+1}$'],
 'steps': [
   ('化簡 $i$ 的次方', ('$i$ 的週期', r'$i^{2}=-1$，故 $i^{4}=1$，$i^{5}=i$，$i^{6}=-1$。'),
    r'''<p>$$\frac{4+i^{5}}{a+i}-i^{6}=\frac{4+i}{a+i}+1$$</p>'''),
   ('分子分母同乘分母的共軛', ('實數化', r'$\dfrac{1}{a+i}=\dfrac{a-i}{(a+i)(a-i)}=\dfrac{a-i}{a^{2}+1}$。'),
    r'''<p>$$\frac{(4+i)(a-i)}{(a+i)(a-i)}=\frac{4a-4i+ai-i^{2}}{a^{2}+1}=\frac{4a+1+(a-4)i}{a^{2}+1}$$</p>'''),
   ('把 $+1$ 也寫成分母 $a^{2}+1$', None,
    r'''<p>$$1=\frac{a^{2}+1}{a^{2}+1}$$</p>
<p>$$\frac{4a+1+(a-4)i+a^{2}+1}{a^{2}+1}=\frac{a^{2}+4a+2+(a-4)i}{a^{2}+1}$$</p>'''),
   ('只取實部', None,
    r'''<p>實部 $=\dfrac{a^{2}+4a+2}{a^{2}+1}$，即選項 D。</p>
<p>易錯：$-\,i^{6}$ 等於 $+1$，不是 $-1$；若把它當成 $-1$，分子會少了 $a^{2}+1$。</p>'''),
 ],
 'ans': r'<b>D</b>（$\dfrac{a^{2}+4a+2}{a^{2}+1}$）',
 'practice': {
   'q': r'若 $a$ 為實數，則 $\dfrac{3+i^{7}}{a+i}-i^{4}$ 的實部是',
   'opts': [r'$\dfrac{3a-1}{a^{2}+1}$', r'$\dfrac{-a^{2}+3a-2}{a^{2}+1}$', r'$\dfrac{a^{2}+3a-2}{a^{2}+1}$', r'$\dfrac{3a-1}{a^{2}-1}$'],
   'steps': [
     r'$i^{7}=-i$，$i^{4}=1$，故原式 $=\dfrac{3-i}{a+i}-1$。',
     r'$\dfrac{(3-i)(a-i)}{a^{2}+1}=\dfrac{3a-1-(3+a)i}{a^{2}+1}$。',
     r'減 $1=\dfrac{a^{2}+1}{a^{2}+1}$：實部 $=\dfrac{3a-1-a^{2}-1}{a^{2}+1}=\dfrac{-a^{2}+3a-2}{a^{2}+1}$。',
   ],
   'ans': r'<b>B</b>（$\dfrac{-a^{2}+3a-2}{a^{2}+1}$）',
 },
},
]
