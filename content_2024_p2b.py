#!/usr/bin/env python3
# 2024 卷二 Q16–Q30
P2_B = [
{'n':16,'title':'DSE 2024 卷二 Q16 · 柱體與錐體體積','tag':'DSE 2024 · 卷二 · Q16',
 'h1':'體積比中要先處理 $\\frac{1}{3}$','sub':'求積法 · 1 分題','marks':'1 分',
 'q':'一直立圓柱體的高與一直立圓錐體的高之比為 $32:15$，而該圓柱體的體積與該圓錐體的體積之比為 $10:9$。若該圓柱體的底半徑為 $25$ cm，則該圓錐體的底半徑為',
 'opts':['$20$ cm','$24$ cm','$48$ cm','$60$ cm'],
 'steps':[
  {'tag':'第 1 步','title':'設高與半徑','rule':('體積','$V_{\\text{柱}}=\\pi r^{2}h$，$V_{\\text{錐}}=\\dfrac{1}{3}\\pi r^{2}h$','錐體要乘 $\\frac{1}{3}$。'),
   'body':'<p>設柱高 $32k$、錐高 $15k$，錐底半徑 $r$：</p><p>$V_{\\text{柱}}=\\pi(25)^{2}(32k)=20000\\pi k$；$V_{\\text{錐}}=\\dfrac{1}{3}\\pi r^{2}(15k)=5\\pi r^{2}k$。</p>'},
  {'tag':'第 2 步','title':'用體積比','body':'<p>$\\dfrac{20000\\pi k}{5\\pi r^{2}k}=\\dfrac{10}{9}\\Rightarrow \\dfrac{4000}{r^{2}}=\\dfrac{10}{9}\\Rightarrow r^{2}=3600\\Rightarrow r=60$ cm，故選 D。</p>'}],
 'ans':'D　$60$ cm'},

{'n':17,'title':'DSE 2024 卷二 Q17 · 正方形內的相似三角形','tag':'DSE 2024 · 卷二 · Q17',
 'h1':'先由相似比定出 $k$，再算面積','sub':'平面幾何 · 面積比 · 1 分題','marks':'1 分',
 'q':'圖中，$ABCD$ 為一正方形。設 $M$ 為 $BC$ 的中點，$E$ 為 $AD$ 上的一點使得 $AE:ED=3:1$，$F$ 為 $BC$ 的延線上的一點使得 $EF\\parallel AM$，$CD$ 與 $EF$ 相交於點 $G$，而 $AM$ 與 $BG$ 相交於點 $H$。若 $\\triangle BMH$ 的面積為 $4\\ \\text{cm}^{2}$，則梯形 $AEGH$ 的面積為',
 'opts':['$12\\ \\text{cm}^{2}$','$33\\ \\text{cm}^{2}$','$39\\ \\text{cm}^{2}$','$45\\ \\text{cm}^{2}$'],
 'steps':[
  {'tag':'第 1 步','title':'設邊長並找 $F$','rule':('平行四邊形','$EF\\parallel AM$ 且 $AE\\parallel MF$','$AMFE$ 是平行四邊形，故 $AE=MF$。'),
   'body':'<p>設 $ED=k$，則 $AE=3k$，邊長 $4k$，$BM=MC=2k$。</p><p>由平行四邊形 $AMFE$：$MF=AE=3k$，故 $CF=MF-MC=k$，且 $BF=5k$。</p>'},
  {'tag':'第 2 步','title':'用相似三角形求 $k^{2}$','rule':('相似三角形','面積比 $=$ 邊長比$^{2}$','$\\triangle BMH\\sim\\triangle BFG$（$BM\\parallel BF$，$MH\\parallel FG$）。'),
   'body':'<p>$\\dfrac{[BMH]}{[BFG]}=\\left(\\dfrac{BM}{BF}\\right)^{2}=\\left(\\dfrac{2}{5}\\right)^{2}=\\dfrac{4}{25}$，故 $[BFG]=25$。</p><p>又 $\\triangle GDE\\cong\\triangle GCF$，得 $DG=GC=2k$，所以 $G$ 到 $BC$ 的高為 $2k$。</p><p>$[BFG]=\\dfrac{1}{2}(5k)(2k)=5k^{2}=25\\Rightarrow k^{2}=5$。</p>'},
  {'tag':'第 3 步','title':'以坐標計算 $AEGH$','body':'<p>取 $B(0,0)$、$M(2k,0)$、$G(4k,2k)$：直線 $AM$ 為 $y=4k-2x$，直線 $BG$ 為 $y=\\dfrac{x}{2}$，解得 $H(1.6k,0.8k)$。</p><p>$[AEGH]=[ABGE]-[\\triangle ABH]=11k^{2}-3.2k^{2}=7.8k^{2}=7.8(5)=39\\ \\text{cm}^{2}$，故選 C。</p>'}],
 'ans':'C　$39\\ \\text{cm}^{2}$'},

{'n':18,'title':'DSE 2024 卷二 Q18 · 畢氏定理逆定理','tag':'DSE 2024 · 卷二 · Q18',
 'h1':'先證直角，再逐邊求長度','sub':'平面幾何 · 1 分題','marks':'1 分',
 'q':'圖中，$ABC$ 為一直線。已知 $AD=37$ cm、$BC=5$ cm、$BD=12$ cm、$CD=13$ cm 及 $CE=9$ cm。若 $\\angle ACE=90^{\\circ}$，求四邊形 $ADCE$ 的周界。',
 'opts':['$76$ cm','$90$ cm','$100$ cm','$180$ cm'],
 'steps':[
  {'tag':'第 1 步','title':'證明 $\\angle CBD=90^{\\circ}$','rule':('畢氏定理逆定理','$5^{2}+12^{2}=13^{2}$','三邊符合畢氏關係，故為直角三角形。'),
   'body':'<p>$BC^{2}+BD^{2}=25+144=169=CD^{2}$，故 $\\angle CBD=90^{\\circ}$，從而 $\\angle ABD=90^{\\circ}$（$A$、$B$、$C$ 共線）。</p>'},
  {'tag':'第 2 步','title':'求 $AB$ 與 $AC$','body':'<p>$AB=\\sqrt{37^{2}-12^{2}}=\\sqrt{1225}=35$，故 $AC=5+35=40$。</p>'},
  {'tag':'第 3 步','title':'求 $AE$ 與周界','body':'<p>$AE=\\sqrt{40^{2}+9^{2}}=\\sqrt{1681}=41$。</p><p>周界 $=37+13+9+41=100$ cm，故選 C。</p>'}],
 'ans':'C　$100$ cm'},

{'n':19,'title':'DSE 2024 卷二 Q19 · 平行線與折線角','tag':'DSE 2024 · 卷二 · Q19',
 'h1':'每遇轉折，加一條平行線','sub':'平行線 · 角 · 1 分題','marks':'1 分',
 'q':'根據圖中所示，下列何者必為正確？',
 'opts':['$p+q-r=90^{\\circ}$','$p-r+s=180^{\\circ}$','$p+q-r+s=270^{\\circ}$','$p+q+r-s=540^{\\circ}$'],
 'steps':[
  {'tag':'第 1 步','title':'作輔助平行線','rule':('內錯角／同旁內角','兩平行線被截線所截','在每個轉折點作與已知平行線平行的直線。'),
   'body':'<p>在 $q$ 及 $r$ 的頂點分別作平行線，便可把折線角化為同旁內角（互補，和為 $180^{\\circ}$）。</p>'},
  {'tag':'第 2 步','title':'把反角寫成 $360^{\\circ}-$','body':'<p>$p$ 與 $r$ 皆為反角（大於 $180^{\\circ}$），處理時寫成 $360^{\\circ}-p$、$360^{\\circ}-r$，再用同旁內角相加。</p>'},
  {'tag':'第 3 步','title':'整理','body':'<p>由兩組同旁內角相加得 $p+q+r-s=540^{\\circ}$，故選 D。</p>'}],
 'ans':'D　$p+q+r-s=540^{\\circ}$'},

{'n':20,'title':'DSE 2024 卷二 Q20 · 正多邊形性質','tag':'DSE 2024 · 卷二 · Q20',
 'h1':'先由內角和定邊數','sub':'多邊形 · 對稱 · 1 分題','marks':'1 分',
 'q':'若一正多邊形的內角和為 $900^{\\circ}$，則下列何者正確？<br>I. 該多邊形的對角線數目為 $7$。<br>II. 該多邊形的旋轉對稱的折數為 $7$。<br>III. 該多邊形的反射對稱軸的數目為 $7$。',
 'opts':['只有 I','只有 II','只有 I 及 III','只有 II 及 III'],
 'steps':[
  {'tag':'第 1 步','title':'求邊數','rule':('內角和','$(n-2)\\times180^{\\circ}$','正多邊形同樣適用。'),
   'body':'<p>$(n-2)180=900\\Rightarrow n-2=5\\Rightarrow n=7$，即正七邊形。</p>'},
  {'tag':'第 2 步','title':'檢查 I','body':'<p>對角線數目 $=\\dfrac{7(7-3)}{2}=14\\ne7$，I 錯誤。</p>'},
  {'tag':'第 3 步','title':'檢查 II、III','body':'<p>正 $n$ 邊形的旋轉對稱折數及反射對稱軸數目皆為 $n$，故 II、III 皆正確，答案為 D。</p>'}],
 'ans':'D　只有 II 及 III'},

{'n':21,'title':'DSE 2024 卷二 Q21 · 菱形與矩形','tag':'DSE 2024 · 卷二 · Q21',
 'h1':'角度追蹤找出等腰三角形','sub':'平面幾何 · 全等 · 1 分題','marks':'1 分',
 'q':'圖中，$ABCD$ 為一菱形。將 $AC$ 與 $BD$ 的交點記為 $E$。設 $F$ 為一點使得 $BH\\parallel EF$ 且 $CFHG$ 為一矩形，其中 $G$ 及 $H$ 分別為 $AC$ 的延線及 $BC$ 的延線上的點。將 $CD$ 與 $EF$ 的交點記為 $I$。下列何者必為正確？<br>I. $CI=FI$<br>II. $\\angle ABE=\\angle GCH$<br>III. $\\triangle ADE\\cong\\triangle HCF$',
 'opts':['只有 I 及 II','只有 I 及 III','只有 II 及 III','I、II 及 III'],
 'steps':[
  {'tag':'第 1 步','title':'處理 I','rule':('內錯角','$DE\\parallel FC$','菱形對角線互相垂直，矩形對邊平行。'),
   'body':'<p>由 $DE\\parallel FC$ 及菱形對角線平分頂角，可證 $\\angle IFC=\\angle ICF$，故 $CI=FI$，I 正確。</p>'},
  {'tag':'第 2 步','title':'處理 II','body':'<p>設 $\\angle ABE=x$，則 $\\angle BCE=90^{\\circ}-x$，而 $\\angle GCH=\\angle BCE=90^{\\circ}-x\\ne x$（一般情況），II 不必然正確。</p>'},
  {'tag':'第 3 步','title':'處理 III','body':'<p>先證 $\\triangle DEC\\cong\\triangle FCE$（AAS）得 $DE=FC$，再配合 $\\angle DAE=\\angle CHF$ 及 $\\angle DEA=\\angle CFH=90^{\\circ}$，得 $\\triangle ADE\\cong\\triangle HCF$（AAS），III 正確。</p><p>故答案為 B。</p>'}],
 'ans':'B　只有 I 及 III'},

{'n':22,'title':'DSE 2024 卷二 Q22 · 圓內兩弦相交','tag':'DSE 2024 · 卷二 · Q22',
 'h1':'先找圓心，再算各段弧','sub':'圓形性質 · 1 分題','marks':'1 分',
 'q':'圖中，$ABCDE$ 為一圓。$AC$ 及 $BE$ 均為該圓的直徑。設 $P$ 為 $AC$ 與 $BD$ 的交點。若 $\\angle ABE=46^{\\circ}$ 及 $\\angle DBE=16^{\\circ}$，則 $\\angle APD=$',
 'opts':['$104^{\\circ}$','$108^{\\circ}$','$120^{\\circ}$','$135^{\\circ}$'],
 'steps':[
  {'tag':'第 1 步','title':'求弧 $AB$ 與弧 $BC$','rule':('圓周角','圓周角 $=\\dfrac{1}{2}$ 所對弧','$\\angle ABE$ 對弧 $AE$。'),
   'body':'<p>弧 $AE=2(46^{\\circ})=92^{\\circ}$。$BE$ 為直徑，故弧 $AB=180^{\\circ}-92^{\\circ}=88^{\\circ}$；$AC$ 亦為直徑，故弧 $BC=180^{\\circ}-88^{\\circ}=92^{\\circ}$。</p>'},
  {'tag':'第 2 步','title':'求弧 $CD$ 與弧 $AD$','body':'<p>$\\angle DBE=16^{\\circ}$ 對弧 $DE=32^{\\circ}$，而弧 $CE=180^{\\circ}-92^{\\circ}=88^{\\circ}$，故弧 $CD=88^{\\circ}-32^{\\circ}=56^{\\circ}$。</p><p>由 $AC$ 為直徑：弧 $AD=180^{\\circ}-56^{\\circ}=124^{\\circ}$。</p>'},
  {'tag':'第 3 步','title':'兩弦相交','rule':('相交弦','$\\angle=\\dfrac{1}{2}(\\text{兩段對頂弧之和})$','$\\angle APD$ 對弧 $AD$ 與弧 $BC$。'),
   'body':'<p>$\\angle APD=\\dfrac{1}{2}(124^{\\circ}+92^{\\circ})=108^{\\circ}$，故選 B。</p>'}],
 'ans':'B　$108^{\\circ}$'},

{'n':23,'title':'DSE 2024 卷二 Q23 · 三角比','tag':'DSE 2024 · 卷二 · Q23',
 'h1':'用 $DC$ 作橋樑','sub':'三角學 · 1 分題','marks':'1 分',
 'q':'圖中，$ABC$ 為一直線。$\\dfrac{BC}{AD}=$',
 'opts':['$\\dfrac{\\sin\\theta}{\\tan\\phi}$','$\\dfrac{\\tan\\phi}{\\sin\\theta}$','$\\dfrac{\\cos\\theta}{\\tan\\phi}$','$\\dfrac{\\tan\\phi}{\\cos\\theta}$'],
 'steps':[
  {'tag':'第 1 步','title':'在 $\\triangle BCD$ 表示 $BC$','rule':('正切','$\\tan\\phi=\\dfrac{DC}{BC}$','$\\angle BCD=90^{\\circ}$。'),
   'body':'<p>$BC=\\dfrac{DC}{\\tan\\phi}$。</p>'},
  {'tag':'第 2 步','title':'在 $\\triangle ACD$ 表示 $AD$','body':'<p>$\\sin\\theta=\\dfrac{DC}{AD}\\Rightarrow AD=\\dfrac{DC}{\\sin\\theta}$。</p>'},
  {'tag':'第 3 步','title':'相除','body':'<p>$\\dfrac{BC}{AD}=\\dfrac{DC/\\tan\\phi}{DC/\\sin\\theta}=\\dfrac{\\sin\\theta}{\\tan\\phi}$，故選 A。</p>'}],
 'ans':'A　$\\dfrac{\\sin\\theta}{\\tan\\phi}$'},

{'n':24,'title':'DSE 2024 卷二 Q24 · 旋轉與反射','tag':'DSE 2024 · 卷二 · Q24',
 'h1':'旋轉 $90^{\\circ}$ 就是 $(x,y)\\to(-y,x)$','sub':'坐標幾何 · 1 分題','marks':'1 分',
 'q':'點 $U$ 的坐標為 $(-3,-8)$。$U$ 繞原點逆時針方向旋轉 $90^{\\circ}$ 至點 $V$，然後 $V$ 對直線 $x=2$ 作反射至點 $W$。求 $W$ 的 $x$ 坐標。',
 'opts':['$-4$','$-3$','$7$','$12$'],
 'steps':[
  {'tag':'第 1 步','title':'旋轉','rule':('逆時針 $90^{\\circ}$','$(x,y)\\to(-y,x)$','繞原點旋轉。'),
   'body':'<p>$U(-3,-8)\\to V(8,-3)$。</p>'},
  {'tag':'第 2 步','title':'反射','rule':('對 $x=a$ 反射','$x\\to 2a-x$','反射只改變 $x$ 坐標。'),
   'body':'<p>$V$ 的 $x=8$ 對 $x=2$ 反射：$x_W=2(2)-8=-4$，故選 A。</p>'}],
 'ans':'A　$-4$'},

{'n':25,'title':'DSE 2024 卷二 Q25 · 垂直平分線','tag':'DSE 2024 · 卷二 · Q25',
 'h1':'$AP=PB$ 即在中垂線上','sub':'坐標幾何 · 1 分題','marks':'1 分',
 'q':'點 $A$ 及 $B$ 的坐標分別為 $(-3,1)$ 及 $(-7,-5)$。若 $P$ 為直線 $x-y+13=0$ 上的一點使得 $AP=PB$，則 $P$ 的 $y$ 坐標為',
 'opts':['$-11$','$-2$','$2$','$11$'],
 'steps':[
  {'tag':'第 1 步','title':'求 $AB$ 的中點與斜率','body':'<p>中點 $M\\left(\\dfrac{-3-7}{2},\\dfrac{1-5}{2}\\right)=(-5,-2)$；$m_{AB}=\\dfrac{1+5}{-3+7}=\\dfrac{3}{2}$。</p>'},
  {'tag':'第 2 步','title':'寫出垂直平分線','rule':('互相垂直','$m_1m_2=-1$','中垂線斜率為 $-\\frac{2}{3}$。'),
   'body':'<p>$y+2=-\\dfrac{2}{3}(x+5)\\Rightarrow 2x+3y+16=0$。</p>'},
  {'tag':'第 3 步','title':'與已知直線聯立','body':'<p>由 $x=y-13$ 代入：$2(y-13)+3y+16=0\\Rightarrow 5y=10\\Rightarrow y=2$，故選 C。</p>'}],
 'ans':'C　$2$'},

{'n':26,'title':'DSE 2024 卷二 Q26 · 平行線條件','tag':'DSE 2024 · 卷二 · Q26',
 'h1':'不相交即斜率相等','sub':'直線方程 · 1 分題','marks':'1 分',
 'q':'求常數 $k$ 使得直線 $6x-8y=7k$ 與 $kx+12y=5$ 互不相交。',
 'opts':['$-16$','$-9$','$9$','$16$'],
 'steps':[
  {'tag':'第 1 步','title':'化為斜截式','body':'<p>$6x-8y=7k\\Rightarrow y=\\dfrac{3}{4}x-\\dfrac{7k}{8}$；$kx+12y=5\\Rightarrow y=-\\dfrac{k}{12}x+\\dfrac{5}{12}$。</p>'},
  {'tag':'第 2 步','title':'斜率相等','rule':('平行','$m_1=m_2$ 且截距不同','兩直線不相交。'),
   'body':'<p>$\\dfrac{3}{4}=-\\dfrac{k}{12}\\Rightarrow k=-9$，故選 B。</p>'}],
 'ans':'B　$-9$'},

{'n':27,'title':'DSE 2024 卷二 Q27 · 圓的方程','tag':'DSE 2024 · 卷二 · Q27',
 'h1':'先化為標準式','sub':'圓方程 · 1 分題','marks':'1 分',
 'q':'記圓 $C$ 為 $3x^{2}+3y^{2}-6x+12y-4=0$。下列何者正確？<br>I. 原點在 $C$ 之內。<br>II. $C$ 的圓周小於 $16$。<br>III. $C$ 的圓心至 $x$ 軸的垂直距離為 $2$。',
 'opts':['只有 I 及 II','只有 I 及 III','只有 II 及 III','I、II 及 III'],
 'steps':[
  {'tag':'第 1 步','title':'求圓心與半徑','rule':('標準式','$x^{2}+y^{2}+Dx+Ey+F=0$','圓心 $\\left(-\\frac{D}{2},-\\frac{E}{2}\\right)$。'),
   'body':'<p>全式除以 $3$：$x^{2}+y^{2}-2x+4y-\\dfrac{4}{3}=0$。</p><p>圓心 $G(1,-2)$；$r=\\sqrt{1+4+\\dfrac{4}{3}}=\\sqrt{\\dfrac{19}{3}}\\approx2.52$。</p>'},
  {'tag':'第 2 步','title':'檢查三項','body':'<p>I：$OG=\\sqrt{5}\\approx2.24<2.52$，原點在圓內 ✓<br>II：圓周 $=2\\pi(2.52)\\approx15.8<16$ ✓<br>III：圓心至 $x$ 軸距離 $=|-2|=2$ ✓</p>'},
  {'tag':'第 3 步','title':'結論','body':'<p>三項皆正確，故選 D。</p>'}],
 'ans':'D　I、II 及 III'},

{'n':28,'title':'DSE 2024 卷二 Q28 · 組合與概率','tag':'DSE 2024 · 卷二 · Q28',
 'h1':'同時抽兩張，用組合','sub':'概率 · 1 分題','marks':'1 分',
 'q':'從分別編號 $1,2,3,4,5$ 及 $6$ 的六張卡中同時隨機抽出兩個數。求所抽得的數之積不小於 $12$ 的概率。',
 'opts':['$\\dfrac{1}{3}$','$\\dfrac{2}{3}$','$\\dfrac{7}{15}$','$\\dfrac{8}{15}$'],
 'steps':[
  {'tag':'第 1 步','title':'樣本空間','rule':('組合','$C_{2}^{6}=\\dfrac{6\\times5}{2}$','「同時」代表不計次序。'),
   'body':'<p>共有 $C_{2}^{6}=15$ 個組合。</p>'},
  {'tag':'第 2 步','title':'數出有利組合','body':'<p>積 $\\ge12$：$\\{2,6\\},\\{3,4\\},\\{3,5\\},\\{3,6\\},\\{4,5\\},\\{4,6\\},\\{5,6\\}$，共 $7$ 個。</p>'},
  {'tag':'第 3 步','title':'求概率','body':'<p>$P=\\dfrac{7}{15}$，故選 C。</p>'}],
 'ans':'C　$\\dfrac{7}{15}$'},

{'n':29,'title':'DSE 2024 卷二 Q29 · 箱形圖','tag':'DSE 2024 · 卷二 · Q29',
 'h1':'分佈域是 $Q_{3}$ 的函數','sub':'統計 · 1 分題','marks':'1 分',
 'q':'以下的箱形圖顯示一組兒童在遊戲中所得代幣數目的分佈。若該分佈的分佈域是其四分位數間距的三倍，求 $m$。',
 'opts':['$248$','$275$','$336$','$360$'],
 'steps':[
  {'tag':'第 1 步','title':'讀出五數概括','body':'<p>最小值 $136$、$Q_{1}=163$、中位數 $224$、$Q_{3}=m$、最大值 $472$。</p>'},
  {'tag':'第 2 步','title':'分佈域與四分位數間距','rule':('定義','分佈域 $=$ 最大 $-$ 最小；$\\text{IQR}=Q_{3}-Q_{1}$','留意 $m$ 只出現在 IQR。'),
   'body':'<p>分佈域 $=472-136=336$；$\\text{IQR}=m-163$。</p>'},
  {'tag':'第 3 步','title':'解方程','body':'<p>$336=3(m-163)\\Rightarrow m-163=112\\Rightarrow m=275$，故選 B。</p>'}],
 'ans':'B　$275$'},

{'n':30,'title':'DSE 2024 卷二 Q30 · 標準差、眾數、中位數','tag':'DSE 2024 · 卷二 · Q30',
 'h1':'先由平均數鎖定 $m+n$','sub':'統計 · 1 分題','marks':'1 分',
 'q':'考慮以下正整數：$5,\\ 5,\\ 5,\\ 6,\\ 9,\\ 9,\\ 11,\\ 13,\\ m,\\ n$。設 $p$、$q$ 及 $r$ 分別為上述正整數的標準差、眾數及中位數。若上述正整數的平均數為 $7$，則下列何者必為正確？<br>I. $p>3$　II. $q=5$　III. $r<7$',
 'opts':['只有 I 及 II','只有 I 及 III','只有 II 及 III','I、II 及 III'],
 'steps':[
  {'tag':'第 1 步','title':'用平均數','body':'<p>總和 $=10\\times7=70$，已知八個數之和為 $63$，故 $m+n=7$。</p>'},
  {'tag':'第 2 步','title':'可能組合','body':'<p>正整數組合只有 $\\{1,6\\},\\{2,5\\},\\{3,4\\}$。</p>'},
  {'tag':'第 3 步','title':'逐項檢查','body':'<p>三組的標準差分別約為 $3.32,3.19,3.13$，皆 $>3$ ✓；三組的眾數都是 $5$ ✓；中位數分別為 $6,5.5,5.5$，皆 $<7$ ✓。</p><p>故選 D。</p>'}],
 'ans':'D　I、II 及 III'},
]
