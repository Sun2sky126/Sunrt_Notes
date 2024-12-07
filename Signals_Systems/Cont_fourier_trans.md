# 连续时间信号的傅里叶变换 Fourier Transforms for Continuous Signals

## 周期信号的傅里叶级数 Fourier Series for Periodic Signals

### 傅里叶级数的定义

设$x(t)$是以$T$为最小正周期的周期信号，那么微积分课程已经告诉我们，$x(t)$可以写成一系列级数之和：

$$
x(t)=\sum_{k=-\infty}^{+\infty}a_k\mathrm{e}^{\mathrm{j}k\omega_0t}
$$

其中$\omega_0=\dfrac{2\pi}{T}$称为**基频**，同样地，$T$有时也会称为**基波周期**. 于是$x(t)$就被分解为了一系列信号的和：一个直流分量$a_0$、一对频率为$\omega_0$的周期信号，一对频率为$2\omega_0$的周期信号（称为2次谐波分量），……，一对$n\omega_0$的周期信号（n次谐波分量）的叠加，这是Fourier分析的核心所在.

上面的式子也可以写成

$$
\begin{align*}
x(t) & =a_0+\sum_{k=1}^{+\infty}a_k\mathrm{e}^{\mathrm{j}k\omega_0 t}+a_{-k}\mathrm{e}^{-\mathrm{j}k\omega_0 t} \\ 
&=a_0+\sum_{k=1}^{+\infty}b_k\cos(k\omega_0t)+c_k\sin(k\omega_0 t)
\end{align*}
$$

其中$b_k=a_k+a_{-k}$，$c_k=\mathrm{j}(a_k-a_{-k})$. 上式也可以使用辅助角公式，写为

$$
x(t) = a_0+\sum_{k=1}^{+\infty}A_k\cos(k\omega_0t+\varphi_k)
$$

这样我们就得到了周期信号的Fourier级数的三种等价表达方式. 出于一般性假设，我们这里让$x(t)$为*复数*信号，那么在上述表达式中，除了$k\omega_0 t$为实数外，其余诸系数$a_k$、$\varphi_k$等都是复数.

> 现实生活中，更常用的是实数信号$x(t)$. 对于实数信号，那么在后两种三角函数的表达式中，$a_0$、$b_k$、$c_k$、$A_k$和$\varphi_k$都是实数. 对于第一种复指数表达式，我们有$x^*(t)=\displaystyle\sum_{k=-\infty}^{+\infty}a_k^*\mathrm{e}^{-\mathrm{j}k\omega_0t}=\sum_{k=-\infty}^{+\infty}a_{-k}^{*}\mathrm{e}^{\mathrm{j}k\omega_0t}$，对比可得$a_k=a_{-k}^{*}$. 也就是说，**实信号的Fourier系数具有共轭对称性**. 这也能自洽地推出后面两个表达式的系数、振幅和相位都是实的. 关于虚实性的更多结论，可以参考后续章节.

### 傅里叶系数的求法

Fourier级数把信号分解为一系列**基**（basis）的线性组合，这些基可以记为$\{\phi_k(t)\}_{k=-\infty}^{+\infty}$，其中$\phi_k(t):=\mathrm{e}^{\mathrm{j}k\omega_0 t}$. 我们定义任意两个基的**内积**为$\displaystyle \langle\phi_m(t),\phi_n(t)\rangle := \int_{(T)}\phi_m(t)\phi_n^{*}(t)\mathrm{d}t$，不要忘记在复空间做内积时要取共轭. 其中$\displaystyle\int_{(T)}$代表在任意一个周期区间内积分，一般取$[0,T]$. 这组基显然是正交的，即

$$
\langle\phi_m(t),\phi_n(t)\rangle = T\delta_{mn}=\begin{cases}
T, & m=n \\
0, & m\neq n
\end{cases}
$$

```{admonition} 正交性的说明
:class: dropdown, tip

当$m=n$时，$\phi_m(t)\phi_n^{*}(t)=1$，故$\langle\phi_m(t),\phi_n(t)\rangle = \displaystyle\int_{(T)}1\mathrm{d}t=T$. 而当$m\neq n$时，有$\displaystyle \int_{(T)}\phi_m(t)\phi_n^{*}(t)\mathrm{d}t=\int_{(T)}\mathrm{e}^{\mathrm{j}(m-n)\omega_0 t}\mathrm{d}t=\left.\frac{1}{\mathrm{j}(m-n)\omega_0}\mathrm{e}^{\mathrm{j}(m-n)\omega_0 t}\right|_{0}^{T}=0$，最后一个等号是因为$\omega_0=\dfrac{2\pi}{T}$.

```

于是，我们就可以得到求出Fourier系数的方法：

$$
\textbf{Analysis Equation:}\quad a_n=\frac{1}{T}\left\langle x(t), \phi_n(t)\right\rangle = \frac{1}{T}\int_{(T)}x(t)\mathrm{e}^{-\mathrm{j}n\omega_0 t}\mathrm{d}t
$$

$$
\textbf{Synthesis Equation:}\quad x(t) = \sum_{k=-\infty}^{+\infty}a_k\mathrm{e}^{\mathrm{j}k\omega_0 t}\mathrm{d}t
$$

第一个方程给定了由信号求取Fourier系数$\{a_k\}
$的方法，称为**分析方程**；第二个方程给定了由Fourier系数恢复原信号的方法，称为**综合方程**. 我们也可以把这一过程记为

$$
x(t)\xrightarrow{\mathcal{FS}} \{a_k\}_{}
$$

$$
\{a_k\}\xrightarrow{\mathcal{FS}^{-1}}x(t) 
$$

```{admonition} 关于分析方程
:class: dropdown, tip

$$
\left\langle x(t), \phi_n(t)\right\rangle = \left\langle \sum_{k=-\infty}^{+\infty}a_k\mathrm{e}^{\mathrm{j}k\omega_0 t}, \phi_n(t)\right\rangle = \sum_{k=-\infty}^{+\infty}a_k\left\langle \phi_k(t), \phi_n(t)\right\rangle=Ta_n
$$

```

## 一般信号的傅里叶变换 Fourier Transforms for Normal Signals