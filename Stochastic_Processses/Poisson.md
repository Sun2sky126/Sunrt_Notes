# 泊松过程 Poisson Processes

## 计数过程 Counting Processes

泊松过程是计数过程的一种. **计数过程**（counting processes）描述了一段时间内发生的事件个数. 设$N(t)$是一个计数过程，那么根据上面的定义，它应该具备下面的性质：

- 对任意$t\geqslant 0$，$N(t)$总是非负整数.
- $N(t)$是单调递增的（可以不严格），即对任意$s < t$，有$N(s)\leqslant N(t)$.
- 对任意$s < t$，$N(t)-N(s)$描述了发生在区间$(s,t]$内的事件数目.

特别地，如果对于任意$s_1 < t_1 < s_2 < t_2$，$N(t_1)-N(s_1)$和$N(t_2)-N(s_2)$独立，则称其为**独立增量过程**. 对于任意$s < t$，如果$N(t)-N(s)$的分布仅取决于$t-s$（即区间的长度）而不依赖于$s$的选取，则称其为**平稳增量过程**.

基于计数过程的定义，我们可以定义两串随机变量. 我们把第$n$个事件发生的时刻记为$S_n$，称为发生时间或**到达时间**. 如果记$S_0=0$，则称$X_n = S_{n}-S_{n-1}$称为第$n$个事件的**等待时间**. 它表示两个事件之间（或者从$t=0$时刻到第一个事件发生）的间隔时间. 于是就有$\displaystyle S_n=\sum_{k=1}^{n}X_k$.


## 泊松过程的定义和性质 Definitions & Properties

### 齐次泊松过程的两种定义

## 到达时间和等待时间

## 泊松过程的推广

### 泊松过程的分流

### 非齐时泊松过程

### 条件泊松过程

### 复合泊松过程