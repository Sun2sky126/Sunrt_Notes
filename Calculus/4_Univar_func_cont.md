# 一元函数及其连续性 Univariable Functions & Continuity


## 一元函数 Univariable Functions

### 基本概念

对于两个集合$X$和$Y$，如果存在这样一条对应法则$f$，使得$X$中的任意元素$x$在此法则下，都能在$Y$找到**唯一**d的元素$y$与之对应，则称$f$是$X$到$Y$的一个**映射**（mapping），记作$f:X\to Y$，或者$f: x\mapsto y$，这时$y$也可以记作$y=f(x)$或者$y=f|_{x}$. $x$称之为（$y$的）**原像**（preimage），$y$称为$x$的**像**（image）. 原像和像的概念同样适用于集合，设$A\subseteq X$，则$f(A):=\{f(x):x\in A\}$称为$A$的像. 我们称$X$是$f$的**定义域**（domain），记为$X=\mathrm{Dom} f$，称$Y$是$f$的**到达域**或**陪域**（codomain），称$f(X)$是$f$的**值域**（range），记为$\mathrm{Range} f$. 显然$f(X)\subseteq Y$.
如果$X$和$Y$都是数集，此时的映射也称为**函数**（function）. 函数可以用表达式、表格、框图、图像等描述. 称曲线$\{(x,y):y=f(x), x\in I\}$是函数$f$在定义域（或区间）$I$内的**图像**. 函数的相关概念和性质我们已经在之前学习过，故不再重复叙述，只做简单总结：

（1）函数的性质：（严格）单调递增/递减性、有界性、周期性、奇偶性、对称性等.

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

> 和前述数列的极限的定义相比，注意到，在定义函数的极限时，我们额外要求函数在某些区域上有定义. 例如，如果要研究$x\to+\infty$的极限时，至少要求函数在某个$(c,+\infty)$上有定义，否则将毫无意义. 而在研究$x\to a$时，则要求$a$应该是函数定义域的一个**聚点**，即函数在$a$的某个去心邻域上有定义.


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

```{caution}
可以在两式之比中使用等价无穷小替换；但是如果分子或分母包含多个式子的加法或减法，则不能对其中的某个部分直接使用替换.
```

### 函数极限的性质

若$\displaystyle\lim_{x\to \star}f(x)=l$，则对**任意**趋于$\star$的数列$\{x_n\}$，$\{f(x_n)\}$必然趋于$l$.

## 一元函数的连续性 Continuity

## 连续函数的性质 Properties of Continuous Functions

