# 数列极限与实数 Limits of Sequences & Real Numbers

<!-- $\newcommand{\varlimsup}{\overline{\lim}}$ -->

## 数列极限的定义 Definition of Sequence Limits

对于数列$\{x_n\}_{n=1}^{\infty}$，如果存在$l\in\mathbb{R}$，使得对于任意$\varepsilon>0$，总能找到一个对应的$N$，使得对于任意满足$n>N$的$x_n$，都有$\vert x_n-l\vert <\varepsilon$，则称数列$\{x_n\}_{n=1}^{\infty}$**收敛**（到$l$），或者说数列$\{x_n\}_{n=1}^{\infty}$趋于$l$，或称$l$是数列$\{x_n\}_{n=1}^{\infty}$的极限，记为

$$
\lim_{n\rightarrow\infty}x_n = l\quad\text{或}\quad x_n\rightarrow l,\quad n\rightarrow\infty
$$

对于数列而言，在研究极限时仅考虑$n\rightarrow\infty$的情形，这一点和后面要讲到的函数的极限是不同的。因此我们可以更精简地记为$\displaystyle \lim x_n = l$和$x_n\rightarrow l$.

> - 直白地说，上面的定义是在描述：通过选择合适的$N$，我们可以将$\vert x_n - l\vert$控制到**任意小**. 即无论给定一个多么小的正数$\varepsilon$，总能找到若干合适的$N_\varepsilon$，从而将数列在超过$N_\varepsilon$的部分严格地控制在区间$(l-\varepsilon, l+\varepsilon)$以内.
> - 我们用$N_\varepsilon$而不是$N(\varepsilon)$，来澄清$N$和$\varepsilon$并不是一个严格的映射（函数）关系。对于每一个$\varepsilon$，我们有不止一种选择$N$的方式。假如我们找到了一个合适的$N^\star_\varepsilon$，则显然$N^\star_\varepsilon+1$、$N^\star_\varepsilon+4$甚至$N^\star_\varepsilon+10000$等也可以作为$N_\varepsilon$的选取方式。

对于数列$\{x_n\}_{n=1}^{\infty}$，只要能找到符合上述定义的$l\in\mathbb{R}$，则称其为**收敛**(convergent)的，否则是**发散**(divergent)的。

### 无穷小量和无穷大量的概念

如果数列$\{x_n\}_{n=1}^{\infty}$的极限是0，则其又称为**无穷小量**，记作

$$
x_n = o(1),\quad n\rightarrow\infty
$$

因此，数列$\{x_n\}_{n=1}^{\infty}$收敛至$l$这一命题**等价于**：$x_n-l$是无穷小量。

> 不能把无穷小量视作数字0（虽然有些场景下这样处理确实很爽，但有些场景则会出现0/0或者$0\times\infty$的复杂情形）。无穷小量并不是一个静态的数字，而是一个动态的变量，一个被下标$n$调控的量。我们可以调控$n$以使得这个变量的值可以**任意小**，因而称为无穷小量。

如果数列$\{x_n\}$满足：对任意的$E>0$，总存在$N_E>0$，使得对于任意$n>N_E$，总有$\vert x_n\vert > E$，则称数列$\{x_n\}$为**无穷大量**。记为$\lim x_n=\infty$或者$x_n\rightarrow\infty$. 特别地，如果$x_n$在这一过程中保持符号，例如，对任意的$E>0$，总存在$N_E>0$，使得对于任意$n > N_E $，总有 $x_n > E$ (**注意这里没有绝对值号**)，则记为$\lim x_n=+\infty$或$x_n\rightarrow +\infty$。如果$\{x_n\}$满足$-x_n\rightarrow+\infty$，则可以记作$\lim x_n=-\infty$或$x_n\rightarrow -\infty$.

> - 上面的定义是在描述：通过选择合适的$N$，我们可以将$\vert x_n\vert$（或者$x_n$，或者$-x_n$）控制到**任意大**.
> - 无穷大量同样也不是一个静态的数，而是一个变量。

### 无穷小量和无穷大量的性质

（1） **加法**：**有限个**无穷小量的和仍然是无穷小量，即$o(1)+o(1)=o(1)$.

（2） **乘法**：若$\{x_n\}$有界，则$\{x_n\}$和一个无穷小量的积也是无穷小量。

（3） **倒数**：若$\{x_n\}$是无穷大量，则$\displaystyle \left\{\frac{1}{x_n}\right\}$是无穷小量；若$\{x_n\}$是无穷小量且$x_n\neq 0$，则$\displaystyle \left\{\frac{1}{x_n}\right\}$是无穷大量.

## 上下界和上下极限 Upper/Lower Bounds&Limits

### 上下界和上下确界

对数集$A$，如果存在$M$，使得对于$A$中的任意元素$x$，均有$x\leqslant M$，则称$M$是$A$的一个**上界**(upper bound)，称$A$是一个有上界的集合. 如果存在$N$，使得对于$A$中的任意元素$x$，均有$x\geqslant N$，则称$N$是$A$的一个**下界**(lower bound)，称$A$是一个有下界的集合. 如果一个集合既有上界又有下界，则称其是**有界**的.

> 有界也可以定义为：存在$M$，使得对于$A$中的任意元素$x$，均有$|x|\leqslant M$.

如果集合$A$有上界，则必然有无数个上界（比上界$M$更大的数自然也是一个上界）. 这些上界中的最小值称为$A$的**上确界**（supremum），记为$\sup A$. 如果更形式化地描述，则为：$M=\sup A$当且仅当：（1）$\forall x\in A$，均有$x\leqslant M$（即，$M$是$A$的上界）；（2）$\forall m < M$，$\exists x\in A$，使得$x>m$（即，$M$是$A$最小的下界；任何比$M$更小的数都不可能是$A$的下界. 同理可以定义下确界：$A$的下界中的最大值称为$A$的**下确界**（infimum），记为$\inf A$.

> “确界”和“最值”的区别和联系：一个集合$A$的最值一定是$A$自身的一个元素. 如果$A$有最值，则这个最值就是确界. 但是如果$A$有确界，则未必有最值. 例如考虑区间$(0,1]$，其没有最小值，但是有下确界0；其有最大值1，这个最大值就是上确界.

但作出上述定义时，我们有一个问题需要解决：如何保证这些上界的最小值就一定存在呢？如何保证这些下界的最大值就一定存在呢？我们有**确界定理**：有上界的集合必然有上确界；有下界的集合必然有下确界.

> 确界定理是描述实数系完备性的基本定理之一，详见本章最后一节.

### 上下极限

不是所有数列都存在极限（无论是有限的数还是趋于无穷），但我们可以研究它的上下极限. 一个数列$\{x_n\}$的**上极限**（upper bound）记为$\displaystyle\limsup_{n\rightarrow \infty} x_n$或者$\displaystyle \varlimsup_{n\rightarrow \infty} x_n$，有下面两种等效的定义方式：

- 定义1：数列$\{x_n\}$所有子列的极限的最大值（上确界）.
- 定义2：$\displaystyle \limsup_{n\rightarrow \infty} x_n := \lim_{k\rightarrow\infty}\sup_{n>k}\{x_n\}$.

> - 若$1\leqslant n_1 < n_2 < \cdots $，则称$\{x_{n_k}\}$是$\{x_n\}$的一个**子列**.
> - 如果$\{x_n\}$没有上界，则上极限趋于正无穷；如果有上界，记$\displaystyle M_k:=\sup_{n>k}\{x_n\}$，则$\{M_k\}$是一个递减数列（由上确界定义可得），因此其必然趋于一有限数或负无穷. 因此任何有上界数列的上极限要么存在，要么趋于负无穷.

```{admonition} 两种定义等价性的证明
:class: tip, dropdown

- 记$\displaystyle \lim_{k\rightarrow\infty} M_k = M$，则$\forall\varepsilon>0$，存在$K>0$，使得$\forall k>K$，有$M_k < M+\varepsilon$，因此对$n>k$也有$x_n \leqslant M_n < M_k < M+\varepsilon$. 对任意子列仍然成立，因此由极限的保序性，任意子列的极限$a$必然满足$a\leqslant M+\varepsilon$. 又因为$\varepsilon$是任意正数，因此$a\leqslant M$.
- 进一步地，为了说明$M$就是这个最大值，需要证明等号可以取到，即找到极限为$M$的子列. 构造方法如下：$\forall n>k$有$x_n < M+\varepsilon$，又$M-\varepsilon < M_k$，则$M-\varepsilon$必然不是$\{x_n\}_{n>k}$的上界，即$\exists n'>k$使得$x_{n'}>M-\varepsilon$，我们选出$x_{n'}$添加到子列中；然后选择一个更小的$\varepsilon'$（例如可以选择$\varepsilon'=M-x_{n'}$），重复上述步骤，选出子列的下一项. 因此总有$|x_{n'}-M|<\varepsilon$，这样就找到了一个趋于$M$的子列. 至此，我们证明了上述两种定义的等价性.

```

类似地，数列的**下极限**记为$\displaystyle\liminf_{n\rightarrow\infty} x_n$或$\displaystyle\varliminf_{n\rightarrow\infty} x_n$，定义为：

- 定义1：数列$\{x_n\}$所有子列的极限的最小值（下确界）.
- 定义2：$\displaystyle \liminf_{n\rightarrow \infty} x_n := \lim_{k\rightarrow\infty}\inf_{n>k}\{x_n\}$.

所以，即使对于不收敛的数列，我们仍可以研究其上下极限。特别地，**数列有极限当且仅当其上下极限相等**，此时有

$$ \lim x_n = \varlimsup x_n = \varliminf x_n $$

## 极限的相关性质 Properties of Limits

### 单个数列极限的性质

（1） **保序性、保号性**：假定$\lim x_n = a$且$a > p$，则从某一项开始（或者说，存在一个$N_p$，使得对于任意的$n>N_p$），总有$x_n>p$。同理，若$a < q$，则从某一项开始，总有$x_n < q$。是为极限的**保序性**。

> 证明思路是很直接的：以$a>p$为例，只需要取一个足够小的$\varepsilon$满足$a-\varepsilon>p$（例如可以取$\displaystyle \varepsilon=\frac{a-p}{2}$）。则对任意$n>N_\varepsilon$，总有$x_n>a-\varepsilon>p$。另一种情况同理。

特别地，当$a>0$时，可以取$p=0$；当$a<0$时，可以取$q=0$。即：若数列趋于一个正数，则从某一项开始数列恒正；若数列趋于一个负数，则从某一项开始数列恒负。是为数列的**保号性**。

（2） **有界性**：收敛数列必有界。即若$\{x_n\}$收敛到$a$，则存在$M>0$，使得对于**所有**$x_n$，均有$\vert x_n\vert \leqslant M$.

> 任意取$\varepsilon$和一个对应的$N_\varepsilon$，则对于$n>N_\varepsilon$的部分，有$\vert x_n \vert < \vert a\vert + \varepsilon$；对于$1\leqslant n \leqslant N_\varepsilon$的部分，这$N_\varepsilon$个有限的$\vert x_n \vert$中总能照到一个最大值，令$\displaystyle M=\max\left\{\max_{1\leqslant n\leqslant N_\varepsilon}|x_n|, \vert a\vert + \varepsilon\right\}$即可。

（3） **唯一性**：收敛数列有且仅有一个极限。即若$x_n\rightarrow a$且同时$x_n\rightarrow b$，则必然有$a=b$。

（4） **有限韧性**：任意增加、删除、改变数列的**有限**项，不影响数列的敛散性和极限。

（5） **子列收敛性**：若$x_n\rightarrow a$，则$x_n$的任意子列也必然收敛到$a$.

> 可以用该定理的逆定理证明某些数列不收敛. 例如，如果数列$\{x_n\}$中可以找到一个发散子列，或者两个收敛到不同数的子列，则原数列必然不收敛.

### 多个数列极限的性质

（1-a）**保序性**：若$x_n\rightarrow a$，$y_n\rightarrow b$，且$a>b$，则从某一项开始，始终有$x_n>y_n$.

（1-b）**保序性**：若$x_n\rightarrow a$，$y_n\rightarrow b$，且从某一项开始始终有$x_n\geqslant y_n$，则$a\geqslant b$.

> **注意**：在保序性1-a中，必须是**严格大于**的关系，如果换成大于等于则未必成立（等号很容易找到反例）。而在保序性1-b中，必须是**大于等于**的关系。因为即使$x_n$的每一项都严格大于$y_n$，二者仍可能收敛到同一极限.

(sqz_thm)=
（2）**夹逼定理**：若数列$\{x_n\}$、$\{y_n\}$和$\{z_n\}$满足，从某一项开始始终有$x_n\leqslant y_n\leqslant z_n$，且$\lim x_n = \lim z_n = a$，则$y_n$也收敛至$a$.

（3）**四则运算**：若$x_n\rightarrow a$且$y_n\rightarrow b$，则$cx_n\pm dy_n\rightarrow ca+db$, $x_ny_n\rightarrow ab$；如果能保证$y_n\neq 0$和$b\neq 0$，则还可以有$\displaystyle \frac{x_n}{y_n}\rightarrow \frac{a}{b}$.

> **注意**：我们要求四则运算中的两个数列收敛到有限的数，即不包含无穷大量的情形。形如$\displaystyle\frac{0}{0}$、$\displaystyle\frac{\infty}{\infty}$、$0\cdot\infty$、$\infty\pm\infty$的形式称为**不定式**，它们有可能是无穷小量，可能是无穷大量，可能收敛到一个非0实数，也可能根本就没有极限。

## 收敛数列的判据和极限的求法 Finding the Limits

在涉及数列极限时，我们经常关心的问题有：

- 如何证明数列$\{x_n\}$的极限就是$a$？
- 已知数列$\{x_n\}$收敛，如何求它的极限？
- 在不知道数列$\{x_n\}$极限的情况下，如何判断一个数列是否收敛？

本节介绍一些数列收敛性的常用判定依据，和一些求极限的方法。

（1）**根据定义**：使用$\varepsilon-N$语言判据.

（2）**根据夹逼定理**：夹逼定理参考[上一节](sqz_thm)针对数列进行左右两个方向的放缩，如果两个新的数列收敛到同一个极限，则原数列也必然收敛到这个值。

> 一个推论是，如果$x_n\rightarrow +\infty$，且从某项开始$y_n \geqslant x_n$，则$y_n\rightarrow +\infty$。负无穷大的情况同理.

（3）**参考一些增长数列的大小关系**：粗略而言，我们有：

$$
(\log n)^k \prec n \prec n^k \prec a^n \prec n! \prec n^n,\quad k,a>1
$$

这里用$\prec$表示一种近似的大小关系：当$n$足够大时，这种不等关系总是成立的。在这个关系链中，左边和右边的比值总是趋于0，因此可以得到$\displaystyle \frac{\log n}{n^k}\rightarrow 0$、$\displaystyle \frac{n^k}{n!}\rightarrow 0$、$\displaystyle \frac{a^n}{n^n}\rightarrow 0$等结论，进一步，可以得到$\sqrt[n]{n}\rightarrow 1$等结论。

（4）**借助四则运算等**：参考上一节的内容，如果两个数列$\{x_n\}$和$\{y_n\}$收敛到有限的实数，则可以计算出其加减乘除得到的新的数列的极限。事实上，除了基础的加减乘除之外，我们还有其他运算规则适用：

- 如果$x_n\rightarrow a$，则$|x_n|\rightarrow |a|$.
- 如果$x_n\rightarrow a$，则$\mathrm{e}^{x_n}\rightarrow \mathrm{e}^a$.
- 如果$x_n\rightarrow a$且$x_n >0$，则$\log x_n\rightarrow \log a$.
- 如果$x_n\rightarrow a$且$n >0$，则$x^n \rightarrow a^n$.

（5）**柯西收敛准则**：如果数列$\{x_n\}$满足，对于任意$\varepsilon > 0$，总存在$N>0$，使得对于任意$n,m>N$，总有$|x_n-x_m|<\varepsilon$，则称这样的数列为**柯西列**。柯西列等价于收敛数列。

> - 柯西收敛准则是一种在不知道数列极限的前提下判定数列收敛的方法. 在后面的章节中，无穷级数和无穷积分等的收敛性往往使用柯西收敛准则来描述.
> - “柯西列等价于收敛数列”是描述实数系完备性的定理之一，详情可见本章最后一节.

（6）**单调有界数列**和e：如果数列$\{x_n\}$数列单调且有界，则其必然收敛. 具体而言，单调递增且有上界的数列收敛到其上确界；单调递减且有下界的数列收敛到其下确界.
> - “单调有界数列必收敛”也是描述实数系完备性的定理之一.
> - 一个重要的例子是数列$\displaystyle x_n=\left(1+\frac{1}{n}\right)^n$，这是一个递增且有上界的数列，其极限正是我们所熟知的无理数$\mathrm{e}$. 基于这一极限，可以得到诸如$\displaystyle \left(\frac{an+b}{cn+d}\right)^{en+f}$形式的数列极限.
> - $\mathrm{e}$的另外一种形式是$\displaystyle \mathrm{e}=\lim 1+\frac{1}{1!}+\frac{1}{2!}+\cdots+\frac{1}{n!}$. 事实上我们有$\displaystyle \mathrm{e}=1+\frac{1}{1!}+\frac{1}{2!}+\cdots+\frac{1}{n!}+\frac{\theta_n}{n!n}, \theta_n\in(0,1)$，由此可以证明$\mathrm{e}$是无理数.

（7）**Stolz定理**：设$\{y_n\}$单调递增且趋于正无穷，且极限$\displaystyle \lim\frac{x_n-x_{n-1}}{y_n-y_{n-1}}$存在，则有

$$
\lim\frac{x_n}{y_n}=\lim\frac{x_n-x_{n-1}}{y_n-y_{n-1}}
$$


## 实数理论 Theories of Real Numbers

### 常见数集及其性质

迄今为止我们接触过了自然数集$\mathbb{N}$/正整数集$\mathbb{N}^{+}$、整数集$\mathbb{Z}$、有理数集$\mathbb{Q}$、无理数集、实数集$\mathbb{R}$等集合. 除了集合外，我们还会关心定义在集合上的二元关系（如大于、小于、等于）和二元运算（如四则运算）. 此外，也有一些常见数集和二元关系/运算的性质：

- 二元关系：例如，大于和小于具有**三歧性**（设$a,b\in\mathbb{X}$，则二者的关系必然属于$a>b$、$a=b$和$a < b$三者中的一种）、传递性；大于等于和小于等于具有传递性、反对称性、自反性等.
- 二元运算：例如，加法和乘法的交换性、结合性、分配性，加法的单位元（0）和逆元（相反数）、乘法的单位元（1）和逆元（倒数）.
- 在讨论二元运算前，首先需要验证其是否在数集上具有**封闭性**. 对于二元运算$\circ$和$a,b\in\mathbb{X}$，若$a\circ b$也在$\mathbb{X}$内，则称数集$\mathbb{X}$对运算$\circ$是封闭的. 例如，自然数集对加法和乘法封闭，但是对减法和除法不封闭；整数集对加、减、乘封闭，对除法不封闭；无理数集对加减乘除都不封闭；有理数集和实数集对加减乘除均封闭.

如果重点比较$\mathbb{Z}$、$\mathbb{Q}$和$\mathbb{R}$三个集合，我们的“直观感受”是：有理数比整数更加“密集”，而实数比有理数更加“密集”. 如果用严格的数学语言来描述，对于第一个“更密集”，是因为有理数集具有**稠密性**；对于第二个“更密集”，是因为实数具有**完备性**.

- **稠密性**：对$\forall a,b\in\mathbb{X}$且$a<b$，必然$\exists c\in\mathbb{X}$，使得$a<c<b$，则称数集$\mathbb{X}$是稠密的.

显然，两个相邻的整数间是没有第三个整数的，故整数集不具备稠密性. 有理数和实数都具有稠密性，而实数特有的性质则是完备性. 完备性的描述可以用下一小节的几个定理来描述.

### 实数的完备性

下面几个定理用来描述实数的完备性，他们彼此等价，可以互相导出：

（1）**戴德金（Dedekind）分割原理**：将实数集*划分*为两个集合$A$和$B$，使得$A$中的任意元素均小于$B$中的任意元素，则总存在着一个数（分界数），使得其要么是$A$的最大值，要么是$B$的最小值.

> - “划分”或者分割是指$A$和$B$不相交，且并集为$\mathbb{R}$. 即任何实数必然处于其中一个集合中. 这样的一个分割记为$A|B$.
> - 把有理数集划分为$A=\{x\in\mathbb{Q}:x^2<2 \text{或}x<0\}$和$B=\{x\in\mathbb{Q}:x^2>2 \text{且}x>0\}$，则容易验证$A|B$是有理数集的一个分割（任意有理数，其平方要么大于2，要么小于2，不可能等于2，则必然位于二者其一）. 但是，$A$没有最大值，$B$没有最小值，不符合Dedekind分割原理，所以有理数不具备完备性.

（2）**柯西（Cauchy）收敛定理**：柯西列是收敛的. 柯西列的定义见上一节.

（3）**确界定理**：有上界的集合必有上确界，有下界的集合必有下确界.

（4）**单调收敛定理**：单调有界数列必收敛.

（5）**聚点定理**：也称为Bolzano-Weierstrass定理，有界数列必有收敛子列. 一种等价叙述是，有界的无穷点集总有聚点.

> **聚点**有三种等价的定义方式，设$A$是集合，$x$是某个点（数字），则$x$是$A$的聚点当且仅当：
> 
> - 存在$A$中的一个数列收敛到$x$；
> - 任意一个$x$的邻域$N(x)$（即包含$x$的区间），都包含**至少一个**相异于$x$的$A$中的点.
> - 任意一个$x$的邻域$N(x)$（即包含$x$的区间），都包含无数个$A$中的点.
> 
> 注意，$x$是$A$的聚点并不要求$x$一定在$A$内.

（6）**闭区间套定理**：若$\{[a_n,b_n]\}_{n=1}^{\infty}$满足$[a_1,b_1]\subset[a_2,b_2]\subset\cdots [a_n,b_n]\subset\cdots$，则称$\{[a_n,b_n]\}_{n=1}^{\infty}$是一个闭区间套. 如果$\lim (b_n-a_n)=0$，则$\displaystyle \bigcap_{n=1}^{\infty}[a_n,b_n]$中包含唯一的一个点.

（7）**有限覆盖定理**：若闭区间$[\alpha,\beta]$和开区间族$\{(a_n,b_n)\}_{n=1}^{\infty}$ 满足 $\displaystyle[\alpha,\beta]\subset\bigcup_{n=1}^{\infty}(a_n,b_n)$，则必然能从开区间族中选择**有限个**开区间，使得$\displaystyle[\alpha,\beta]\subset \bigcup_{k=1}^{M}(a_{n_k},b_{n_k})$.