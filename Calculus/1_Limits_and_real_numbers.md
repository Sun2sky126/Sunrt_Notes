# 数列极限与实数 Limits of Sequences & Real Numbers


## 数列极限的定义

对于数列$\{x_n\}_{n=1}^{\infty}$，如果存在$l\in\mathbb{R}$，使得对于任意$\varepsilon>0$，总能找到一个对应的$N$，使得对于任意满足$n>N$的$x_n$，都有$\vert x_n-l\vert <\varepsilon$，则称数列$\{x_n\}_{n=1}^{\infty}$**收敛**（到$l$），或者说数列$\{x_n\}_{n=1}^{\infty}$趋于$l$，或称$l$是数列$\{x_n\}_{n=1}^{\infty}$的极限，记为

$$
\lim_{n\rightarrow\infty}x_n = l\quad\text{或}\quad x_n\rightarrow l,\quad n\rightarrow\infty
$$

对于数列而言，在研究极限时仅考虑$n\rightarrow\infty$的情形，这一点和后面要讲到的函数的极限是不同的。因此我们可以更精简地记为$\displaystyle \lim x_n = l$.