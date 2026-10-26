# -*- coding: utf-8 -*-
# 2018 卷二 Q17–Q24
QUESTIONS = [
{
 'year': '2018', 'paper': '卷二', 'num': 17,
 'h1': '圓心到弦的垂線：先找半徑，再找圓心角',
 'sub': '求積法 · 扇形面積',
 'q': r'''圖中 $O$ 是扇形 $OABCD$ 的圓心。$AD$ 與 $OC$ 互相垂直，並相交於 $E$。$F$ 是 $AD$ 上的一點，使 $BF\perp AD$。若 $AF=9\text{ cm}$、$DF=39\text{ cm}$ 及 $OE=18\text{ cm}$，則扇形 $OBC$ 的面積是''',
 'opts': [r'$48\pi\text{ cm}^{2}$', r'$75\pi\text{ cm}^{2}$', r'$96\pi\text{ cm}^{2}$', r'$150\pi\text{ cm}^{2}$'],
 'fig': r'''<img src="figures/2018_P2_17.png" alt="扇形 OABCD 與弦 AD" style="max-width:100%;height:auto;"><figcaption>圖：$OC\perp AD$ 於 $E$，$BF\perp AD$ 於 $F$</figcaption>''',
 'steps': [
   ('圓心到弦的垂線平分弦', ('垂徑定理', r'由圓心向弦作垂線，必平分該弦。'),
    r'''<p>$$AE=DE=\frac{AD}{2}=\frac{9+39}{2}=24\text{ cm}$$</p>'''),
   ('在 $\triangle OAE$ 求半徑', ('畢氏定理', r'$OA^{2}=AE^{2}+OE^{2}$。'),
    r'''<p>$$OA=\sqrt{24^{2}+18^{2}}=\sqrt{576+324}=\sqrt{900}=30\text{ cm}$$</p>
<p>故扇形半徑 $r=30\text{ cm}$。</p>'''),
   ('求 $EF$，再搬到 $BG$', ('矩形', r'過 $B$ 作 $BG\perp OC$，則 $BGEF$ 是矩形，$BG=EF$。'),
    r'''<p>$$EF=AE-AF=24-9=15\text{ cm}\;\Rightarrow\;BG=15\text{ cm}$$</p>'''),
   ('在 $\triangle OBG$ 求圓心角', ('正弦', r'在直角三角形中 $\sin\theta=\dfrac{\text{對邊}}{\text{斜邊}}$。'),
    r'''<p>$$\sin\angle BOG=\frac{BG}{OB}=\frac{15}{30}=\frac{1}{2}\;\Rightarrow\;\angle BOG=30^{\circ}$$</p>
<p>即 $\angle BOC=30^{\circ}$。</p>'''),
   ('代扇形面積公式', ('扇形面積', r'$A=\dfrac{\theta}{360^{\circ}}\pi r^{2}$。'),
    r'''<p>$$A=\frac{30}{360}\pi(30)^{2}=\frac{1}{12}\times900\pi=75\pi\text{ cm}^{2}$$</p>'''),
 ],
 'ans': r'<b>B</b>（$75\pi\text{ cm}^{2}$）',
 'practice': {
   'q': r'一個扇形的半徑為 $15\text{ cm}$，圓心角為 $48^{\circ}$。求它的面積。',
   'opts': [r'$24\pi\text{ cm}^{2}$', r'$30\pi\text{ cm}^{2}$', r'$36\pi\text{ cm}^{2}$', r'$45\pi\text{ cm}^{2}$'],
   'steps': [
     r'扇形面積 $=\dfrac{\theta}{360^{\circ}}\pi r^{2}$。',
     r'$\dfrac{48}{360}=\dfrac{2}{15}$。',
     r'$A=\dfrac{2}{15}\pi(15)^{2}=30\pi\text{ cm}^{2}$。',
   ],
   'ans': r'<b>B</b>（$30\pi\text{ cm}^{2}$）',
 },
},
{
 'year': '2018', 'paper': '卷二', 'num': 18,
 'h1': '菱形＋對稱軸：一對全等三角形就夠',
 'sub': '平面幾何 · 菱形與全等三角形',
 'q': r'''圖中 $ABCD$ 是菱形。$E$、$F$ 分別在 $AB$、$AD$ 上，使 $AE=AF$ 及 $\angle ECF=42^{\circ}$。若 $\angle BAD=110^{\circ}$，則 $\angle BEC=$''',
 'opts': [r'$70^{\circ}$', r'$76^{\circ}$', r'$80^{\circ}$', r'$84^{\circ}$'],
 'fig': r'''<img src="figures/2018_P2_18.png" alt="菱形 ABCD，E 在 AB、F 在 AD" style="max-width:100%;height:auto;"><figcaption>圖：$AE=AF$，$\angle ECF=42^{\circ}$，$\angle BAD=110^{\circ}$</figcaption>''',
 'steps': [
   ('對角線 $AC$ 平分 $\angle BAD$', ('菱形性質', r'菱形的對角線平分對角。'),
    r'''<p>$$\angle CAE=\angle CAF=\frac{110^{\circ}}{2}=55^{\circ}$$</p>'''),
   ('證明 $\triangle ACE\cong\triangle ACF$', ('S.A.S.', r'$AC$ 公共、$\angle CAE=\angle CAF$、$AE=AF$。'),
    r'''<p>$$\therefore\ \triangle ACE\cong\triangle ACF\quad(\text{S.A.S.})$$</p>'''),
   ('對應角相等，平分 $\angle ECF$', None,
    r'''<p>$$\angle ACE=\angle ACF=\frac{42^{\circ}}{2}=21^{\circ}$$</p>'''),
   ('在 $\triangle ACE$ 求 $\angle AEC$，再取補角', ('三角形內角和', r'三角形三角之和 $=180^{\circ}$。'),
    r'''<p>$$\angle AEC=180^{\circ}-55^{\circ}-21^{\circ}=104^{\circ}$$</p>
<p>$A$、$E$、$B$ 在同一直線上，故</p>
<p>$$\angle BEC=180^{\circ}-104^{\circ}=76^{\circ}$$</p>'''),
 ],
 'ans': r'<b>B</b>（$76^{\circ}$）',
 'practice': {
   'q': r'圖中 $PQRS$ 是菱形，$T$、$U$ 分別在 $PQ$、$PS$ 上，使 $PT=PU$ 及 $\angle TRU=50^{\circ}$。若 $\angle SPQ=80^{\circ}$，求 $\angle TUR$。',
   'opts': [r'$65^{\circ}$', r'$70^{\circ}$', r'$75^{\circ}$', r'$80^{\circ}$'],
   'steps': [
     r'$PR$ 平分 $\angle SPQ$，故 $\angle TPR=\angle UPR=40^{\circ}$。',
     r'$\triangle PTR\cong\triangle PUR$（S.A.S.）$\Rightarrow\angle PRT=\angle PRU=25^{\circ}$。',
     r'$\angle PUT=180^{\circ}-40^{\circ}-25^{\circ}=115^{\circ}$，故 $\angle TUR=65^{\circ}$。',
   ],
   'ans': r'<b>A</b>（$65^{\circ}$）',
 },
},
{
 'year': '2018', 'paper': '卷二', 'num': 19,
 'h1': '正五邊形的對稱軸：三句一次過判斷',
 'sub': '平面幾何 · 正多邊形',
 'q': r'''圖中 $ABCDE$ 是正五邊形，$AD$ 與 $CE$ 相交於 $F$。下列何者正確？
<br>I. $\triangle ABF\cong\triangle CBF$
<br>II. $\angle AFB+\angle EAF=90^{\circ}$
<br>III. $AC\perp BF$''',
 'opts': ['只有 I 及 II', '只有 I 及 III', '只有 II 及 III', 'I、II 及 III'],
 'fig': r'''<img src="figures/2018_P2_19.png" alt="正五邊形 ABCDE，對角線 AD 與 CE 交於 F" style="max-width:100%;height:auto;"><figcaption>圖：$F$ 為 $AD$ 與 $CE$ 的交點</figcaption>''',
 'steps': [
   ('先算正五邊形的內角', ('正多邊形', r'每個內角 $=\dfrac{(n-2)\times180^{\circ}}{n}$。'),
    r'''<p>$$\text{內角}=\frac{3\times180^{\circ}}{5}=108^{\circ}$$</p>
<p>在等腰 $\triangle ADE$ 中（$AE=ED$）：</p>
<p>$$\angle EAD=\angle ADE=\frac{180^{\circ}-108^{\circ}}{2}=36^{\circ}$$</p>
<p>故 $\angle BAD=108^{\circ}-36^{\circ}=72^{\circ}$。</p>'''),
   ('找出 $BF$ 是對稱軸', ('對稱', r'正五邊形有一條對稱軸經過 $B$，並把 $A\leftrightarrow C$、$D\leftrightarrow E$ 對調。'),
    r'''<p>$AD$ 與 $CE$ 在這對稱下互相對調，所以交點 $F$ 被固定在對稱軸上，即 $BF$ 就是這條對稱軸。</p>
<p>因此 $\angle ABF=\dfrac{108^{\circ}}{2}=54^{\circ}$。</p>'''),
   ('檢驗 I：用 S.S.S.', None,
    r'''<p>$AB=CB$（正五邊形邊長）、$AF=CF$（對稱）、$BF$ 公共，故</p>
<p>$$\triangle ABF\cong\triangle CBF\quad(\text{S.S.S.})$$</p>
<p>I 正確。</p>'''),
   ('檢驗 II：在 $\triangle ABF$ 求 $\angle AFB$', None,
    r'''<p>$$\angle AFB=180^{\circ}-72^{\circ}-54^{\circ}=54^{\circ}$$</p>
<p>而 $\angle EAF=\angle EAD=36^{\circ}$，故</p>
<p>$$54^{\circ}+36^{\circ}=90^{\circ}$$</p>
<p>II 正確。</p>'''),
   ('檢驗 III：對稱軸垂直連線', None,
    r'''<p>$A$ 與 $C$ 關於 $BF$ 對稱，所以 $AC\perp BF$，III 正確。</p>
<p>三句都正確。</p>'''),
 ],
 'ans': r'<b>D</b>（I、II 及 III）',
 'practice': {
   'q': r'''圖中 $PQRST$ 是正五邊形，$PR$ 與 $QS$ 相交於 $X$。下列何者正確？
<br>I. $PQ=QR$
<br>II. $\angle PXQ=72^{\circ}$
<br>III. $PX=QX$''',
   'opts': ['只有 I 及 II', '只有 I 及 III', '只有 II 及 III', 'I、II 及 III'],
   'steps': [
     r'正五邊形邊長相等，I 正確。',
     r'$\angle PQS=\angle QPR=36^{\circ}$，故 $\triangle PQX$ 中 $\angle PXQ=180^{\circ}-72^{\circ}=108^{\circ}$，II 錯誤。',
     r'$\angle QPR=\angle PQS=36^{\circ}$，故 $PX=QX$，III 正確。',
   ],
   'ans': r'<b>B</b>（只有 I 及 III）',
 },
},
{
 'year': '2018', 'paper': '卷二', 'num': 20,
 'h1': '正方形外接一點：一條平行線造出相似三角形',
 'sub': '平面幾何 · 相似三角形',
 'q': r'''圖中 $ABCD$ 是正方形。$E$ 是 $AB$ 延長線上的一點，使 $BE=4\text{ cm}$。$BC$ 與 $DE$ 相交於 $F$。若 $EF=5\text{ cm}$，則 $DF=$''',
 'opts': [r'$9\text{ cm}$', r'$10\text{ cm}$', r'$12\text{ cm}$', r'$15\text{ cm}$'],
 'fig': r'''<img src="figures/2018_P2_20.png" alt="正方形 ABCD，E 在 AB 延長線上" style="max-width:100%;height:auto;"><figcaption>圖：$BE=4\text{ cm}$，$EF=5\text{ cm}$，$BC$ 與 $DE$ 交於 $F$</figcaption>''',
 'steps': [
   ('先求 $BF$', ('直角', r'正方形中 $BC\perp AB$，故 $\angle EBF=90^{\circ}$。'),
    r'''<p>$$BF=\sqrt{EF^{2}-BE^{2}}=\sqrt{25-16}=3\text{ cm}$$</p>'''),
   ('找相似三角形', ('平行線', r'$ABCD$ 是正方形，故 $AD\parallel BC$，即 $AD\parallel BF$。'),
    r'''<p>在 $\triangle EAD$ 中，$B$ 在 $EA$ 上、$F$ 在 $ED$ 上，且 $BF\parallel AD$，故</p>
<p>$$\triangle EBF\sim\triangle EAD$$</p>'''),
   ('用邊比求正方形邊長', ('相似比', r'$\dfrac{EB}{EA}=\dfrac{BF}{AD}$。'),
    r'''<p>設邊長 $AD=AB=s$，則 $EA=s+4$：</p>
<p>$$\frac{4}{s+4}=\frac{3}{s}\;\Rightarrow\;4s=3s+12\;\Rightarrow\;s=12$$</p>'''),
   ('用同一相似比求 $DF$', None,
    r'''<p>$$\frac{EF}{ED}=\frac{EB}{EA}=\frac{4}{16}=\frac{1}{4}$$</p>
<p>故 $ED=4\times5=20$，$DF=ED-EF=20-5=15\text{ cm}$。</p>'''),
 ],
 'ans': r'<b>B</b>（$15\text{ cm}$）',
 'practice': {
   'q': r'圖中 $PQRS$ 是正方形，$T$ 在 $PQ$ 延長線上使 $QT=8\text{ cm}$。$QR$ 與 $TS$ 交於 $U$。若 $TU=10\text{ cm}$，求 $SU$。',
   'opts': [r'$24\text{ cm}$', r'$28\text{ cm}$', r'$30\text{ cm}$', r'$36\text{ cm}$'],
   'steps': [
     r'$QU=\sqrt{10^{2}-8^{2}}=6$（$\angle TQU=90^{\circ}$）。',
     r'$SR\parallel QT$，故 $\triangle UQT\sim\triangle USR$，$\dfrac{QT}{SR}=\dfrac{QU}{UR}$。設邊長 $s$：$\dfrac{8}{s}=\dfrac{6}{s-6}$。',
     r'解得 $8s-48=6s$，$s=24$；再由 $\dfrac{TU}{US}=\dfrac{8}{24}=\dfrac{1}{3}$ 得 $US=30\text{ cm}$。',
   ],
   'ans': r'<b>C</b>（$30\text{ cm}$）',
 },
},
{
 'year': '2018', 'paper': '卷二', 'num': 21,
 'h1': '梯形三等分：把三條等式逐條驗證',
 'sub': '三角學 · 直角三角形中的比',
 'q': r'''圖中 $ABCD$ 是梯形，$\angle ABC=\angle BAD=90^{\circ}$。$E$、$F$ 是 $AB$ 上的點，把 $AB$ 分成三等份。下列何者必定正確？
<br>I. $AF\sin\alpha=BE\sin\beta$
<br>II. $CE\cos\alpha=DF\cos\beta$
<br>III. $AD\tan\alpha=BC\tan\beta$''',
 'opts': ['只有 I 及 II', '只有 I 及 III', '只有 II 及 III', 'I、II 及 III'],
 'fig': r'''<img src="figures/2018_P2_21.png" alt="梯形 ABCD，E、F 把 AB 三等分" style="max-width:100%;height:auto;"><figcaption>圖：$\angle ABC=\angle BAD=90^{\circ}$，$\alpha$ 在 $E$、$\beta$ 在 $F$</figcaption>''',
 'steps': [
   ('把三等份寫成代數', ('三等分', r'設 $AE=EF=FB=x$。'),
    r'''<p>$$AF=AE+EF=2x,\qquad BE=EF+FB=2x$$</p>
<p>即 $AF=BE=2x$，這是三條式子的共同基礎。</p>'''),
   ('寫出四個三角比', ('直角三角形', r'$\sin=\dfrac{\text{對}}{{\text{斜}}}$、$\cos=\dfrac{\text{鄰}}{{\text{斜}}}$、$\tan=\dfrac{\text{對}}{\text{鄰}}$。'),
    r'''<p>在 $\triangle BCE$（直角在 $B$）：$\sin\alpha=\dfrac{BC}{CE}$、$\cos\alpha=\dfrac{BE}{CE}$、$\tan\alpha=\dfrac{BC}{BE}$。</p>
<p>在 $\triangle ADF$（直角在 $A$）：$\sin\beta=\dfrac{AD}{DF}$、$\cos\beta=\dfrac{AF}{DF}$、$\tan\beta=\dfrac{AD}{AF}$。</p>'''),
   ('檢驗 II', None,
    r'''<p>$$CE\cos\alpha=CE\cdot\frac{BE}{CE}=BE=2x$$</p>
<p>$$DF\cos\beta=DF\cdot\frac{AF}{DF}=AF=2x$$</p>
<p>兩者相等，II 必定正確。</p>'''),
   ('檢驗 III', None,
    r'''<p>$$AD\tan\alpha=AD\cdot\frac{BC}{BE}=\frac{AD\cdot BC}{2x}$$</p>
<p>$$BC\tan\beta=BC\cdot\frac{AD}{AF}=\frac{BC\cdot AD}{2x}$$</p>
<p>兩者相等，III 必定正確。</p>'''),
   ('檢驗 I', None,
    r'''<p>$$AF\sin\alpha=2x\cdot\frac{BC}{CE},\qquad BE\sin\beta=2x\cdot\frac{AD}{DF}$$</p>
<p>一般情況下 $\dfrac{BC}{CE}\neq\dfrac{AD}{DF}$，故 I 不一定成立。</p>'''),
 ],
 'ans': r'<b>C</b>（只有 II 及 III）',
 'practice': {
   'q': r'圖中 $PQRS$ 是梯形，$\angle PQR=\angle QPS=90^{\circ}$。$T$、$U$ 把 $PQ$ 分成三等份（$PT=TU=UQ$）。若 $\angle QRT=\theta$、$\angle USP=\phi$，下列何者必定正確？',
   'opts': [r'$PS\tan\theta=QR\tan\phi$', r'$PT\sin\theta=QU\sin\phi$', r'$RT\cos\theta=SU\cos\phi$', r'$PS\sin\phi=QR\sin\theta$'],
   'steps': [
     r'設每份為 $x$，則 $QU=x$、$PT=x$，而 $QT=2x$、$PU=2x$。',
     r'$\tan\theta=\dfrac{QR}{QT}=\dfrac{QR}{2x}$，$\tan\phi=\dfrac{PS}{PU}=\dfrac{PS}{2x}$。',
     r'故 $PS\tan\theta=\dfrac{PS\cdot QR}{2x}=QR\tan\phi$，選 A。',
   ],
   'ans': r'<b>A</b>（$PS\tan\theta=QR\tan\phi$）',
 },
},
{
 'year': '2018', 'paper': '卷二', 'num': 22,
 'h1': '圓內接四邊形＋等腰三角形：一直設 $x$ 就通',
 'sub': '平面幾何 · 圓與等腰三角形',
 'q': r'''圖中 $ABCD$ 是一個圓。$AD$ 延長與 $BC$ 延長相交於 $E$。已知 $BD=DE$、$\angle BAC=66^{\circ}$ 及 $\angle ABD=30^{\circ}$，求 $\angle CED$。''',
 'opts': [r'$18^{\circ}$', r'$28^{\circ}$', r'$22^{\circ}$', r'$20^{\circ}$'],
 'fig': r'''<img src="figures/2018_P2_22.png" alt="圓 ABCD，AD 與 BC 延長交於 E" style="max-width:100%;height:auto;"><figcaption>圖：$BD=DE$，$\angle BAC=66^{\circ}$，$\angle ABD=30^{\circ}$</figcaption>''',
 'steps': [
   ('設 $\angle CED=x$', None,
    r'''<p>$E$ 在 $AD$ 及 $BC$ 的延長線上，故 $\angle CED$ 就是 $\triangle BDE$ 在 $E$ 的角。</p>'''),
   ('等腰三角形給出 $x$', ('等腰三角形底角', r'$BD=DE\Rightarrow\angle EBD=\angle BED=x$。'),
    r'''<p>$$\angle EBD=\angle BED=x$$</p>
<p>又 $E$、$C$、$B$ 共線，故 $\angle CBD=x$。</p>'''),
   ('同弓形內的圓周角', ('同弓形', r'$\angle CAD$ 與 $\angle CBD$ 同時對着弦 $CD$。'),
    r'''<p>$$\angle CAD=\angle CBD=x$$</p>'''),
   ('在 $\triangle ABE$ 用內角和', ('三角形內角和', r'三個角相加 $=180^{\circ}$。'),
    r'''<p>$$\angle ABE=\angle ABD+\angle DBE=30^{\circ}+x$$</p>
<p>$$\angle BAE=\angle BAC+\angle CAE=66^{\circ}+x$$</p>
<p>$$(30^{\circ}+x)+(66^{\circ}+x)+x=180^{\circ}$$</p>
<p>$$3x=84^{\circ}\;\Rightarrow\;x=28^{\circ}$$</p>'''),
 ],
 'ans': r'<b>B</b>（$28^{\circ}$）',
 'practice': {
   'q': r'圖中 $PQRS$ 是一個圓。$PQ$ 延長與 $SR$ 延長相交於 $T$。已知 $QR=RT$、$\angle PRS=58^{\circ}$ 及 $\angle QPR=26^{\circ}$，求 $\angle QTR$。',
   'opts': [r'$26^{\circ}$', r'$28^{\circ}$', r'$30^{\circ}$', r'$32^{\circ}$'],
   'steps': [
     r'設 $\angle QTR=y$；$QR=RT\Rightarrow\angle RQT=\angle QTR=y$。',
     r'同弓形：$\angle QSR=\angle QPR=26^{\circ}$，故 $\angle PQS=\angle PRS=58^{\circ}$。',
     r'在 $\triangle PQT$：$(58^{\circ}+y)+(26^{\circ}+y)+y=180^{\circ}\Rightarrow3y=96^{\circ}\Rightarrow y=32^{\circ}$。',
   ],
   'ans': r'<b>D</b>（$32^{\circ}$）',
 },
},
{
 'year': '2018', 'paper': '卷二', 'num': 23,
 'h1': '旋轉對稱重數：數 360° 內重合幾次',
 'sub': '變換與對稱 · 旋轉對稱',
 'q': r'''下圖由八個大小相同的正方形組成。該圖形的旋轉對稱重數是''',
 'opts': [r'$2$', r'$4$', r'$6$', r'$8$'],
 'fig': r'''<img src="figures/2018_P2_23.png" alt="由八個正方形組成的圖形" style="max-width:320px;height:auto;"><figcaption>圖：八個全等正方形；$O$ 為中心</figcaption>''',
 'steps': [
   ('先找旋轉中心', ('旋轉對稱', r'圖形繞某一點旋轉 $\theta$ 後能與原圖完全重合，該點就是旋轉中心。'),
    r'''<p>唯一可能的中心是圖形中央的 $O$：繞 $O$ 轉動時，八個正方形才可能逐格對應回本身。</p>'''),
   ('測試 90°', None,
    r'''<p>繞 $O$ 旋轉 $90^{\circ}$，四個方向的方塊互相對應，圖形與原圖完全重合。</p>'''),
   ('測試更小的角（45°）', None,
    r'''<p>旋轉 $45^{\circ}$ 後，方塊會落在原本沒有方塊的位置（例如對角空隙），不能重合。</p>'''),
   ('重數＝360° ÷ 最小重合角', ('重數', r'若最小重合角為 $\theta$，重數 $=\dfrac{360^{\circ}}{\theta}$。'),
    r'''<p>$$\frac{360^{\circ}}{90^{\circ}}=4$$</p>'''),
 ],
 'ans': r'<b>B</b>（$4$）',
 'practice': {
   'q': r'一個正方形被兩條對角線分成四個三角形，並把其中一組對頂三角形塗色。該塗色圖形的旋轉對稱重數是',
   'opts': [r'$2$', r'$4$', r'$1$', r'$8$'],
   'steps': [
     r'繞中心旋轉 180° 時，兩個塗色三角形互換位置，圖形重合。',
     r'旋轉 90° 時，塗色部分會轉到未塗色的位置，不重合。',
     r'重數 $=\dfrac{360^{\circ}}{180^{\circ}}=2$。',
   ],
   'ans': r'<b>A</b>（$2$）',
 },
},
{
 'year': '2018', 'paper': '卷二', 'num': 24,
 'h1': '極坐標：角度差決定三角形形狀',
 'sub': '座標幾何 · 極坐標',
 'q': r'''點 $C$、$D$、$E$ 的極坐標分別為 $(16,127^{\circ})$、$(12,217^{\circ})$ 及 $(5,307^{\circ})$。求 $\triangle CDE$ 的周界。''',
 'opts': [r'$54$', r'$78$', r'$126$', r'$130$'],
 'steps': [
   ('比較極角，找出直角', ('極坐標', r'$(r,\theta)$ 中 $r$ 是與 $O$ 的距離，$\theta$ 是由正 $x$ 軸量起的角。'),
    r'''<p>$$\angle COD=217^{\circ}-127^{\circ}=90^{\circ}$$</p>
<p>故 $\triangle COD$ 在 $O$ 成直角。</p>'''),
   ('求 $CD$', ('畢氏定理', r'$CD^{2}=OC^{2}+OD^{2}$。'),
    r'''<p>$$CD=\sqrt{16^{2}+12^{2}}=\sqrt{256+144}=20$$</p>'''),
   ('求 $DE$', None,
    r'''<p>$$\angle DOE=307^{\circ}-217^{\circ}=90^{\circ}\;\Rightarrow\;DE=\sqrt{12^{2}+5^{2}}=13$$</p>'''),
   ('求 $CE$：三點共線', None,
    r'''<p>$$\angle COE=307^{\circ}-127^{\circ}=180^{\circ}$$</p>
<p>故 $C$、$O$、$E$ 在同一直線上，$CE=16+5=21$。</p>'''),
   ('相加', None,
    r'''<p>$$\text{周界}=20+13+21=54$$</p>'''),
 ],
 'ans': r'<b>A</b>（$54$）',
 'practice': {
   'q': r'點 $P$、$Q$、$R$ 的極坐標分別為 $(8,40^{\circ})$、$(6,130^{\circ})$ 及 $(15,310^{\circ})$。求 $\triangle PQR$ 的周界。',
   'opts': [r'$42$', r'$46$', r'$48$', r'$50$'],
   'steps': [
     r'$\angle POQ=90^{\circ}\Rightarrow PQ=\sqrt{8^{2}+6^{2}}=10$。',
     r'$\angle QOR=180^{\circ}\Rightarrow QR=6+15=21$；$\angle POR=270^{\circ}$ 即 $90^{\circ}$，$PR=\sqrt{8^{2}+15^{2}}=17$。',
     r'周界 $=10+21+17=48$。',
   ],
   'ans': r'<b>C</b>（$48$）',
 },
},
]
