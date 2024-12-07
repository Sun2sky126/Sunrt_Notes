# 鞅 Martingales

## 鞅的概念 Concepts on Martingales

### 基本定义

如果一个随机过程$\{X_n: n\in\mathbb{N}^{+}\}$满足，对$\forall n\in\mathbb{N}^{+}$，都有

- $\mathbf{E}\left[|X_n|\right] < \infty$
- $\mathbf{E}\left[X_{n+1}|X_n,\cdots,X_1\right] = X_n$

则称其是一个**鞅**（martingale）. 

```{tip}

事实上，在上面的定义中，如果条件概率中的条件不仅含有$X_n$，还含有其他的随机变量$Z$，那么其仍然是一个鞅.

如果$\mathbf{E}\left[X_{n+1}|X_n,\cdots,X_1, Z\right] = X_n$，那么
$$
\begin{align*}
\mathbf{E}\left[X_{n+1}|X_n,\cdots,X_1\right] & = \mathbf{E}\left[\mathbf{E}\left[X_{n+1}|X_n,\cdots,X_1, Z\right]|X_n,\cdots,X_1\right] \\
& = \mathbf{E}\left[X_{n}|X_n,\cdots,X_1\right] \\
& = X_n
\end{align*}
$$

---

上面的推导用到了条件期望的这一性质：因为有$\mathbf{E}[X] = \mathbf{E}[\mathbf{E}[X|Y]]$，那么再套一层条件Z，就有$\mathbf{E}[X|Z] = \mathbf{E}[\mathbf{E}[X|Y,Z]|Z]$


```
有时，我们也会借助另外一个过程$\{Y_n: n\in\mathbb{N}^{+}\}$来观察$\{X_n\}$，如果满足：

- $\mathbf{E}\left[|X_n|\right] < \infty$
- $\mathbf{E}\left[X_{n+1}|Y_n,\cdots,Y_1\right] = X_n$

则称$\{X_n\}$是一个*关于*$\{Y_n\}$的鞅. 

### 性质

（1）鞅的运算：如果$\{X_n\}$和$\{Y_n\}$是（关于$\{Z_n\}$）的鞅，那么$\{X_n\pm Y_n\}$也是（关于$\{Z_n\}$）的鞅. 若两个过程相互独立，那么$\{X_nY_n\}$也是（关于$\{Z_n\}$）的鞅.

（2）鞅中每一个随机变量的期望都是相同的. 也就是说，如果$\{X_n\}$是（关于$\{Y_n\}$）是鞅，那么有$\mathbf{E}[X_{n+1}]=\mathbf{E}[X_{n}]=\cdots=\mathbf{E}[X_1]$.

> 我们有 $\mathbf{E}[X_{n+1}]=\mathbf{E}[{\mathbf{E}\left[X_{n+1}|Y_n,\cdots,Y_1\right]}]=\mathbf{E}[X_n]$，然后就可以递推下去.

（3）在第$n$时刻，观测的$X_n$、$X_{n+1}$及之后的每一个随机变量$X_{n+k}$，其**条件期望**均等于$X_n$. 也就是说，对于$k=0,1,2,\cdots$，均有$\mathbf{E}[X_{n+k}|Y_n,\cdots,Y_1]=X_n$. 也就是说，我们站在“当前”，看到未来的一切均有相同的数学期望.

> - 当$k=0$时，因为$X_n=\mathbf{E}\left[X_{n+1}|Y_n,\cdots,Y_1\right]$是$Y_1,\cdots,Y_n$的函数，所以有$\mathbf{E}[X_{n}|Y_n,\cdots,Y_1]=X_n$.
> - 当$k=1$时，这就是鞅的定义.
> - 对$k>1$的情形，使用归纳法. 假设等式对$k$成立，那么对$k+1$，有：
> $$\begin{align*} & \mathbf{E}[X_{n+k+1}|Y_n,\cdots,Y_1] \\ = &\mathbf{E}[\mathbf{E}[X_{n+k+1}|Y_{n+k},\cdots,Y_1]|Y_n,\cdots,Y_1] \\ = &\mathbf{E}[X_{n+k}|Y_n,\cdots,Y_1] \\ = & X_n\end{align*}$$

### 鞅的实例

（1）独立同分布的0均值随机变量之和：若$Y_n$ i.i.d.且任意$n$有$\mathbf{E}[Y_n]=0$，记$X_n=\displaystyle\sum_{k=1}^{n}Y_k$，则$\{X_n\}$是关于$\{Y_n\}$的鞅.

（2）Doob鞅：设有随机过程$\{Y_n\}$和某个随机变量$X$，定义$Z_n=\mathbf{E}[X|Y_n,\cdots,Y_1]$，则$\{Z_n\}$是关于$\{Y_n\}$的鞅.

> 我们有 
> $$\begin{align*}
\mathbf{E}[Z_{n+1}|Y_n,\cdots, Y_1] & = \mathbf{E}[\mathbf{E}[X|Y_{n+1},\cdots,Y_1]|Y_n,\cdots, Y_1] \\
& = \mathbf{E}[X|Y_n,\cdots, Y_1] \\
& = Z_n
\end{align*}$$

## 停时 Stopping Times

### 停时的概念

我们设$N$是一个正整数型随机变量（允许其取到无穷），$\{X_n\}$是一个随机过程. 如果事件$\{N=n\}$的发生与否可以完全由$X_1,\cdots,X_n$来决定，那么称$N$是随机过程$\{X_n\}$的一个**停时**（stopping time）. 更形式化一点，"事件$\{N=n\}$可以完全由$X_1,\cdots,X_n$来决定"就是在说，示性函数$I_{N=n}$是$X_1,\cdots,X_n$的函数.

> - 例如，每轮游戏随机赚取10元或者0元，并设定第$N$轮可以首次赚满100元，其中$N$是随机变量. 考虑事件$\{N=n\}$，那么只需要知道$X_1,\cdots,X_n$，即前$n$轮的收益，就可以看出事件$\{N=n\}$是否成立.
> - 但是，如果我们稍作修改，设定第$N+1$轮可以首次赚满100元，那么由$X_1,\cdots,X_n$是不能看出事件$\{N=n\}$是否成立的. 因为如果前$n$轮加在一起刚好赚够了90元，那么第$n+1$轮能否赚够100元就完全取决于$X_{n+1}$了，仅凭$X_1,\cdots,X_n$是不能作出判断的.

上面的定义中，$\{N=n\}$可以由$X_1,\cdots,X_n$完全决定，其实事件$\{N < n\}$、$\{N \leqslant n\}$、$\{N > n\}$和$\{N \geqslant n\}$也可以由$X_1,\cdots,X_n$来确定.

停时的一个性质是，如果$M$、$N$都是$\{X_n\}$的停时，那么$M+N$、$M\wedge N:=\min\{M,N\}$和$M\vee N:=\max\{M,N\}$也是$\{X_n\}$的停时.

### 鞅的停时定理：总述

任何一个随机过程都可以定义它的一个停时，下面我们着重分析鞅的停时. 下面的讨论基于下面的预设：

- $\{X_n\}$是一个鞅，$N$是$\{X_n\}$的一个停时.
- 或者，$\{X_n\}$是一个关于$\{Y_n\}$的鞅，$N$是$\{Y_n\}$的一个停时.

那么，根据停时的定义，$I_{N=n}$是$X_n,\cdots,X_1$或者$Y_n,\cdots,Y_1$的函数，因而对于任意随机变量$Z$，有

$$
\mathbf{E}[ZI_{N=n}|Y_n,\cdots,Y_1]=I_{N=n}\mathbf{E}[Z|Y_n,\cdots,Y_1]
$$

> 根据上述讨论，这一性质当然对$I_{N < n}$等也成立.

我们已经知道对于鞅，有$\mathbf{E}[X_1]=\cdots=\mathbf{E}[X_n]$，那么我们当然关心，如果以停时这一随机变量为下标，是否也有

$$
\mathbf{E}[X_N]=\mathbf{E}[X_1]
$$

这就是**停时定理**. 下面讨论，停时定理的条件应该是什么，即$\{X_n\}$和$N$应该满足什么样的条件使得上述等式成立.

### 鞅的停时定理：条件

我们来首先看一个停时定理的“简化版本”，考虑$N\wedge n$这一下标，即只考虑$N$取值在$[1,n]$之间的情形，或者说考虑$N$是**有限**的，我们就得到了一个简单版本的停时定理：

$$
\mathbf{E}[X_1] = \mathbf{E}[X_{N\wedge n}] = \mathbf{E}[X_n]
$$

```{admonition} 证明
:class: dropdown, tips

$$\begin{align*}
\mathbf{E}[X_{N\wedge n}] & = \mathbf{E}[\mathbf{E}[X_{N\wedge n}|N]]=\sum_{k=1}^{+\infty}\mathbf{E}[X_{N\wedge n}|N=k]p_N(k) \\
& = \sum_{k=1}^{+\infty}\mathbf{E}[X_{k\wedge n}]p_N(k) \\
& = \sum_{k=1}^{n}\mathbf{E}[X_k]p_N(k) + \sum_{k=n+1}^{+\infty}\mathbf{E}[X_n]p_N(k) \\
& = \mathbf{E}[X_n]\sum_{k=1}^{+\infty}p_N(k) = \mathbf{E}[X_n] = \mathbf{E}[X_1]
\end{align*}$$

其中，最后一行用到了对于$\forall 1\leqslant k\leqslant n$有$\mathbf{E}[X_k]=\mathbf{E}[X_n]$的性质. 而后面的和式，由概率的性质得知所有$k$对应的概率加在一起为1. 这里$p_N(k)$即表示$P(\{N=k\})$或者记为$P(N=k)$.

```

也就是说，如果把$N$限制在有限的范围（$n$以内），那么结论是很显然的. 但实际上，$N$并非一个有界的随机变量，而是有可能取到无穷. 对无穷情形的处理是比较棘手的，因为为了保证求和的收敛性，有必要对$\{X_n\}$和$N$加上一些条件的限制.

我们仍然类比上面的证明过程进行一些分析，那么有

$$\begin{align*}
\mathbf{E}[X_{N}] & = \mathbf{E}[\mathbf{E}[X_N|N]]=\sum_{k=1}^{+\infty}\mathbf{E}[X_{N}|N=k]p_N(k) \\
& = \sum_{k=1}^{+\infty}\mathbf{E}[X_{k}]p_N(k) 
\end{align*}$$

所以，首先要保证的第一个条件是：哪怕是对于任意大的$k$，应保证$\mathbf{E}[X_k]$存在. 我们假设这个条件满足，那么继续下去：

$$\begin{align*}
\mathbf{E}[X_{N}] & = \sum_{k=1}^{+\infty}\mathbf{E}[X_{k}]p_N(k) = \mathbf{E}[X_n]\sum_{k=1}^{+\infty}p_N(k)
\end{align*}$$

由级数收敛的条件，应满足$\displaystyle \lim_{k\to+\infty}p_N(k)=0$，或者记为$P(N=+\infty)=0$以及$P(N<+\infty)=1$.


## 上鞅和下鞅 Supermartingales & Submartingales

### 上下鞅的定义

上下鞅的定义可以视为对鞅定义的推广，将等号关系改为不等关系. 如果随机过程$\{X_n\}$和$\{Y_n\}$满足：

- $\mathbf{E}[|X_n|] < \infty$
- $\mathbf{E}[{X_{n+1}|Y_n,\cdots,Y_1}]\leqslant X_n$

则称$\{X_n\}$是一个（关于$\{Y_n\}$）的**上鞅**（supermartingale）. 类似于鞅，上鞅也有相似的性质：

（1）若$\{X_n\}$和$\{Y_n\}$是上鞅，则$\{X_n\pm Y_n\}$也是上鞅. 若它们非负且相互独立，则$\{X_nY_n\}$也是上鞅.

（2）若$\{X_n\}$是上鞅，则$\{X_n\}$的期望随着$n$的增加而单调递减.

（3）若$\{X_n\}$是上鞅，则$\forall k\in\mathbb{N}^{+}$，均有$\mathbf{E}[X_{n+k}|Y_n,\cdots,Y_1]\leqslant X_n$.

完全对偶过来我们就得到了下鞅的定义. 如果随机过程$\{X_n\}$和$\{Y_n\}$满足：

- $\mathbf{E}[|X_n|] < \infty$
- $\mathbf{E}[{X_{n+1}|Y_n,\cdots,Y_1}]\geqslant X_n$

则称$\{X_n\}$是一个（关于$\{Y_n\}$）的**下鞅**（submartingale）. 同样下鞅也有类似的上面三条性质.

> - 要记清："上"鞅是递减的，"下"鞅是递增的.
> - 由于此时不再有$X_n$是$Y_n,\cdots,Y_1$的函数，故性质（3）中我们限制$k\neq 0$.

### 上下鞅的构造

构造上鞅和下鞅也有很多方式，这里介绍一种基于**鞅**和函数凹凸性的构造方式.

设$\varphi(x)$是一下凸函数，即满足$\displaystyle \varphi\left(\sum_{i=1}^{n}a_i x_i\right)\leqslant \sum_{i=1}^{n}a_i\varphi(x_i)$，其中$a_i$是和为1的非负数. 那么由期望的Jensen不等式，有$\varphi(\mathbf{E}[X])\leqslant \mathbf{E}[\varphi(X)]$，这一不等式对条件期望同样成立. 那么针对下凸函数$\varphi$我们有结论——如果$\{X_n\}$是鞅，那么$\{\varphi(X_n)\}$是下鞅.

> 我们有$\mathbf{E}[\varphi(X_{n+1})|Y_n,\cdots,Y_1]\geqslant\varphi(\mathbf{E}[X_{n+1}|Y_n,\cdots,Y_1])=\varphi(X_n)$

同样，对于上凸函数$\psi(x)$，有$\mathbf{E}(\psi(X))\leqslant\psi(\mathbf{E}[X])$. 因此如果$\{X_n\}$是鞅，那么$\{\psi(X)\}$是上鞅.

```{tip}

随手画一个圆，"上"半圆是"上"凸的，对应上鞅；"下"半圆是"下"凸的，对应下鞅.

```

### 分解定理

### 上穿与下穿不等式

## Doob定理和Azuma不等式