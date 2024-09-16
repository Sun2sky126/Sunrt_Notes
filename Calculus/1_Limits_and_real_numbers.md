# 数列极限与实数 Limits of Sequences & Real Numbers

## 数列极限的定义

对于数列$\{x_n\}_{n=1}^{\infty}$，如果存在$l\in\mathbb{R}$，使得对于任意$\varepsilon>0$，总能找到一个对应的$N$，使得对于任意满足$n>N$的$x_n$，都有$\vert x_n-l\vert <\varepsilon$，则称数列$\{x_n\}_{n=1}^{\infty}$**收敛**（到$l$），或者说数列$\{x_n\}_{n=1}^{\infty}$趋于$l$，或称$l$是数列$\{x_n\}_{n=1}^{\infty}$的极限，记为

$$
\lim_{n\rightarrow\infty}x_n = l\quad\text{或}\quad x_n\rightarrow l,\quad n\rightarrow\infty
$$

对于数列而言，在研究极限时仅考虑$n\rightarrow\infty$的情形，这一点和后面要讲到的函数的极限是不同的。因此我们可以更精简地记为$\displaystyle \lim x_n = l$.

> - 直白地说，上面的定义是在描述：通过选择合适的$N$，我们可以将$\vert x_n - l\vert$控制到**任意小**. 即无论给定一个多么小的正数$\varepsilon$，总能找到若干合适的$N_\varepsilon$，从而将数列在超过$N_\varepsilon$的部分严格地控制在区间$(l-\varepsilon, l+\varepsilon)$以内.
> - 我们用$N_\varepsilon$而不是$N(\varepsilon)$，来澄清$N$和$\varepsilon$并不是一个严格的映射（函数）关系。对于每一个$\varepsilon$，我们有不止一种选择$N$的方式。假如我们找到了一个合适的$N^\star_\varepsilon$，则显然$N^\star_\varepsilon+1$、$N^\star_\varepsilon+4$甚至$N^\star_\varepsilon+10000$等也可以作为$N_\varepsilon$的选取方式。

对于数列$\{x_n\}_{n=1}^{\infty}$，只要能找到符合上述定义的$l\in\mathbb{R}$，则称其为**收敛**(convergent)的，否则是**发散**(divergent)的。

## 无穷小量和无穷大量

如果数列$\{x_n\}_{n=1}^{\infty}$的极限是0，则其又称为**无穷小量**，记作
$$
x_n = o(1),\quad n\rightarrow\infty
$$

因此，数列$\{x_n\}_{n=1}^{\infty}$收敛至$l$这一命题**等价于**：$x_n-l$是无穷小量。

