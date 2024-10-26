# 线性空间 Linear Spaces

## 线性空间和子空间 Linear Spaces/Subspaces

### 线性空间的定义

「线性」相比于「非线性」具有更多优美的性质，因而我们更喜欢解决线性的问题，或者把非线性问题转换为线性问题. 如何刻画「线性」？

记四元组$\mathcal{S}=\langle\mathbb{F},\mathbb{U},\circ, *\rangle$，其中：
- $\mathbb{F}$和$\mathbb{U}$均为包含若干元素的集合
- $\circ$是定义在$\mathbb{F}$上的二元运算：$\circ: \mathbb{F}\times\mathbb{F}\to \mathbb{F}$，也是在$\mathbb{U}$上的二元运算：$\circ: \mathbb{U}\times\mathbb{U}\to \mathbb{U}$
- $*$是定义在$\mathbb{U}$和$\mathbb{F}$上的二元运算：$*:\mathbb{U}\times\mathbb{F}\to \mathbb{F}$

如果$\mathcal{S}$满足下述条件，则称其为一个**线性空间**（linear space）：

（1）运算$\circ$的交换律：任意$x,y\in\mathbb{F}$，均有$x\circ y=y\circ x$.

（2）运算$\circ$的结合律：任意$x,y,z\in\mathbb{F}$，均有$(x\circ y)\circ z=x \circ (y\circ z)$.

（3）运算$\circ$的单位元：存在$e\in\mathbb{F}$，使得对于任意的$x\in\mathbb{F}$，有$e\circ x = x\circ e = x$. 此时$e$称为**单位元**.

（4）运算$\circ$的逆元：对于任意$x\in\mathbb{F}$，存在$x'\in\mathbb{F}$，使得$x\circ x' = x'\circ x = e$. 此时$x'$称为元素$x$的**逆元**.

（5）运算$*$的结合律：对于任意$a,b\in\mathbb{U}$和$x\in\mathbb{F}$，有$(ab)x=a(bx)$.

（6）运算$*$对$\mathbb{F}$的分配律：对于任意$a,b\in\mathbb{U}$和$x\in\mathbb{F}$，有$(a\circ b)* x = a*x\circ b*x$.

（7）运算$*$对$\mathbb{U}$的分配律：对于任意$a\in\mathbb{U}$和$x,y\in\mathbb{F}$，有$a * (x\circ y) = a*x\circ a*y$.

（8）运算$*$的单位元：存在$e\in\mathbb{U}$，使得对任意$x\in\mathbb{F}$，有$e* x = x$.

> - $\circ$的单位元是唯一的. 因为有$e' = e'\circ e'' = e''$.
> - $x$的逆元也是唯一的.因为有$x' = e\circ x' = (x''\circ x)\circ x' = x''\circ (x\circ x') = x''$.

一个常见、典型的例子就是向量空间：$\langle\mathbb{R}^n,\mathbb{R},+,\cdot\rangle$，也可以称之为$n$维向量空间. 这里$+$代表向量和实数的加法，$\cdot$代表实数和向量的乘法. 加法运算的单位元就是$\boldsymbol{0}$，即零向量；$\boldsymbol{x}$的逆元为$-\boldsymbol{x}$；数乘运算的单位元为数字$1$. 由于$+$和$\cdot$是比$\circ$和$*$更常见的记号，后面我们就用$\langle\mathbb{F},\mathbb{R},+,\cdot\rangle$来表述线性空间了. 或者，为了更方便，会直接拿$\mathbb{F}$来代表这个线性空间.

### 线性子空间

「子空间」的概念类似于「子集」，但不能完全等同，因为子空间要求对两个运算封闭. 我们记$\mathcal{S}=\langle\mathbb{A},\mathbb{B},+,\cdot\rangle$是一个线性空间，对于另一个四元组$\mathcal{S}'=\langle\mathbb{A}',\mathbb{B}',+,\cdot\rangle$，如果其满足：

- $\mathbb{A}'\subseteq\mathbb{A}$且$\mathbb{B}'\subseteq\mathbb{B}$
- 子集$\mathbb{A}'$、$\mathbb{B}'$对$+$和$\cdot$运算封闭

则称$\mathcal{S}'$是$\mathcal{S}$的一个**线性子空间**（linear subspace）.

> - 判定线性子空间只需要验证封闭性，因为子空间一定是满足8条性质的.
> - 由此可见，并不是简单选择一个子集就可以称为子空间. 例如，平面$x+y+z=1$是$\mathbb{R}^3$的一个子集，但不是子空间.

### 线性子空间的运算

设有两个线性空间$U$和$V$，且其是某一个更大的线性空间的子空间（为了保证后面的加法运算等可以成立），由是我们可以定义他们的几种运算：**交集**、**和**（sum）、**直和**（direct sum）等.

两个空间的**交集**定义为：

$$
U\cap V=\{x: x\in U \wedge x \in V\}
$$

上述两个空间的**和**定义为：

$$
U+V := \{u+v:u\in U, v\in V\}
$$

同理，如果有更多的子空间$U_i$，$1\leqslant i\leqslant n$，则它们的和定义为：

$$
U_1+\cdots+U_n = \{u_1+\cdots+u_n: u_1\in U_1,\cdots, u_n\in U_n\}
$$

如果这些子空间满足一些特定的需求，则它们的和就可以成为**直和**，记为$U_1\oplus\cdots\oplus U_n$. 直和的定义，或者说是这些子空间需要满足的需求：

- 任意的$v\in U_1\oplus\cdots\oplus U_n$，分别存在**唯一的**$u_1\in U_1$，$u_2\in U_2$，…… $u_n\in U_n$（即分解是唯一的）.
- 一种等价叙述：若$u_1+\cdots+u_n=\boldsymbol{0}$当且仅当$u_1=u_2=\cdots=u_n=\boldsymbol{0}$.
- 如果是两个子空间求和的情形，还有第二种等价叙述：$U+V=U\oplus V$当且仅当$U\cap V=\{\boldsymbol{0}\}$.

> - 第一种等价叙述的说明：假如$\boldsymbol{0}$存在非全零的分解，那么和空间中的任意元素$v$，必然可以找到两种分解（分别是原本的分解和$v+0$的分解），违反了原本定义.
> - 第二种等价叙述的说明：设$c\in U\cap V$且$c$非零，则从$U$选择元素$c$，从$V$中选择$-c$，那么有$\boldsymbol{0}=c+(-c)$，这违反了第一种等价叙述.

可见直和是一种特殊的和. 相比于普通的和，直和要求累加的结果是「可逆」或者「可溯源」的.

```{admonition} Example
- 空间中两条不重合的过原点的直线$l_1$和$l_2$显然是$\mathbb{R}^3$的两个子空间，那么它们的和就是这两条直线所在的平面，其实这个和也是直和.
- 可以加入第三条过原点的直线$l_3$. 如果$l_3$在刚刚那个平面内，则$l_1+l_2+l_3$也是该平面，但此时这个和不是直和. 如果$l_3$不在刚刚那个平面内，则此时$l_1+l_2+l_3$也是直和，实际上就是整个$\mathbb{R}^3$.
```

尽管在集合中还有并集、补集等运算，但它们并不能直接推广到线性子空间的运算中. 容易验证，一般$U\cup V$并不是一个线性空间；而如果对线性空间*直接*取补集，则补集也不是一个线性空间（没有零元素），所以没有太大的研究意义. 但是，我们有另一种方式定义我们想要的 「补」. 设$U$是$W$的一个子空间，则$W$总能拆解为两个子空间的直和：

$$
W=U\oplus V
$$

此时称$U$和$V$互为对方的**补（空间）**.

## 线性组合与相关性 Linear Combination & Dependence

上面直和中提到了分解的唯一性，这实际上有着非常深刻的性质.

设$\boldsymbol{u}_1,\cdots,\boldsymbol{u}_n$是某个线性空间$W=\langle \mathbb{F},\mathbb{R},+,\cdot\rangle$内的若干元素，则定义它们的**张成空间**（span space）为

$$
\mathrm{span}(\boldsymbol{u}_1,\cdots,\boldsymbol{u}_n) := \{c_1\boldsymbol{u}_1+\cdots+c_n\boldsymbol{u}_n : c_i\in\mathbb{R}, 1\leqslant i\leqslant n\}
$$

显然新的空间是$W$的一个子空间. 称$\boldsymbol{u}_1,\cdots,\boldsymbol{u}_n$是该空间的一个**张成组**，而该子空间的每个元素为$\boldsymbol{u}_1,\cdots,\boldsymbol{u}_n$的一个**线性组合**（linear combination）.

每个线性空间或子空间都可以找出很多不同的张成组，而这些张成组中所包含的元素个数（后面称为「长度」）可能各不相同. 对于$\mathbb{R}^3$中过原点的一个平面，甚至可以选出一个包含几百个向量的张成组. 这显然是浪费的，因为如果张成组中的某个元素可以表示为组内其它元素的线性组合，那么它就是冗余的，完全可以从张成组中去掉，而不影响张成空间. 所以可以提出线性**相关**（dependent）和**无关**（independent）的概念.

称一组元素$\boldsymbol{u}_1,\cdots,\boldsymbol{u}_n$是相关的，有下面三种等效定义：

- 其中某个元素可以表示为其他元素的线性组合，即存在$k$，使得$\displaystyle \boldsymbol{u}_k = \sum_{i\neq k}c_i\boldsymbol{u}_i$.
- 存在不全为0的系数$\{c_i\}$，使得$\displaystyle \sum_{i=1}^{n}c_i\boldsymbol{u}_i=\boldsymbol{0}$.
- 若对于任意$\boldsymbol{v}\in\mathrm{span}(\boldsymbol{u}_1,\cdots,\boldsymbol{u}_n)$，$\boldsymbol{v}$写作$\boldsymbol{u}_1,\cdots,\boldsymbol{u}_n$线性组合的方式**不唯一**. 即存在不完全相同的$\{c_i\}$和$\{d_i\}$，使得$\displaystyle \boldsymbol{v}=\sum_{i=1}^{n}c_i\boldsymbol{u}_i=\sum_{i=1}^{n}d_i\boldsymbol{u}_i$.

同理，称一组元素$\boldsymbol{u}_1,\cdots,\boldsymbol{u}_n$是无关的，有下面三种等效定义：

- 任何一个元素都无法表示为其他元素的线性组合.
- $\displaystyle \sum_{i=1}^{n}c_i\boldsymbol{u}_i=\boldsymbol{0}$当且仅当所有系数$c_i$均为0.
- 若对于任意$\boldsymbol{v}\in\mathrm{span}(\boldsymbol{u}_1,\cdots,\boldsymbol{u}_n)$，$\boldsymbol{v}$写作$\boldsymbol{u}_1,\cdots,\boldsymbol{u}_n$线性组合的方式**是唯一的**. 即如果$\displaystyle \boldsymbol{v}=\sum_{i=1}^{n}c_i\boldsymbol{u}_i=\sum_{i=1}^{n}d_i\boldsymbol{u}_i$，则对每个$i$都有$c_i=d_i$.

所以，如果一个张成组中的元素是线性相关的，那么我们可以删除其中可以由其他元素组合出来的元素，来使得其更加经济，由此得到张成空间的**最大无关组**. 称$\{\boldsymbol{v}_i\}_{i=1}^m$是$\{\boldsymbol{u}_i\}_{i=1}^n$的最大无关组，如果

- $\{\boldsymbol{v}_i\}_{i=1}^m\subseteq \{\boldsymbol{u}_i\}_{i=1}^n$
- $\{\boldsymbol{v}_i\}_{i=1}^m$线性无关
- 如果从$\{\boldsymbol{u}_i\}_{i=1}^n$剩下的元素中任选一个加入到$\{\boldsymbol{v}_i\}_{i=1}^m$中，其将立刻变成线性相关.

## 基和维数 Bases & Dimensions