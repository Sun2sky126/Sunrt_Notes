# 宽平稳过程 Stationary Processes (Wide Sense)

## 自相关函数

对于任意宽平稳复过程$X(t)$，其（自）相关函数定义为

$$
R_{XX}(\tau)=\mathbf{E}[X(t+\tau)X^*(t)]
$$

有时也简记为$R(\tau)$或$R_{X}(\tau)$.

不难验证，相关函数具有**共轭对称性**，即满足$R(-\tau)=R^*(\tau)$. 特别地，当$X(t)$是完全的实数过程时，有$R(\tau)=\mathbf{E}[X(t+\tau)X(t)]$. 此时相关函数是对称的，或者说是偶函数，满足$R(-\tau)=R(\tau)$.

相关函数在0点处的取值具有重要的意义. 其具有如下性质：

（1）最大值：我们有$R(0)\geqslant 0$. 如果$X(t)$是实的，那么任意$\tau$有$R(0)\geqslant R(\tau)$.

> 这是因为我们有$\mathbf{E}[|X(t+\tau)-X(t)|^2]=2R(0)-2R(\tau)\geqslant 0$. （展开计算即可）

（2）有界性：如果随机过程$X$和$Y$都是实的，那么有$R_{XY}(\tau)^2\leqslant R_X(0)R_Y(0)$.

> 由数学期望的Cauchy-Schwarz不等式$\mathbf{E}[XY]^2\leqslant \mathbf{E}[X]^2\mathbf{E}[Y]^2$，代入$X=X(t+\tau)$和$Y=Y(t)$便可立刻得到上述结论.

（3）周期性：若存在$T\neq 0$使得$R(0)=R(T)$，则$R$是一个以$T$为周期的函数.

（4）连续性：若$R(\tau)$在0处连续，则在任何点处都连续.

## 功率谱 

$$
S(\omega) = \int_{-\infty}^{+\infty}R(\tau)\mathrm{e}^{-\mathrm{j}\omega\tau}\mathrm{d}\tau
$$

（1）$S(\omega)$总是实的. 这是因为对于任意**复**的宽平稳过程，其自相关函数总是共轭对称的，因而自相关函数的Fourier变换总是实的.

（2）特别地，如果$X(t)$是实的，那么$S(\omega)$是实偶函数.

> $\displaystyle S(\omega) = \int_{-\infty}^{+\infty}R(\tau)\cos(\omega\tau)\mathrm{d}\tau
$

（3）$S(\omega)$曲线下的面积（积分）总是非负的. 特别地，若$S(\omega)$的某部分连续，则这一连续部分都是非负的.

## 线性系统 Linear Systems

$$
\eta_Y = \eta_X H(0)
$$

$$
R_{YX}(\tau) = R_{XX}(\tau)*h(\tau)
$$

$$
R_{YY}(\tau) = R_{YX}(\tau)*h^*(-\tau) = R_{XX}(\tau)*h(\tau)*h^*(-\tau)
$$