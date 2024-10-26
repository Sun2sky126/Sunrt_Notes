# 一元函数及其连续性 Univariable Functions & Continuity


## 一元函数 Univariable Functions

### 基本概念

对于两个集合$X$和$Y$，如果存在这样一条对应法则$f$，使得$X$中的任意元素$x$在此法则下，都能在$Y$找到**唯一**d的元素$y$与之对应，则称$f$是$X$到$Y$的一个**映射**（mapping），记作$f:X\to Y$，或者$f: x\mapsto y$，这时$y$也可以记作$y=f(x)$或者$y=f|_{x}$. $x$称之为（$y$的）**原像**（preimage），$y$称为$x$的**像**（image）. 原像和像的概念同样适用于集合，设$A\subseteq X$，则$f(A):=\{f(x):x\in A\}$称为$A$的像. 我们称$X$是$f$的**定义域**（domain），记为$X=\mathrm{Dom} f$或者$D(f)$，称$Y$是$f$的**到达域**或**陪域**（codomain），称$f(X)$是$f$的**值域**（range），记为$\mathrm{Range} f$或者$R(f)$. 显然$f(X)\subseteq Y$.
如果$X$和$Y$都是数集，此时的映射也称为**函数**（function）. 函数可以用表达式、表格、框图、图像等描述. 称曲线$\{(x,y):y=f(x), x\in I\}$是函数$f$在定义域（或区间）$I$内的**图像**. 函数的相关概念和性质我们已经在之前学习过，故不再重复叙述，只做简单总结：

（1）函数的性质：（严格）单调递增/递减性、有界性、周期性、奇偶性、对称性；单射、满射、一一映射等.

> 设$I\subseteq \mathrm{Dom} f$，则$f$在$I$上的有界性就定义为其值域$f(I)$的有界性，详见[上一章](./1_Limits_and_real_numbers.md#上下界和上下确界).

（2）函数的运算：对于两个函数$f$和$g$，可以定义两个函数的加减法$f\pm g$、乘法$fg$、除法$\displaystyle\frac{f}{g}$和复合$f\circ g$等.

（3）函数图像的变换：包括函数图像的平移变换、横向/纵向伸缩变换、对称变换等.

（4）反函数：如果$f$的反函数存在，则记这个反函数为$f^{-1}$.

### 初等函数

以下六类函数称为**基本初等函数**：

（1）常数函数（constant）：$f(x)= c$.

（2）幂函数（power functions）：$f(x)=x^p$

> 可以将上面两类函数归结为**多项式函数**（polynomial functions），即$f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1 x+a_0$. 如果一个函数可以表示为两个多项式函数的比值，则称其为有理函数.

（3）指数函数（exponential functions）：$f(x)=a^x$，其中$a>0$且$a\neq 1$.

（4）对数函数（logarithms）：$f(x)=\log_{a}x$，其中$a>0$且$a\neq 1$.

（5）三角函数（trigonometric functions）：包括正弦函数（sine）$f(x)=\sin x$和其倒数余割函数（cosecant）$f(x)=\csc x$、余弦函数（cosine）$f(x)=\cos x$和其倒数正割函数（secant）$f(x)=\sec x$、正切函数（tangent）$f(x)=\tan x$和其倒数余切函数（cotangent）$f(x)=\cot x$.

（6）反三角函数（inverse trigonometric functions）：（5）中各个三角函数的反函数. 例如，正弦函数对应的是反正弦函数，记为$f(x)=\arcsin x$或者$f(x)=\sin^{-1}x$.

> 基于指数函数$\mathrm{e}^x$，可以定义双曲函数（hyperbolic functions）. 如双曲正弦函数$\displaystyle \sinh x=\mathrm{sh} x=\frac{\mathrm{e}^{x}-\mathrm{e}^{-x}}{2}$、双曲余弦函数$\displaystyle \cosh x=\mathrm{ch} x = \frac{\mathrm{e}^{x}+\mathrm{e}^{-x}}{2}$、双曲正切函数$\displaystyle\tanh x=\mathrm{th} x=\frac{\sinh x}{\cosh x}$. 这些函数和三角函数具有十分相似的性质（包括相互间的转换、倍角公式、和角公式等.

上述六类基本初等函数，在经过**有限次**的加、减、乘、除或复合运算后得到的函数，均称为**初等函数**（elementary functions）.

> - 之所以提出初等函数这一概念，是因为其具备非常好的性质，如连续性、光滑性等，研究起来十分简单. 因此使用函数建模时也优先考虑使用初等函数.
> - 什么样的函数*不是*初等函数呢？即构建函数的过程中，涉及到了非基本初等函数，或者涉及了**无穷次**运算. 前者的例子包括我们所熟知的分段函数(piecewise functions)，如$f(x)=\begin{cases}  f_A(x), & x\in A \\  f_B(x), & x\in B \\  \cdots, & \cdots \end{cases}$，可以写成$f(x)=f_A(x)I_A(x)+f_B(x)I_B(x)+\cdots$的形式，其中$I_{S}(x):=\begin{cases}1, & x\in S \\ 0, & x\notin S\end{cases}$，称为示性函数，而示性函数不是基本初等函数. 后者的例子包括用函数项级数表达的函数（如Bessel函数、Weierstrass函数、Riemann-$\zeta$函数等，这些函数没有初等形式.）


## 函数的极限 Limits of Functions

### 函数极限的定义

函数极限的定义可以类比于数列极限的定义，采用$\varepsilon-N$语言，但是真正的情形要比数列极限复杂. 数列可以视作定义在$\mathbb{N}$上的函数，其极限过程只有下标$n$递增到正无穷一种情况；而函数的定义域是多样的，且其极限过程可以是趋于正无穷，可以趋于负无穷，也可以趋于一个点；可以是递增方向，也可以是递减方向.

（1）趋于无穷时的定义：

- 设函数$f(x)$在$(c,+\infty)$上有定义，存在$l\in\mathbb{R}$，使得对于任意$\varepsilon>0$，总存在$N>0$，使得对于任意$x>N$，均有$|f(x)-l|<\varepsilon$，则称$f$在$x\rightarrow +\infty$时收敛到$l$，或$l$是$f$在$+\infty$处的**极限**，记为$\displaystyle \lim_{x\to+\infty} f(x)=l$，或$f(x)\to l, x\to+\infty$.
- 设函数$f(x)$在$(-\infty, c)$上有定义，存在$l\in\mathbb{R}$，使得对于任意$\varepsilon>0$，总存在$N<0$，使得对于任意$x < N$，均有$|f(x)-l|<\varepsilon$，则称$f$在$x\rightarrow -\infty$时收敛到$l$，或$l$是$f$在$-\infty$处的**极限**，记为$\displaystyle \lim_{x\to-\infty} f(x)=l$，或$f(x)\to l, x\to-\infty$.
- 设函数$f(x)$在$(-\infty, c)\cup (d,+\infty)$上有定义，存在$l\in\mathbb{R}$，使得对于任意$\varepsilon>0$，总存在$N>0$，使得对于任意$|x|>N$，均有$|f(x)-l|<\varepsilon$，则称$f$在$x\rightarrow \infty$时收敛到$l$，或$l$是$f$在$\infty$处的**极限**，记为$\displaystyle \lim_{x\to\infty} f(x)=l$，或$f(x)\to l, x\to\infty$.

> $\displaystyle \lim_{x\to\infty} f(x)=l$ 当且仅当 $\displaystyle \lim_{x\to+\infty} f(x)=l$ 和 $\displaystyle \lim_{x\to\infty} f(x)=l$ 同时成立.

（2）趋于某点时的定义

- 设函数在$(c, a)\cup (a, d)$上有定义，存在$l\in\mathbb{R}$，使得对于任意$\varepsilon>0$，总存在$\delta>0$，使得对于任意满足$|x-a|<\delta$的$x$，均有$|f(x)-l|<\varepsilon$，则称$f$在$x\rightarrow a$时收敛到$l$，或$l$是$f$在$a$处的**极限**，记为$\displaystyle \lim_{x\to a} f(x)=l$，或$f(x)\to l, x\to a$.
- 设函数在$(a, d)$上有定义，存在$l\in\mathbb{R}$，使得对于任意$\varepsilon>0$，总存在$\delta>0$，使得对于任意满足$x-a<\delta$的$x$，均有$|f(x)-l|<\varepsilon$，则称$f$在$x\rightarrow a^+$时收敛到$l$，或$l$是$f$在$a$处的**右极限**，记为$\displaystyle \lim_{x\to a^+} f(x)=l$，或$f(x)\to l, x\to a^+$，或$f(a^+)=l$，或$f(a+0)=l$.
- 设函数在$(c,a)$上有定义，存在$l\in\mathbb{R}$，使得对于任意$\varepsilon>0$，总存在$\delta>0$，使得对于任意满足$a-x<\delta$的$x$，均有$|f(x)-l|<\varepsilon$，则称$f$在$x\rightarrow a^-$时收敛到$l$，或$l$是$f$在$+\infty$处的**右极限**，记为$\displaystyle \lim_{x\to a^-} f(x)=l$，或$f(x)\to l, x\to a^-$，或$f(a^-)=l$，或$f(a-0)=l$.

左极限和右极限统称为**单边极限**，单边极限不是真正的极限，不能只依靠某一边的极限而对函数在某点处的敛散性作判断. **函数在一点处收敛当且仅当其左右极限均存在且相等**.

> - 和前述数列的极限的定义相比，注意到，在定义函数的极限时，我们额外要求函数在某些区域上有定义. 例如，如果要研究$x\to+\infty$的极限时，至少要求函数在某个$(c,+\infty)$上有定义，否则将毫无意义. 而在研究$x\to a$时，则要求$a$应该是函数定义域的一个**聚点**，即函数在$a$的某个去心邻域上有定义.
> - 可以将区间$(a-r,a+r)$记为$B(a,r)$或$U(a,r)$，即以$a$为中心半径为$r$的邻域；而将去心邻域$(a-r,a)\cup (a,a+r)$记为$\mathring{B}(a,r)$或者$\mathring{U}(a,r)$.

同样，函数的收敛也可以使用**柯西收敛准则**，这提供了一种绕开极限值的判据方式。例如：

- 设$f(x)$在$(c,+\infty)$上有定义，对$\forall\varepsilon >0$，总存在$M>0$，使得对于任意的$x_1,x_2>M$，都有$|f(x_1)-f(x_2)| < \varepsilon$，则称$f(x)$在$x\to +\infty$时收敛.
- 设$f(x)$在$x_0$的一个去心邻域上有定义，对$\forall\varepsilon >0$，总存在$\delta>0$，使得对于任意的$x_1,x_2\in\mathring{U}(x_0,\delta)$，都有$|f(x_1)-f(x_2)| < \varepsilon$，则称$f(x)$在$x\to x_0$时收敛.
- 其他极限过程类似.


### 无穷小量和无穷大量

如果$f(x)$在某一极限过程（可以是上一小节六种情况的某一种，后面统一记为$x\to\star$）中趋于0，则称$f(x)$是（这一过程）的**无穷小量**，记为$f(x)=o(1),\,x\to\star$. 而如果是趋于无穷，则称为**无穷大量**. 上一章所提及的数列的无穷小量和无穷大量的性质仍然适用于函数（前提是应用在同一个极限过程）.

设$f(x)$和$g(x)$都是某一极限过程$x\to\star$的无穷小量，则我们可以比较它们的“分阶”：

- 若$\displaystyle \lim_{x\to\star}\frac{f(x)}{g(x)}=0$，则称$f$是$g$的**高阶无穷小量**，有时也记作$f(x)=o(g(x))$，我们称$f$比$g$高阶，$g$比$f$低阶.
- 若$\displaystyle \lim_{x\to\star}\frac{f(x)}{g(x)}=l$，其中$l$既不是0也不是无穷大，则称$f$是$g$的**同阶无穷小量**
- 在上面的描述中，“高”和“低”都是定性的描述，我们也可以使用定量描述：如果$\displaystyle \lim_{x\to\star}\frac{f(x)}{g(x)^k}=l\neq 0$，则称$f$是$g$的$k$**阶无穷小**. 此时$g(x)$作为我们比较的基准，一般选取较简单的形式作为基准$g(x)$，例如$x$、$x-a$、$\displaystyle \frac{1}{x-a}$等.

> 无穷小的“阶”描述了无穷小量的“衰减速度”. 例如，在$x\to 0$的过程中，$x^2$比$x$下降到0的速度更快，而$x$比$\log(x+1)$的下降速度更快，则$x^2$是更高阶的无穷小，$\log(x+1)$是更低阶的无穷小.

同阶无穷小的一种特殊情形是**等价无穷小**，记为$f(x)\sim g(x), x\to\star$. 有两种定义方式：

- 若$\displaystyle \lim_{x\to\star}\frac{f(x)}{g(x)}=1$，则称$f$和$g$是**等价无穷小量**.
- 若$f-g$是$f$（或$g$）的高阶无穷小，则称$f$和$g$是**等价无穷小量**.

无穷小的分阶有诸多应用：

- 如果要求$\displaystyle\frac{f(x)}{t(x)}$的极限，而这一极限过程中$f(x)$和$g(x)$是等价无穷小，则$\displaystyle\lim\frac{f(x)}{t(x)}=\lim\frac{g(x)}{t(x)}$. 同理分母也可以进行类似的替换.
- 如果$f(x)\sim a_kx^k$，则可以根据上述等价无穷小的第二个定义，得出$f(x)=a_kx^k+o(x^k)$，完成了对$f(x)$的一种分解（使用多项式来近似$f(x)$，这在物理学和工程中是一种常用的技巧）. 同理，可以对$f(x)-a_kx^k$作进一步分解，得到$f(x)=a_kx^k+a_lx^l+o(x^l)$，其中$l>k$. 实际上，Taylor展开就是这样的一种分解方式.

```{attention}
可以在两式之比中使用等价无穷小替换；但是如果分子或分母包含多个式子的加法或减法，则不能对其中的某个部分直接使用替换.
```

### 函数极限的性质

类比数列极限的性质，我们也可以得到函数极限的相关性质；同时，函数的极限也具有一些不同于数列极限的新性质.

（一）单个函数极限的相关性质

（1）**保序性、保号性**：若$\displaystyle \lim_{x\to+\infty}f(x)=A>p$，则$x$充分大时总有$f(x)>p$；若$\displaystyle \lim_{x\to x_0}f(x)=A>p$，则$x$充分接近$x_0$时总有$f(x)>p$. $A < p$和其它极限过程同理.

（2）**有界性**：若$x\to+\infty$时$f(x)$收敛，则$x$充分大时$f(x)$有界；若$x\to x_0$时$f(x)$收敛，则$x$充分接近$x_0$时$f(x)$有界.

> - 上述两条性质和数列的不同之处在于，数列的保序性、有界性是整体的性质，即对所有$n$均成立；而函数的保序性和有界性是局部性质，只对充分大的$x$或者充分靠近$x_0$的$x$成立，而在此之外未必成立.
> - “充分大”和“充分接近$x_0$都可以用更精准的$\varepsilon-N$或者$\varepsilon-\delta$语言来描述. 后面为了省事，我们会直接说成$x$充分接近于$\star$.

（3）**唯一性**：若$f(x)$在某个极限过程中收敛，则极限是唯一的.

（4）**和数列结合的性质**：若$\displaystyle\lim_{x\to \star}f(x)=l$，则对**任意**趋于$\star$的数列$\{x_n\}$，$\{f(x_n)\}$必然趋于$l$.

（二）多个函数极限的相关性质

（1-a）**保序性**： 若在$x\to\star$时有$f(x)\to a$和$g(x)\to b$，且$a>b$，则在$x$充分接近$\star$时有$f(x)>g(x)$.

（1-b）**保序性**：若在$x\to\star$时有$f(x)\to a$和$g(x)\to b$，且在$x$充分接近$\star$时有$f(x)\geqslant g(x)$，则$a\geqslant b$.

（2）**夹逼定理**：若$x$在$\star$附近有$g(x)\leqslant f(x)\leqslant h(x)$，且$x\to\star$时有$g(x)\to A$和$h(x)\to A$，则$x\to\star$时也有$f(x)\to A$.

（3）**四则运算和其他运算**，若$x\to\star$时有$f(x)\to A$和$g(x)\to B$，则$f(x)\pm g(x)\to A\pm B$，$f(x)g(x)\to AB$，当$g(x)\neq 0$和$B\neq 0$时有$\displaystyle\frac{f(x)}{g(x)}\to\frac{A}{B}$. 更多地，我们有$|f(x)|\to |A|$、$f(x)^\alpha\to A^\alpha(\alpha>0)$、$\mathrm{e}^{f(x)}\to\mathrm{e}^A$和$\ln f(x)\to\ln A\,(f(x)>0, A>0)$.

（4）**复合函数的极限**：这也是函数极限相比于数列极限所独有的性质之一。设$\displaystyle\lim_{x\to x_0}f(x)=u_0$，且$\displaystyle\lim_{u\to u_0}g(u)=A$，并且在$x_0$的一个去心邻域中，始终有$f(x)\neq u_0$，则$\displaystyle \lim_{x\to x_0}g(f(x))=\lim_{u\to u_0}g(u)=A$.

```{attention}
复合函数的极限要求在$x$趋于$x_0$的过程中，不能有其余的$x$值满足$f(x)=u_0$，这是十分必要的. 因此在使用变量替换求解极限时，最好的处理方法是使用一个一一映射来替换.
```

（三）函数极限的求法和收敛性判断

很多方法同数列的极限求法类似，如使用定义、夹逼定理、四则运算、柯西收敛准则、单调有界等等. 此外，也有一些新的方法，例如：

- 直接代入：如果$f$在$x_0$处连续，则$\displaystyle\lim_{x\to x_0}f(x)=f(x_0)$.
- 变量代换
- 等价无穷小替换
- Taylor展开替换
- L'Hospital法则等

```{tip}
一些常用极限：

$$
\lim_{x\to\infty}\left(1+\frac{1}{x}\right)^{x}=\lim_{x\to 0}(1+x)^\frac{1}{x}=\mathrm{e}
$$

$$
\lim_{x\to 0}\frac{\sin x}{x} = 1
$$

$$
\lim_{x\to 0}\frac{\ln(x+1)}{x} = 1
$$
```

## 一元函数的连续性 Continuity

### 函数连续性的定义

如果$f(x)$在$x_0$处的**邻域**有定义，且满足$\displaystyle\lim_{x\to x_0}f(x)=f(x_0)$，则称$f$在$x_0$**连续**（continuous），记为$f\in\mathcal{C}(x_0)$. 类比于单侧极限，我们也可以定义单侧连续. 若$f(x_0^+)=f(x_0)$，则称为右连续；若$f(x_0^-)=f(x_0)$，则称为左连续. $f$在$x_0$连续当且仅当在$x_0$处同时右连续和左连续.

定义$f$在一点处的连续性后，可以进一步定义在区间上的连续性. 对区间$(a,b)$，若$f$在其内的每一点都连续，则称$f$在区间$(a,b)$上连续，记为$f\in\mathcal{C}(a,b)$. 对区间$[a,b]$，若$f$在$(a,b)$连续，且在两个端点$a$、$b$处单侧连续，则称$f$在区间$[a,b]$上连续，记为$f\in\mathcal{C}[a,b]$. 同理可以定义在半开半闭区间上的连续性.

### 连续性的判断方法

判定$f$在$x_0$连续的三个要素：$f$在$x_0$的附近有定义，且$x\to x_0$时极限存在；$f$在$x_0$这一点处有定义，保证$f(x_0)$存在；$f$在$x_0$的极限值等于$f(x_0)$本身.

进一步地，可以由四则运算来推知其他函数的连续性. 若$f$，$g$均在$x_0$连续，则$f\pm g$和$fg$也在$x_0$处连续. 若$g$在$x_0$的邻域内不为0，则$\displaystyle \frac{f}{g}$也在$x_0$连续.

也可以由复合函数来推广连续性. 设$g(x_0)=u_0$，且$g$在$x_0$连续，而$f$在$u_0$连续，则$g\circ g$在$x_0$连续.

容易证明**基本初等函数**在其定义域内都是连续的. 进一步结合上述两个性质，可以推知：所有初等函数在其定义域内都是连续的.

### 函数的间断

如果$f$在$x_0$处不连续，那就称其在$x_0$处间断，或者$x_0$是$f$的一个间断点. 间断点可分为第一类间断点和第二类间断点，其中第一类间断点又分为可去间断点和跳跃间断点. 设$f$在$x_0$处间断，则：

- 若$f(x_0^+)$和$f(x_0^-)$均存在，则称为**第一类间断点**；若$f(x_0^+)$和$f(x_0^-)$中至少有一个不存在，则称为**第二类间断点**.
- 在第一类间断点中，若$f(x_0^+)$和$f(x_0^-)$均存在，则$\displaystyle \lim_{x\to x_0}f(x)$存在，但是不等于$f(x_0)$，或者$f(x_0)$没有定义. 此时$x_0$又称为**可去间断点**.
- 在第一类间断点中，若$f(x_0^+)\neq f(x_0^-)$，则称$x_0$是一个**跳跃间断点**.

> 对于可去间断点，可以让$f(x_0)$的值移动到$\displaystyle \lim_{x\to x_0}f(x)$处，从而将其修改为连续的. 对于跳跃间断点，可以整体移动一侧的函数图像来使其连续. 对于第二类间断点，由于单侧极限不存在（如振荡或者无穷），则很难通过简单的修改来使其连续.

## 连续函数的性质 Properties of Continuous Functions

下面是闭区间上连续函数的重要性质.

### 零点定理和介值定理

（1）**Bolzano-Cauchy第一定理（零点定理）**：设$f\in\mathcal{C}[a,b]$且$f(a)$、$f(b)$异号，则存在$c\in[a,b]$使得$f(c)=0$.

> 可以使用“二分法”并结合闭区间套定理来证明. 也可以构造$\{x\in[a,b]:f(x)<0\}$这一集合，利用确界定理来证明.

（2）**Bolzano-Cauchy第二定理（介值定理）**：设$f\in\mathcal{C}[a,b]$，$f(a)=A$、$f(b)=B$，则对于$\forall C\in[A,B]$，存在$c\in[a,b]$，使得$f(c)=C$.

> 对于非平凡的情形，构造辅助函数$g(x)=f(x)-C$，然后应用零点定理即可证明.

（3）设$f\in\mathcal{C}[a,b]$，则$f([a,b])$（即值域）构成一个区间. 构成一个区间则意味着其具有$(a,b)$或者半开半闭、闭区间的形式，而不是$(a,b)\cup (c,d)$这种几个区间相并的形式.

> - 构成一个区间，即对于$\forall y_1,y_2 \in f([a,b])$，都有$[y_1,y_2]\subseteq f([a,b])$. 这其实就是介值定理.
> - 由闭区间上连续函数的最值定理可知，值域不仅是一个区间，而且是闭区间.
> - 设$f\in\mathcal{C}(a,b)$，则用类似的方法可以得到$f((a,b))$也构成一个区间，只不过这个区间可能含有无穷远作为端点. 半开半闭区间同理.

### 有界和最值定理

（1）**Weierstrass第一定理**：若$f\in\mathcal{C}[a,b]$，则其在$[a,b]$上必有上下界.

```{admonition} 证明过程
:class: tip, dropdown

若$f$在$[a,b]$无界，则可以构造数列$\{x_n\}\subset [a,b]$，使得对于每一项$n$有$|f(x_n)|>n$，因而数列$\{|f(x_n)|\}$趋于无穷. 而$\{x_n\}$有界，则可以选出收敛子列$\{x_{n_k}\}$，假设$x_{n_k}\to x_0\in[a,b]$，由极限的性质可知$|f(x_{n_k})|\to |f(x_0)|$. 趋于无穷的数列是不可能有收敛子列的，矛盾.

```

有上下界就意味着有上下确界. 更进一步，我们可以说明其还具有最值，即上下确界可以在值域中取到：

（2）**Weierstrass第二定理**：若$f\in\mathcal{C}[a,b]$，则存在$m,M\in [a,b]$，使得$\displaystyle f(m)=\min_{x\in [a,b]}f(x)$，$\displaystyle f(M)=\max_{x\in [a,b]}f(x)$

```{admonition} 证明过程
:class: tip, dropdown

只证明最大值情形. 设$\displaystyle M=\sup_{x\in[a,b]}f(x)$. 则可以构造数列$\{x_n\}\subset [a,b]$，使得对于每一项$n$有$\displaystyle |f(x_n)|>M-\frac{1}{n}$，因而数列$\{f(x_n)\}$趋于$M$. 而$\{x_n\}$有界，则可以选出收敛子列$\{x_{n_k}\}$，假设$x_{n_k}\to x_0\in[a,b]$，由极限的性质可知$f(x_{n_k})\to f(x_0)$. $\{f(x_{n_k})\}$作为收敛数列$\{f(x_n)\}$的子列，其必然和原数列趋于同一个极限，故$f(x_0)=M$.

```

### 一致连续性

$f$在区间$I$上连续，是说$\forall x_0\in I$，和$\forall \varepsilon >0$，总存在$\delta>0$，使得$\forall x\in \mathring{U}(x_0,\delta)$，都有$|f(x)-f(x_0)|<\varepsilon$. 由此可见，此处$\delta$的选取不仅依赖于$\varepsilon$，还依赖于$x_0$的选取. 如果$\delta$的选取可以不依赖于$x_0$，即可以为$I$中的每一点找到一个“公共”的$\delta$，则称$f$在$I$上是**一致连续**的. 可以形式化为：

- $\forall \varepsilon >0$，总存在$\delta>0$，使得任意$\forall x_1\in I$，和$\forall x_2\in \mathring{U}(x_1,\delta)$，都有$|f(x_1)-f(x_2)|<\varepsilon$.
- $\forall \varepsilon >0$，总存在$\delta>0$，使得任意$\forall x_1,x_2$，若满足$|x_1-x_2|<\delta$，则$|f(x_1)-f(x_2)|<\varepsilon$.

> - 我们交换了$\forall x_0$和$\exists \delta$的顺序，从而得到一致连续的定义. 
> - 一致连续是定义在一个区间上的，没法说一个函数在一个点上一致连续（跟谁一致呢？）.

**Cantor定理**：若$f$在闭区间上连续，则其也在该区间上一致连续.

### 单调函数的连续性

下面几条性质专门适用于单调函数.

（1）定义在一个区间上的单调函数只可能有跳跃间断点，而不可能有可去间断点和第二类间断点.

> 对于区间内任一点$x_0$，在$x\to x_0^+$或$x_0^-$的过程中，一定是单调且有界的，则必然收敛，故单侧极限总是存在，不可能存在第二类间断.
> 若$f$有可去间断点，则其必然不可能单调.

（2）设函数$f$在一个区间上单调，则$f$在区间上连续当且仅当它的值域构成一个区间.

> - 必要性可以由介值定理证明，而充分性可以这样证明：若$f$不连续，由于其是单调的，则只可能存在跳跃间断点，而易证跳跃间断点会导致值域区间的断开.

(3) 若函数$f$在一个区间上严格单调且连续，则其存在反函数，且反函数也单调且连续.

> - 反函数的连续性可以由上面的（2）得知.