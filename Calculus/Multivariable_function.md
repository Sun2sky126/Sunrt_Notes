# 多元函数 Multivariable Functions

本部分主要内容包括
- 高维度量空间、点集拓扑
- 多元函数、向量值函数的定义
- 极限和连续性
- 微分和偏导数

## 高维度量空间 

*Refs*: 
- 《高等微积分教程（下）》1.1
- 卓里奇《数学分析（第一卷）》7.1，8.1

### $n$维Euclid空间的定义

对于一个集合 $X$，如果对于其中的任意两个元素 $x_1$ 和 $x_2$ ，我们都能定义这两个元素之间的**距离**(distance)或**度量**(metric) $d(x_1,x_2)$，且这个距离具有如下性质：
- **正定性**：对任意两个元素，总有 $d(x_1,x_2)\geqslant 0$；且 $d(x_1,x_2)=0$ 当且仅当 $x_1=x_2$.
- **对称性**：对任意两个元素，总有 $d(x_1,x_2)=d(x_2,x_1)$.
- **三角不等式**：对任意三个元素，总有 $d(x_1,x_2)+d(x_2,x_3)\geqslant d(x_1,x_3)$.

则称 $\langle\, X, d\,\rangle$ 构成了一个**度量空间**(metric space). 

在线性代数中我们已经引入了$n$维实线性空间 $\langle\,\mathbb{R}^n,+,\cdot\,\rangle$，$\mathbb{R}^n$ 中的元素可以表示为 $\boldsymbol{X}=(x_1,\cdots,x_n)^\mathrm{T}$，可以称 $\boldsymbol{X}$ 为一个**点**或者**向量**。

> 关于 $\langle\,\mathbb{R}^n,+,\cdot\,\rangle$ 空间的更详尽介绍可以参考线性代数部分的笔记。由于在微积分部分的笔记中我们不过多强调矩阵运算，所以后面将省略转置上标。

定义向量 $\boldsymbol{X}$ 的 $p$-**范数**(norm)为

$$
\Vert\boldsymbol{X}\Vert_p:=\left(\sum_{i=1}^n |x_i|^p\right)^\frac{1}{p}
$$

常用的范数包括1-范数 $\displaystyle \|\boldsymbol{X}\|_1=\sum_i |x_i|$，2-范数 $\displaystyle \|\boldsymbol{X}\|_2=\sum_i |x_i|^2$ 和无穷范数 $\displaystyle \|\boldsymbol{X}\|_\infty=\max_i |x_i|$. 我们使用2-范数，又称为**Euclid距离**，来作为上述线性空间中的度量，并省略下标2. 因此， $\langle\,\mathbb{R}^n,+,\cdot\,\rangle$ 中两个点 $\boldsymbol{X}$ 和 $\boldsymbol{Y}$ 的距离定义为

$$
d(\boldsymbol{X},\boldsymbol{Y}) := \|\boldsymbol{X}-\boldsymbol{Y}\|
$$

可以验证这一定义满足上面提到的三个条件，至此，我们已经完成了 $n$ 维Euclid度量空间的定义 $\langle\,\mathbb{R}^n,+,\cdot,d\,\rangle$.

### 空间上的点集拓扑

对于点 $\boldsymbol{X}_0$ 和实数 $\delta >0$， 定义点 $\boldsymbol{X}_0$ 的 **$\delta$-邻域**和**去心 $\delta$-邻域**为

$$
B(\boldsymbol{X}_0,\delta):=\{\boldsymbol{X}:\|\boldsymbol{X}-\boldsymbol{X}_0\| <\delta\}
$$

$$
B^\circ(\boldsymbol{X}_0,\delta):=\{\boldsymbol{X}:0<\|\boldsymbol{X}-\boldsymbol{X}_0\| <\delta\} = B(\boldsymbol{X}_0,\delta)\backslash\{\boldsymbol{X}_0\}
$$

基于这一定义，我们可以对空间中点和集合的性质进行一些分类。考虑 $\mathbb{R}^n$ 中的集合 $E$。则对于 $\mathbb{R}^n$ 中的点 $\boldsymbol{X}_0$，定义

- $\boldsymbol{X}_0$ 是 $E$ 的**内点**，如果存在 $\delta > 0$，满足 $B(\boldsymbol{X}_0,\delta)\subset E$.
- $\boldsymbol{X}_0$ 是 $E$ 的**外点**，如果存在 $\delta > 0$，满足 $B(\boldsymbol{X}_0,\delta)\subset E^\mathrm{c}$.
- $\boldsymbol{X}_0$ 是 $E$ 的**边界点**，如果它既不是 $E$ 的内点，也不是 $E$ 的外点. 也可以这样定义：对于 $\forall\delta>0$，$B(\boldsymbol{X}_0,\delta)\cap E\neq\varnothing$ 且 $B(\boldsymbol{X}_0,\delta)\cap E^\mathrm{c}\neq\varnothing$.

> 从定义中可以看出：给定点 $\boldsymbol{X}_0$ 和集合 $E$，二者之间的关系必然居于上述三种情况之一。集合的内点一定属于该集合，外点一定不属于该集合，边界点不一定属于或不属于该集合。

基于对内点的定义，可以定义集合的开闭性：

- $E$ 是**开集**，如果 $E$ 中所有点都是它的内点.
- $E$ 是**闭集**，如果 $E^\mathrm{c}$ 是开集.

> 上述定义并不是二分的，一个集合可以既不是开集也不是闭集。类比于一维情形下的半开半闭区间，在高维空间中半开半闭的情形会更加复杂。

同时，也可以定义集合的内部、外部和边界：

- $E$ 的所有内点构成 $E$ 的**内部**，记为 $\mathrm{int} E$ 或 $\mathring{E}$.
- $E$ 的所有外点构成 $E$ 的**外部**，记为 $\mathrm{ext} E$.
- $E$ 的所有边界构成 $E$ 的**边界**，记为 $\partial E$.

基于对内部和边界的定义，可以定义一个集合的**闭包**. 一个集合 $E$ 的闭包记为 $\mathrm{cl}E$ 或 $\bar{E}$ ，有如下几种等价的定义方式：

- $\bar{E}:= E\cup\partial E$.
- $\bar{E}$ 是集合 $E$ 和它所有**极限点**构成的集合.

其中，**极限点**也称为**聚点**，同样也有几种不同但等价的定义方式：

- $\boldsymbol{X}_0$ 是集合 $E$ 的聚点，如果 $\boldsymbol{X}_0$ 的任意邻域 $N(\boldsymbol{X}_0)$ 都包含了 $E$ 中无穷多个点.
- $\boldsymbol{X}_0$ 是集合 $E$ 的聚点，如果 $\boldsymbol{X}_0$ 的任意邻域 $N(\boldsymbol{X}_0)$ 都包含了 $E$ 中至少一个相异于 $\boldsymbol{X}_0$ 的点.
- $\boldsymbol{X}_0$ 是集合 $E$ 的聚点，如果 $E$ 中存在一个各项互异的数列 $\{\boldsymbol{X}_i\}_{i=1}^\infty$ 收敛到 $\boldsymbol{X}_0$.

> - 点 $\boldsymbol{X}$ 的**邻域**(neighbor)指的是包含 $\boldsymbol{X}$ 的开集，可以记为 $N(\boldsymbol{X})$.
> - 一个集合的聚点可能是集合的内点，也可能是集合的边界点，但绝无可能是集合的外点。 

下面介绍**紧集**. 有界闭集称为紧集. 称一个集合 $E$ **有界**，如果存在 $0<M<\infty$，使得 $\forall\boldsymbol{X}\in E$，都有 $\|\boldsymbol{X}\|\leqslant M$. 同一维情形下的闭区间，有界闭集具有有限覆盖性质，即对于紧集 $E$ 的任何一个开覆盖 $\{G_\alpha\}_{\alpha\in\Gamma}$，$\displaystyle E\subset\bigcup_{\alpha\in\Gamma}G_\alpha$，总能在其中找到其中有限个集合覆盖 $E$，即 $\displaystyle E\subset\bigcup_{i=1}^N G_{\alpha_i}$.

最后介绍集合的连通性。如果一个集合中任意两点均可用一条**折线段**连接，则称该集合为连通集，否则为不连通。连通开集称为**开区域**，开区域的闭包称为**闭区域**。

> 要注意此处闭区域的定义。闭区域**不等于**连通的闭集。要判定一个集合是否为闭区域，需要先检验其内部是否为开区域。一个反例是“8”字型集合，即两个闭集之间只有唯一的公共点。该集合的内部不包含该公共点，是不连通的。

### $n$维Euclid空间的完备性

