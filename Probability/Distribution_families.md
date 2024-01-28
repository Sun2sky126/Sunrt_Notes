# 分布族 Distribution Families

## 常见离散型随机变量分布

### 均匀分布 Unifrom Distribution
称随机变量$X$服从$[a,b]$上的**均匀分布**，记为$X\sim\mathcal{U}(a,b)$，如果$X$仅能取到区间$[a,b]$内的所有整数值，且取到每个值的概率相等。其PMF为
$$
p_X(x|a,b)=\left\{
\begin{align*}
&\frac{1}{b-a+1}, &\quad x\in [a,b] \\
&0, &\quad \text{others.}  
\end{align*}
\right.
$$

均匀分布的期望为$\displaystyle\mathbb{E}[X]=\frac{a+b}{2}$，方差为$\displaystyle \mathrm{var}(X)=$。

> **均值和方差的推导**
> $$ \mathbb{E}[X]=\sum_{x=a}^{b}x\frac{1}{b-a+1} = \frac{1}{b-a+1}\frac{(a+b)(b-a+1)}{2}=\frac{a+b}{2}$$
> $$ \begin{align*}\mathrm{var}(X) \end{align*}$$


### 超几何分布 Hypergeometric Distribution

假设一个罐子里有$N$个除颜色外完全一致的小球，其中有$M$个是红色的，其余是蓝色的。从中随机选择$K$个小球，则其中红球的数目$X$服从**超几何分布**，记作$X\sim \mathcal{H}(N,M,K)$。其PMF为
$$
p_X(x|N,M,K)=\frac{\displaystyle \binom{M}{x}\binom{N-M}{K-x}}{\displaystyle\binom{N}{K}}
$$

### 伯努利分布和二项分布 Bernoulli Distribution & Binomial Distribution

### 泊松分布 Poisson Distribution

### 负二项分布和几何分布 Negative Binomial Distribution & Geometric Distribution

## 常见连续型随机变量分布

### 均匀分布

### 伽马分布、卡方分布和指数分布 Gamma Distribution, Chi-square Distribution & Exponential Distribution

对于一个函数$f(x)$，如果能满足$f(x)\geqslant 0$且$\displaystyle \int_{-\infty}^{\infty}f(x)\mathrm{d}x<+\infty$，则可以将
$$
\frac{f(x)}{\displaystyle\int_{-\infty}^{+\infty}f(x)\mathrm{d}x}$$
作为一个合法的PDF。为此，考虑Gamma函数$\displaystyle \Gamma(\alpha)=\int_{0}^{+\infty}t^{\alpha-1}\mathrm{e}^{-t}\mathrm{d}t$，我们已经知道了它的一些性质，如$\Gamma(\alpha+1)=\alpha\Gamma(\alpha)$，对整数$n$有$\Gamma(n)=(n-1)!$，$\Gamma(1)=1$等。对其进行推广，定义$\Gamma(\alpha,\beta)$为
$$
\Gamma(\alpha,\beta)=\int_0^{+\infty}t^{\alpha-1}\mathrm{e}^{-\beta t}\mathrm{d}t=\beta^{-\alpha}\Gamma(\alpha)
$$
并进一步定义PDF为
$$
f_X(x|\alpha,\beta)=\frac{x^{\alpha-1}\mathrm{e}^{-\beta x}}{\beta^{-\alpha}\Gamma(\alpha)},\quad x>0,\quad\alpha,\beta>0$$
该分布称为**伽马分布**，记作$X\sim\Gamma(\alpha,\beta)$.

> **伽马分布期望和方差的推导**
> $$\mathbb{E}[X]=\frac{1}{\beta^{-\alpha}\Gamma(\alpha)}\int_0^{+\infty}x^{\alpha}\mathrm{e}^{-\beta x}\mathrm{d}x=\frac{\Gamma(\alpha+1,\beta)}{\beta^{-\alpha}\Gamma(\alpha)}=\frac{\beta^{-\alpha-1}\Gamma(\alpha+1)}{\beta^{-\alpha}\Gamma(\alpha)}=\frac{\alpha}{\beta}$$
> $$\mathbb{E}[X^2]=\frac{\Gamma(\alpha+2,\beta)}{\beta^{-\alpha}\Gamma(\alpha)}=\frac{\beta^{-\alpha-2}\Gamma(\alpha+2)}{\beta^{-\alpha}\Gamma(\alpha)}=\frac{\alpha(\alpha+1)}{\beta^2}$$
> $$\mathrm{var}(X)=\mathbb{E}[X^2]-\mathbb{E}[X]^2=\frac{\alpha}{\beta^2}$$