# 布朗运动 Brownian Motions

## 布朗运动的概念 Concepts on Brownian Motions

### 定义

布朗运动可以视为随机游走的一种极限情形. 考虑这样一个随机游走过程：每经过一段时间$\Delta t$，就等概率地向左或者向右移动$\Delta x$的距离. 为此我们定义一组独立同分布的随机变量$X_i$，有$P_{X_i}(+1)=P_{X_i}(-1)=\dfrac{1}{2}$，来标记每次是向左还是向右移动（例如向右定义为$+1$而向左定义为$-1$），那么在时间$t$处物体的位置可以记为

$$
X(t)=(X_1+X_2+\cdots + X_{\lfloor t/\Delta t\rfloor})\Delta x
$$

这是$\left\lfloor\dfrac{t}{\Delta t}\right\rfloor$个Bernoulli随机变量的叠加，因此可以认为服从二项分布. 对于单个$X_i$，有$\mathbf{E}[X_i]=0$而$\mathrm{var}(X_i)=1$，于是有

$$
\mathbf{E}[X(t)]=0\quad \mathrm{var}(X(t))=(\Delta x)^2\left\lfloor\frac{t}{\Delta t}\right\rfloor
$$

现在考虑$\Delta t\to 0$的极限过程，如果$\Delta x$和$\Delta t$满足$\displaystyle\lim_{\Delta t\to 0}\frac{(\Delta x)^2}{\Delta t}=c^2\neq 0$，就可以得到$\mathrm{var}(X(t))=c^2t$. 并且在这一极限过程中，二项分布将变为正态分布，于是得到

$$
X(t)\sim\mathcal{N}(0,\,c^2t)
$$

> 如果$\displaystyle\lim_{\Delta t\to 0}\frac{(\Delta x)^2}{\Delta t}=0$，就得到了$\mathrm{var}(X(t))=0$的平凡情形. 如果$\displaystyle\lim_{\Delta t\to 0}\frac{(\Delta x)^2}{\Delta t}=\infty$，就变成了一种难以处理的情形，此时$X(t)$的方差为无穷大.

更进一步，如果结合随机游走的性质，我们可以知道$X(t)$还是一个独立增量过程和平稳增量过程. 这样就得到了布朗运动. 下面是一个具体的定义：

如果随机过程$\{X(t), t\geqslant 0\}$满足：

- $X(0)=0$
- $X(t)$是独立增量过程，也是平稳增量过程
- 对任意$s\geqslant 0$，有$X(s+t)-X(s)\sim\mathcal{N}(0,\, c^2t)$.

则称其为**布朗运动**（Brownian motions）或者**维纳过程**（Wiener process）. 有时会将$c=1$的情形称为**标准布朗运动**.

> 布朗最早用这一过程来描述微粒的不规则运动，而后维纳在论文中给定了这一过程的正式定义和分析.

### 有限维联合分布

由于布朗运动的独立增量和平稳增量特性，我们可以轻易地得到有限个时刻$t_1,\cdots,t_n$时$X(t_i)$的联合分布函数. 设$B(t)$是一个布朗运动，下面考察$B(t_1),\cdots, B(t_n)$的概率密度函数，则

$$
\begin{align*}
& f_{B(t_1),\cdots, B(t_n)}(x_1,\cdots,x_n) \\
= & f_{Y(t_1),\cdots, Y(t_n)}(x_1, x_2-x_1,\cdots, x_n-x_{n-1}) \\
= & \prod_{k=1}^{n}f_{Y(t_k)}(x_k-x_{k-1}) \\
= & \prod_{k=1}^n\mathcal{N}(x_k-x_{k-1}|0,\, c^2(t_k-t_{k-1})) \\
= & \prod_{k=1}^n \frac{1}{c\sqrt{2\pi (t_k-t_{k-1})}}\exp\left\{-\frac{(x_k-x_{k-1})^2}{2c^2(t_k-t_{k-1})}\right\}
\end{align*}
$$

这里规定$x_0=t_0=0$，故$B(t_0)=0$，且$Y(t_k):=B(t_k)-B(t_{k-1})$，$\mathcal{N}(x|\mu,\sigma^2)$表示正态分布的PDF. 于是由布朗运动的独立性和平稳增量特性可以得到上述形式. 类似地，我们也可以得到一些其他结论，例如给定$B(t_1)=x_1$，那么对于另一个时刻$t_2>t_1$有

$$
f_{B(t_2)|B(t_1)}(x_2|x_1)=\mathcal{N}(x_2-x_1|0,\, c^2(t_2-t_1))
$$

### 性质