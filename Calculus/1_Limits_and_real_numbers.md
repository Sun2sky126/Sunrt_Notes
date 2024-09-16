# 数列极限与实数 Limits of Sequences & Real Numbers

## 数列极限的定义

对于数列$\{x_n\}_{n=1}^{\infty}$，如果存在$l\in\mathbb{R}$，使得对于任意$\varepsilon>0$，总能找到一个对应的$N$，使得对于任意满足$n>N$的$x_n$，都有$\vert x_n-l\vert <\varepsilon$，则称数列$\{x_n\}_{n=1}^{\infty}$**收敛**（到$l$），或者说数列$\{x_n\}_{n=1}^{\infty}$趋于$l$，或称$l$是数列$\{x_n\}_{n=1}^{\infty}$的极限，记为

$$
\lim_{n\rightarrow\infty}x_n = l\quad\text{或}\quad x_n\rightarrow l,\quad n\rightarrow\infty
$$

对于数列而言，在研究极限时仅考虑$n\rightarrow\infty$的情形，这一点和后面要讲到的函数的极限是不同的。因此我们可以更精简地记为$\displaystyle \lim x_n = l$和$x_n\rightarrow l$.

> - 直白地说，上面的定义是在描述：通过选择合适的$N$，我们可以将$\vert x_n - l\vert$控制到**任意小**. 即无论给定一个多么小的正数$\varepsilon$，总能找到若干合适的$N_\varepsilon$，从而将数列在超过$N_\varepsilon$的部分严格地控制在区间$(l-\varepsilon, l+\varepsilon)$以内.
> - 我们用$N_\varepsilon$而不是$N(\varepsilon)$，来澄清$N$和$\varepsilon$并不是一个严格的映射（函数）关系。对于每一个$\varepsilon$，我们有不止一种选择$N$的方式。假如我们找到了一个合适的$N^\star_\varepsilon$，则显然$N^\star_\varepsilon+1$、$N^\star_\varepsilon+4$甚至$N^\star_\varepsilon+10000$等也可以作为$N_\varepsilon$的选取方式。

对于数列$\{x_n\}_{n=1}^{\infty}$，只要能找到符合上述定义的$l\in\mathbb{R}$，则称其为**收敛**(convergent)的，否则是**发散**(divergent)的。

## 无穷小量和无穷大量

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

## 极限的相关性质 Properties of Limits

### 单个数列极限的性质

（1） **保序性、保号性**：假定$\lim x_n = a$且$a > p$，则从某一项开始（或者说，存在一个$N_p$，使得对于任意的$n>N_p$），总有$x_n>p$。同理，若$a < q$，则从某一项开始，总有$x_n < q$。是为极限的**保序性**。

> 证明思路是很直接的：以$a>p$为例，只需要取一个足够小的$\varepsilon$满足$a-\varepsilon>p$（例如可以取$\displaystyle \varepsilon=\frac{a-p}{2}$）。则对任意$n>N_\varepsilon$，总有$x_n>a-\varepsilon>p$。另一种情况同理。

特别地，当$a>0$时，可以取$p=0$；当$a<0$时，可以取$q=0$。即：若数列趋于一个正数，则从某一项开始数列恒正；若数列趋于一个负数，则从某一项开始数列恒负。是为数列的**保号性**。

（2） **有界性**：收敛数列必有界。即若$\{x_n\}$收敛到$a$，则存在$M>0$，使得对于**所有**$x_n$，均有$\vert x_n\vert \leqslant M$.

> 任意取$\varepsilon$和一个对应的$N_\varepsilon$，则对于$n>N_\varepsilon$的部分，有$\vert x_n \vert < \vert a\vert + \varepsilon$；对于$1\leqslant n \leqslant N_\varepsilon$的部分，这$N_\varepsilon$个有限的$\vert x_n \vert$中总能照到一个最大值，令$\displaystyle M=\max\left\{\max_{1\leqslant n\leqslant N_\varepsilon}|x_n|, \vert a\vert + \varepsilon\right\}$即可。

（3） **唯一性**：收敛数列有且仅有一个极限。即若$x_n\rightarrow a$且同时$x_n\rightarrow b$，则必然有$a=b$。

### 多个数列极限的性质