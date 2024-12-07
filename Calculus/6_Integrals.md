# 一元函数积分学 Integration for Univariable Functions

## 原函数与不定积分 Primitive Functions & Indefinite Integrals

### 不定积分的定义与结构

对于某个函数$f$，如果存在另外一个函数$F$，使得$F$的导函数刚好是$f$，即$F'=f$，则称$F$是$f$的一个**原函数**（primitive functions, or antiderivative）. 如$x^2$和$x^2-6$都是$2x$的原函数. 不难发现，若$F$是$f$的一个原函数，则对于任意常数$C$，$F+C$也是$f$的一个原函数.

若$f$存在原函数，则其*所有*原函数的集合称为这个函数的**不定积分**（indefinite integrals），记为$\displaystyle \int f\mathrm{d}x$. 即

$$
\int f(x)\mathrm{d}x:=\{F(x):F'(x)=f(x)\}
$$

不难发现这个集合的结构：集合中的每个函数都相差一个常数$C$. 

> 若$F$是$f$的一个原函数，则$G=F+C$满足$G'=F'+0=f$也是$f$的一个原函数. 若$F$，$G$都是$f$的原函数，则$(F-G)'=f-f=0$，由上一章的结论可知$F$和$G$相差一个常数. 这样就证明了其充分性和必要性.

因此只要我们找到了$f$的一个原函数$F$，就可以找到其所有的原函数，这样不定积分也可以写作

$$
\int f(x)\mathrm{d}x=F(x)+C,\quad C\text{为任意常数}
$$

### 不定积分的计算

（一）常见函数的不定积分与运算法则

```{admonition} 一些常见函数的不定积分
:class: tip, dropdown

- 常数 $\displaystyle\int a\mathrm{d}x = ax+C$
- 幂函数（幂不为-1）$\displaystyle\int x^n\mathrm{d}x = \frac{x^{n+1}}{n+1}+C$
- 幂函数（幂为-1）$\displaystyle\int \frac{1}{x}\mathrm{d}x = \ln\vert x\vert+C$
- 指数函数 $\displaystyle\int a^x\mathrm{d}x = \frac{a^x}{\ln a}+C$
- 对数函数 $\displaystyle\int \ln x\mathrm{d}x = x\ln x-x+C$
- 三角函数：
- $\displaystyle\int \sin x\mathrm{d}x = -\cos x+C$
- $\displaystyle\int \cos x\mathrm{d}x = \sin x+C$
- $\displaystyle\int \tan x\mathrm{d}x = -\ln|\cos x|+C$
- $\displaystyle\int \cot x\mathrm{d}x = \ln|\sin x|+C$
- $\displaystyle\int \frac{1}{\sin^2 x}\mathrm{d}x = -\cot x+C$
- $\displaystyle\int \frac{1}{\cos^2 x}\mathrm{d}x = \tan x+C$
- 双曲三角函数：
- $\displaystyle\int \sinh x\mathrm{d}x = \cosh x+C$
- $\displaystyle\int \cosh x\mathrm{d}x = \sinh x+C$
- $\displaystyle\int \tanh x\mathrm{d}x = \ln\cosh x+C$
- 对于反三角函数和反双曲三角函数，我们更常用的形式是由它们的导函数推知其原函数，需要注意的是，反双曲三角函数可以有更直接的形式表达：
- $\displaystyle\int \frac{1}{\sqrt{1-x^2}}\mathrm{d}x = \arcsin x+C$
- $\displaystyle\int \frac{1}{1+x^2}\mathrm{d}x = \arctan x+C$
- $\displaystyle\int \frac{1}{\sqrt{x^2+1}}\mathrm{d}x = \mathrm{arcsinh}\,x+C=\ln\vert x+\sqrt{x^2+1}\vert+C$
- $\displaystyle\int \frac{1}{\sqrt{x^2-1}}\mathrm{d}x = \mathrm{arccosh}\,x+C=\ln\vert x+\sqrt{x^2-1}\vert+C$

```

（二）分部积分法与换元积分法

（三）一些特殊类函数的积分技巧

### 有理式的不定积分

### 根式有理函数的不定积分

### 三角有理函数的不定积分

考虑$\displaystyle \int R(\sin x, \cos x)\mathrm{d}x$，其中$R(u,v)$为关于$u$和$v$的有理函数.

此类问题有一种“万能”的代换方法，即令$t=\tan\dfrac{x}{2}$，此时$\sin x=\dfrac{2t}{1+t^2}$，$\cos x=\dfrac{1-t^2}{1+t^2}$，$\mathrm{d}x=\mathrm{d}(2\arctan t)=\dfrac{2}{1+t^2}\mathrm{d}t$. 于是原式变为

$$
R(\sin x,\cos x)\mathrm{d}x=R\left(\dfrac{2t}{1+t^2}, \dfrac{1-t^2}{1+t^2}\right)\dfrac{2}{1+t^2}\mathrm{d}t
$$

于是就变为了普通的有理式积分. 这一方法颇具有通用性，即适用于任何一种三角有理式，但是其计算代价往往也很大. 有些时候，我们可以采用更简单的换元法.

> 我们先引入如下的结论，考虑有理式$R(u,v)$：
> - 如果$R(-u, v)=R(u, v)$，即$R$关于$u$是偶对称的，那么可以将$R(u,v)$写为$P(u^2, v)$的形式，其中$P$是另外一个有理式.
> - 如果$R(-u, v)=-R(u, v)$，即$R$关于$u$是奇对称的，那么可以将$R(u,v)$写为$uP(u^2, v)$的形式，其中$P$是另外一个有理式.

如果有理函数$R(u,v)$对$u$是奇对称的，即满足$R(-u,v)=-R(u,v)$，则我们总可以将其写为$R(u,v)=uP(u^2,v)$的形式，其中$P$是另外一个有理函数. 那么对于三角有理式的情形，如果满足$R(-\sin x,\cos x)=-R(\sin x,\cos x)$，则有

$$
\begin{align*}
R(\sin x,\cos x)\mathrm{d}x & =\sin xP(\sin^2 x,\cos x)\mathrm{d}x \\ & =-P(1-\cos^2 x,\cos x)\mathrm{d}\cos x \\
& = -P(1-t^2, t)\mathrm{d}t
\end{align*}
$$

因此，只需要做换元$t=\cos x$，这明显比上面的通用换元法简单得多.

同理，如果有理函数$R(u,v)$对$v$是奇对称的，则我们总可以将其写为$R(u,v)=vP(u, v^2)$. 那么对于三角有理式的情形，如果满足$R(\sin x,-\cos x)=-R(\sin x,\cos x)$，则有

$$
\begin{align*}
R(\sin x,\cos x)\mathrm{d}x & =\cos xP(\sin x,\cos ^2 x)\mathrm{d}x \\ & =P(\sin x, 1-\sin^2 x)\mathrm{d}\sin x \\
& = P(t, 1-t^2)\mathrm{d}t
\end{align*}
$$

因此只需要做换元$t=\sin x$就可以得到更简单的有理式.

倘若$R(u,v)$满足$R(-u,-v)=R(u,v)$. 我们可以将$R(u,v)$写为$P(\dfrac{u}{v},v)$的形式，这时$P(\dfrac{u}{v}, v)$就变成了仅仅对$v$是偶对称的：

$$
R(-u,-v)=P(\dfrac{u}{v},-v)=R(u,v)=P(\dfrac{u}{v},v)
$$

于是，$R(u,v)$便可以写作$P(\dfrac{u}{v}, v^2)$的形式. 此时有

$$
\begin{align*}
R(\sin x,\cos x)\mathrm{d}x & =P\left(\frac{\sin x}{\cos x}, \cos^2 x \right)\mathrm{d}x \\
& = P\left(\tan x, \frac{1}{1+\tan^2 x} \right)\mathrm{d}x \\
& = P\left(t, \frac{1}{1+t^2} \right) \frac{1}{1+t^2}\mathrm{d}t
\end{align*}
$$

于是可以做换元$t=\tan x$.

对于一般形式的$R(u,v)$，或许其并不具有上述所说的几种对称性. 但是，正如同我们可以将一个一元函数分解为一个奇函数和一个偶函数之和一样，我们也可以对该有理式进行分解. 不妨设

$$
(1)\quad R(u,v)=R_1(u,v)+R_2(u,v)+R_3(u,v)
$$

其中$R_1(-u, v)=-R_1(u,v)$，$R_2(u,-v)=-R_2(u,v)$，而$R_3(-u,-v)=R_3(u,v)$. 于是

$$ 
(2)\quad R(-u,v)=-R_1(u,v)+R_2(-u,v)+R_3(-u, v)
$$

$$ 
(3)\quad R(u, -v)=R_1(u,-v)-R_2(u,v)+R_3(-u, v)
$$

$$ 
(4)\quad R(-u, -v)=-R_1(u,-v)-R_2(-u,v)+R_3(u, v)
$$

```{admonition} 求解过程
:class: dropdown, tip

由(1)-(3)可得

```

## 黎曼积分 Riemann Integrals

### 黎曼积分的定义

下面要研究的是**定积分**（definite integrals），通俗意义可以解释为函数$f(x)$在区间$[a,\,b]$内，图像与坐标轴之间曲边梯形的面积. 在微积分课程中，我们采取**黎曼积分**（Riemann integrals）的定义方式. 黎曼积分的研究对象是定义在闭区间$[a,\,b]$上的一个**有界函数**，因此，下面所有讨论都是基于被积函数是有界函数、积分区间是有限闭区间上进行的. 对于无界函数，和非闭区间上积分的情形，将在最后一节“广义积分”中讨论.

首先，在$a$和$b$之间插入一系列分点，完成对区间$[a,\, b]$的一个**分割**，我们将这个分割记为$\mathcal{T}$：

$$
\mathcal{T}: a=x_0 < x_1 < x_2 < \cdots < x_{n-1} < x_n=b
$$

于是，原来的区间$[a,\,b]$被切割为$n$个小区间$[x_{i-1},\, x_i]$，$1\leqslant i\leqslant n$，每个区间的长度定义为$\Delta_i = x_i-x_{i-1}$. 我们在每个小区间上随机“采样”一点$\xi_i$，即$\xi_i\in[x_{i-1},\, x_i]$，以此来用$f(\xi_i)$“代表”函数$f$在$[x_{i-1},\, x_i]$的值. 这样，我们就得到了一系列宽度为$\Delta_i$，高度为$f(\xi_i)$的小矩形，并用这些矩形面积之和来作为“曲边梯形”面积的近似值. 定义**黎曼和**为

$$
\sigma(f,\mathcal{T}):=\sum_{i=1}^{n}f(\xi_i)\Delta_i
$$

当分割粒度越来越密时，那么用小矩形面积之和的近似精度也将越来越高. 为此，我们定义$\Delta_i$中的最大值为分割$\mathcal{T}$的模，记为$\displaystyle|\mathcal{T}|=\max_{i}\Delta_i$，于是$|\mathcal{T}|$就可用于表征分割的粒度粗细. 下面考虑极限：

$$
\lim_{|\mathcal{T}|\to 0}\sigma(f,\mathcal{T})
$$

如果该极限存在，则称$f$在$[a,\, b]$上是**黎曼可积**的，记为$f\in R[a,\, b]$，并将极限值称为$f$在$[a,\, b]$上的**积分**，记为$\displaystyle \int_{a}^{b}f(x)\mathrm{d}x$. 这里$a$和$b$称为积分下限和积分上限.

> 除了黎曼积分的定义外，还有其他定积分的定义方式，如**勒贝格积分**（Lebesgue integrals）等. 勒贝格可积是比黎曼可积更宽松一点的条件，如Dirichlet函数在黎曼积分下是不可积的，但是在勒贝格积分下是可积的. 勒贝格积分的介绍详见实分析课程.

### 可积性讨论

对可积性的讨论实际上需要更深层次的实分析的知识. 这里对其进行一些简单的讨论.

我们仍然回到黎曼积分的定义上来，在原始定义中，我们任意地选择$\xi_i\in[x_{i-1},\, x_i]$，以$f(\xi_i)$来代表小区间上的函数值. 由于$f$是有界的，自然在每个小区间上也有界. 为此，取$\displaystyle m_i:=\inf_{[x_{i-1},\, x_i]}f(x)$和$\displaystyle M_i:=\sup_{[x_{i-1},\, x_i]}f(x)$. 特别地，定义$m$和$M$为$f$在整个$[a,\,b]$上的下确界和上确界. 定义Darboux上和和下和：

$$
U(f,\mathcal{T}):=\sum_{i=1}^{n}M_i\Delta_i
$$

$$
L(f,\mathcal{T}):=\sum_{i=1}^{n}m_i\Delta_i
$$

由于$m_i\leqslant f(\xi_i)\leqslant M_i$，故对任何分割$\mathcal{T}$总有$L(f,\mathcal{T})\leqslant \sigma(f,\mathcal{T}) \leqslant U(f,\mathcal{T})$.

下面进一步来探究分割$\mathcal{T}$的疏与密对上下和的影响. 我们假设对原分割插入新的分点，从而得到一个新的分割$\mathcal{T}'$，则有

$$
U(f,\mathcal{T})\geqslant U(f,\mathcal{T}')
$$

$$
L(f,\mathcal{T}) \leqslant L(f,\mathcal{T}')
$$

这一结论是符合直觉的：把一个小区间分为多个，新分出的区间可能会产生更小的上确界和更大的下确界.

```{admonition} 证明
:class: tip, dropdown

考虑在$[x_{i-1},\, x_i]$中插入的一个新分点$z$，则有

$$\begin{align*}
& \sup_{[x_{i-1},\, z]}f(x)(z-x_{i-1}) + \sup_{[z,\, x_i]}f(x)(x_i-z) \\
\leqslant  & \sup_{[x_{i-1},\, x_i]}f(x)(z-x_{i-1}) + \sup_{[x_{i-1},\, x_i]}f(x)(x_i-z) \\
= & \sup_{[x_{i-1},\, x_i]}f(x)(x_i-x_{i-1})
\end{align*}$$

同样，这一过程也适用于其他分点. 于是可以得到$U(f,\mathcal{T})\leqslant U(f,\mathcal{T}')$. 对下确界的讨论可以得到$L(f,\mathcal{T}) \leqslant L(f,\mathcal{T}')$.

---

其实我们也可以估算出插入新分点后，引起的上和/下和变化量的上界. 有

$$\begin{align*}
& \sup_{[x_{i-1},\, x_i]}f(x)(x_i-x_{i-1}) - [\sup_{[x_{i-1},\, z]}f(x)(z-x_{i-1}) + \sup_{[z,\, x_i]}f(x)(x_i-z)] \\
\leqslant & M(x_i-x_{i-1}) - m(x_i-x_{i-1}) 
\end{align*}$$

于是加入一个分点后，有

$$
0\leqslant U(f,\mathcal{T})-U(f,\mathcal{T}')\leqslant (M-m)\vert\mathcal{T}\vert
$$

加入$k$个分点后，则为

$$
0\leqslant U(f,\mathcal{T})-U(f,\mathcal{T}')\leqslant k(M-m)\vert\mathcal{T}\vert
$$

对下和也有类似的结论

$$
0\leqslant L(f,\mathcal{T}')-U(f,\mathcal{T})\leqslant k(M-m)\vert\mathcal{T}\vert
$$

```

现在我们用$\mathcal{T}^1$来表示一个包含1个分点的分割，以$\mathcal{T}^{k+1}$表示在$\mathcal{T}^{k}$的基础上再新增一个分点得到的分割. 特别地，$k=0$表示没有分割，此时$L(f,\mathcal{T}^0)=m(b-a)$以及$U(f,\mathcal{T}^0)=M(b-a)$，于是根据上述讨论，有

$$
m(b-a)=L(f,\mathcal{T}^0)\leqslant L(f,\mathcal{T}^1) \leqslant L(f,\mathcal{T}^2) \leqslant \cdots
$$

以及

$$
\cdots\leqslant U(f,\mathcal{T}^2)\leqslant U(f,\mathcal{T}^1) \leqslant U(f,\mathcal{T}^0) = M(b-a)
$$

所以在增加新的分点的过程中，下和会单调递增，上和会单调递减，二者“双向奔赴”. 那么上和和下和是否会撞车？即是否会存在一些下和大于上和的情况？我们说明这是不可能的. 对于任意两个分割$\mathcal{T}_1$和$\mathcal{T}_2$，我们把两个分割的分割点合并得到$\mathcal{T}_3$，于是

$$
L(f,\mathcal{T}_1)\leqslant L(f,\mathcal{T}_3)\leqslant U(f,\mathcal{T}_3) \leqslant U(f,\mathcal{T}_2)
$$

可见二者“渠会永无缘”，所有的下和和所有的上和之间存在一条“鸿沟”. 在增加分割点的过程中，下和有上和作为上界，于是有上确界；同理上和有下确界. 称下和的上确界为**下积分**，上和的下确界为**上积分**，记为

$$
I_*=\sup_\mathcal{T}L(f,\mathcal{T})
$$

$$
I^*=\inf_\mathcal{T}U(f,\mathcal{T})
$$

现在，我们终于得到了下面这一链条：

$$
m(b-a)=L(f,\mathcal{T}^0)\leqslant L(f,\mathcal{T}^1) \leqslant L(f,\mathcal{T}^2) \leqslant \cdots \\
\leqslant I_* \leqslant I^* \leqslant \\

\cdots\leqslant U(f,\mathcal{T}^2)\leqslant U(f,\mathcal{T}^1) \leqslant U(f,\mathcal{T}^0) = M(b-a)
$$

由此可以得到黎曼可积性的两个充要条件：

（1）**充要条件**：$f$在$[a,\, b]$上黎曼可积，当且仅当$I_*=I^*$，此时上下积分的值就等于积分值本身.

（2）**充要条件**：$f$在$[a,\, b]$上黎曼可积，当且仅当对于$\forall\varepsilon >0$，存在分割$\mathcal{T}$，使得$U(f,\mathcal{T})-L(f,\mathcal{T}) < \varepsilon$.

### 黎曼积分的性质

## 定积分的计算 Calculation of Definite Integrals

### 微积分基本定理

### 计算技巧

## 定积分的应用 Applications

## 广义积分