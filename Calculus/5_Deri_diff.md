# 一元函数的导数和微分 Derivatives & Differentials for Univariable Functions

## 一元函数的导数 Derivatives

### 导数的定义

若$f$在$x_0$附近有定义，且极限$\displaystyle \lim_{h\to 0}\frac{f(x_0+h)-f(h)}{h}$存在，则称$f$在$x_0$处**可导**，并将这一极限值称为$f$在$x_0$处的**导数**（derivative），可以记为$f'(x_0)$、$f'|_{x_0}$、$\displaystyle \frac{\mathrm{d}f(x_0)}{\mathrm{d}x}$等等. 同理，类比于单侧极限和单侧连续，可以定义函数的左导数$f'_{-}(x_0)=\displaystyle \lim_{h\to 0^-}\frac{f(x_0+h)-f(h)}{h}$和右导数$\displaystyle \lim_{h\to 0^+}\frac{f(x_0+h)-f(h)}{h}$. 同样地，$f$在$x_0$处可导当且仅当其左右导数均存在且相等.

> 由于$x_0$处对应着唯一的$y_0$，所以也可以说$f'(x_0)$是$f$在$P_0(x_0,y_0)$处的导数，可以记为$f'(P_0)$、$f'|_{(x_0, y_0)}$、$\dfrac{\mathrm{d}f}{\mathrm{d}x}(P_0)$等等. 后续在处理隐函数、反函数等的导数时，我们也会这样来表示.

导数的物理含义是"瞬时变化率"，即函数在这一点附近的增长趋势. 正的导数意味着瞬时增加，而负的导数意味着瞬时减少. 更进一步，除了定性判定瞬时增加或减少之外，还可以估算具体增加或减少的量. 由导数的定义，我们可以得到$\displaystyle \frac{f(x_0+h)-f(x_0)}{h}=f'(x_0)+o(1),\,h\to 0$，只需要变形即可得到$f(x_0+h)-f(x_0) = f'(x_0)h+o(h),\, h\to 0$. 其中$h$是自变量的变化量，记为$\Delta x$，而等号左边为$\Delta x$引起的函数值变化量，记为$\Delta y$，那么

$$
\Delta y = f'(x_0)\Delta x + o(\Delta x),\, \Delta x\to 0
$$

由此，函数改变量$\Delta y$就被分解为了两部分，其中第一部分$f'(x_0)\Delta x$是估计的增加（减少）量，第二部分是估计误差，是自变量增长值$\Delta x$的高阶无穷小. 更进一步，如果上式中令$\Delta x\to 0$，可以得到

$$
\lim_{\Delta x\to 0}f(x_0+\Delta x)-f(x_0)=0
$$

这说明$f$在$x_0$处连续，即可导性蕴含着连续性. 事实上，**可导一定连续，而连续不一定可导**.

如果$f$在区间$(a,b)$上的每一点都可导，则称其在整个区间上可导. 类似于连续函数，如果加上端点单侧可导的条件，可以得到其在闭区间或半开半闭区间上的可导性. 由此，我们可以确定一个新的映射（函数）：即每一点$x_0$映射到它在这一点上的导数$f'(x_0)$. 我们将这一新的函数称为函数$f$的**导函数**，有时也会直接简称为导数.

$$
f': x \mapsto f'(x)
$$

> - 导数有很多记号，例如$f'$、$f_x'$、$f_x$、$\dot{f}$、$\mathcal{D}(f)$、$\displaystyle \frac{\mathrm{d}f}{\mathrm{d}x}$等. 我们在使用$f'(x_0)$这样的记号时，切记它代表着"函数$f'$在$x_0$处的值"，而绝非"f(x_0)的导数"，因为$f(x_0)$是一个常数，其导数为0.

对于这一新的函数$f'$，不能直接判断出其是否连续和可导. 一个可导函数的导数，可能是个不连续的函数. 如果函数$f$在区间$I$可导，且其导函数连续，则称其**连续可导**，记为$f\in \mathcal{C}^{(1)}(I)$. 如果它的性质再好一点，即导函数也可导，那么就可以类似地求出导函数的导函数. 一个函数的导函数的导函数称为它的**二阶导（函）数**，记为$f''$或者$\displaystyle\frac{\mathrm{d}^2 f}{\mathrm{d}x^2}$. 同理，可以定义三阶导数$f'''$和$\displaystyle\frac{\mathrm{d}^3 f}{\mathrm{d}x^3}$，以及$n$阶（$n>3$）阶导数$f^{(n)}$或$\displaystyle\frac{\mathrm{d}^n f}{\mathrm{d}x^n}$. 若函数$f$的$n$阶导数连续，则称为$n$阶连续可导，记为$f\in\mathcal{C}^{(n)}(I)$.

### 导数的求法

导数的通用求法是使用定义，但对于初等函数或者初等函数的片段，可以用更简便的法则去求.

（1）**基本初等函数的导数**

基本初等函数在其定义域内都是可导的. 其导函数如下.

```{admonition} 基本初等函数的导函数
:class: tip, dropdown

（1）常数函数：$c'=0$.

（2）幂函数：$(x^{n})'=nx^{n-1}$

（3）指数函数：$(a^x)'=a^x\ln a$

（4）对数函数：$\displaystyle (\log_{a}x)'=\frac{1}{x\ln a}$

（5-a）三角函数：$(\sin x)'=\cos x$，$(\cos x)'=\textcolor{red}{-}\sin x$

（5-b）双曲三角函数：$(\sinh x)'=\cosh x$，$(\cosh x)'=\sinh x$

（6-a）反三角函数：$\displaystyle (\arcsin x)'=\frac{1}{\sqrt{1-x^2}}$，$(\arccos x)'=-\dfrac{1}{\sqrt{1-x^2}}$，$(\arctan x)'=\dfrac{1}{1+x^2}$

（6-b）反双曲三角函数：$(\mathrm{arcsinh}\,x)'=\dfrac{1}{\sqrt{1+x^2}}$，$(\mathrm{arccosh}\,x)'=\dfrac{1}{\sqrt{x^2-1}}$，$(\mathrm{arctanh}\, x)'=\dfrac{1}{1-x^2}$.
```

（2）**四则运算和复合函数的导数**

初等函数在其定义域内都是可导的. 因此，可以使用下面的法则来求其导数.

$$
(f\pm g)'=f'\pm g'
$$

$$
(fg)' = f'g + fg'
$$

$$
\left(\frac{f}{g}\right)'=\frac{f'g-fg'}{g^2}
$$

上述法则对于高阶导数也有相应的版本：

$$
(f\pm g)^{(n)} = f^{(n)}+g^{(n)}
$$

$$
(fg)^{(n)}=\sum_{i=0}^{n}\mathbf{C}_{n}^{i}f^{(i)}g^{(n-i)}
$$

上面第二个等式也称作Leibniz公式（区分于Newton-Leibniz公式！）

对于复合函数，我们有：如果$g(x)$在$x_0$可导，而$f(u)$在$u_0=g(x_0)$处可导，则$f(g(x))$在$x_0$可导，且

$$
[f(g(x))]'=f'(u_0)g'(x_0)
$$

这一法则也称为**链式法则**（chain rule）.

（3）**隐函数和反函数的导数**

对于方程$F(x,y)=0$，如果对于$\forall x\in I$，总能解出一个唯一的$y$与之对应，那么这个方程实际上确定了一个$x$到$y$的函数，称为**隐函数**. 我们当然可以用$y=f(x)$来表示，只是一般我们没有办法得到解析的关系式罢了.

如果这个隐函数是可导的，当然可以求出其在某个点$(x,y)$处的导数. 只需要对$F(x,y)=0$两侧对$x$求导即可. 这里要注意，方程中的$y$不再是自由变量，而是$x$的函数，所以在对$x$求导时，也要对$y$使用链式法则求导. 我们使用偏微分的记号，那么有

$$
F_x'+F_y'y_x'=0
$$

于是

$$
y_x' = -\frac{F_x'}{F_y'}
$$

当然可以继续求更高阶的导数，例如可以对$F_x'+F_y'y_x'=0$两侧继续对$x$求导，于是有（注意$F_x'$和$F_y'$也是包含两个变量的函数！）

$$
(F_{xx}''+F_{xy}''y_x')+(F_{yx}''+F_{yy}''y_x')y_x'+F_y'y_{xx}''=0
$$

从而

$$
y_{xx}''=\frac{-F_{xx}''-2F_{xy}''(y_x')-F_{yy}''(y_x')^2}{F_y'}=\frac{-F_{xx}''(F_{y}')^2-F_{yy}''(F_x')^2+2F_{xy}''F_x'F_y'}{(F_y')^3}
$$

这个式子也可以通过对$y_x' = -\dfrac{F_x'}{F_y'}$求导得到.

可以把反函数视为隐函数的一种情形，即对于$F(x,y)=f(x)-y=0$，如果在$P(x,y)$附近有反函数存在，那么由上面的结论，可以通过对$y$求导来得到反函数的导数，有

$$
x_y'=-\frac{F_y'}{F_x'}=\frac{1}{f'}
$$

以及更高阶的导数

$$
x_{yy}''=-\frac{f''}{(f')^3}
$$

> - 用这种方法得到的导数表达式，其中往往同时含有$x$和$y$，因此在计算某一点导数值时，需要先算出对应的$y$，然后把$x$和$y$的值同时代入进去.
> - 上面的表达式看上去比较复杂，是因为我们使用了抽象的表达式. 在面对实际具体的函数时，可以直接用所说的方法求导，而不必套用公式.
> - 有关隐函数及反函数的存在性、连续性和可导性，以及上述方法更严谨的形式证明，都放在了多元函数部分. 那一章会得到一些更一般的结论.

（4）**参数方程和极坐标下的导数**

有的函数会使用参数方程来描述：

$$
\begin{cases}
x = \varphi(t) \\ y = \psi(t)
\end{cases}
$$

则某个点$t$对应的点$(x,y)=(\varphi(t),\psi(t))$的导数为

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=\frac{\psi'(t)}{\varphi'(t)}=\frac{y_t'}{x_t'}
$$

$$
\frac{\mathrm{d}^2 y}{\mathrm{d} x^2}=\frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)=\frac{\dfrac{\mathrm{d}}{\mathrm{d}t}\left(\dfrac{\mathrm{d}y}{\mathrm{d}x}\right)}{\dfrac{\mathrm{d}x}{\mathrm{d}t}}=\frac{\psi''\varphi'-\psi'\varphi''}{(\varphi')^3}
$$

如果函数使用极坐标的形式给出$\rho=\rho(\theta)$，那么有

$$
\begin{cases}
x=\rho\cos\theta=\rho(\theta)\cos\theta=\varphi(\theta)\\
y=\rho\sin\theta=\rho(\theta)\sin\theta=\psi(\theta)
\end{cases}
$$

于是可以按照参数方程的方式来处理.


## 一元函数的微分 Differentials

### 一阶微分

设$f$在$x_0$的邻域内有定义，记自变量$\Delta x$引起的函数变化量为$\Delta y=f(x_0+\Delta x)-f(x_0)$. 如果存在**常数**$A$，使得对于任意$\Delta x$总有

$$
\Delta y = A\Delta x+o(\Delta x),\quad \Delta x\to 0
$$

则称$f$在$x_0$是**可微的**，称$A\Delta x$是$f$在$x_0$处的**微分**（differential），记为

$$
\mathrm{d}y = \mathrm{d}f =A\Delta x
$$

可见$\Delta y$和$\mathrm{d} y$不是等价的. 后者是对前者的*近似*. 但有一个例外，那就是恒等映射$f(x)=x$，对于恒等映射而言，$\Delta f$严格等于$\mathrm{d}f$，而$\mathrm{d}f=\Delta x$（使用微分的定义），且$\mathrm{d}f=\mathrm{d}x$（代入$f$的表达式），于是$\mathrm{d}x=\Delta x$. 这样可微函数$f$的微分也可以表达为

$$
\mathrm{d}y = \mathrm{d}f =A\mathrm{d} x
$$

### 一阶微分的性质和计算

（1）**可微等价于可导**. $f$在$x_0$可微当且仅当在$x_0$可导，且$\mathrm{d}f=f'(x_0)\mathrm{d}x$.

> 这一结论对一元函数是显然的，但对于多元函数是不成立的. 详见多元函数部分.

因此，微分继承了导数的性质和计算方法，例如有

$$
\mathrm{d}\sin x=\cos x\mathrm{d}x
$$

$$
\mathrm{d}(u+v)=\mathrm{d}u+\mathrm{d}v
$$

$$
\mathrm{d}\left(\frac{u}{v}\right)=\frac{v\mathrm{d}u-u\mathrm{d}v}{v^2}
$$

（2）**一阶微分的形式不变性**. 考虑一个可微的复合函数$y=f(g(x))$，令$u=g(x)$，如果选择$u$为自变量，则有$\mathrm{d}y=y_u'\mathrm{d}u$. 如果选择$x$为自变量，有$\mathrm{d}y=y_x'\mathrm{d}x$. 根据复合函数导数的链式法则，我们又有$\mathrm{d}y=y_x'\mathrm{d}x=(y_u'u_x')\mathrm{d}x=y_u'(u_x'\mathrm{d}x)=y_u'\mathrm{d}u$. 我们又回来了！无论$x$是作为自由的自变量还是中间变量，我们总能得到相同的形式，是为一阶微分的形式不变性.

### 高阶微分

在表达式$\mathrm{d}y=y_x'\mathrm{d}x$中，如果再次考虑增量$\mathrm{d}x$对左侧$\mathrm{d}y$的影响，则可以得到高阶微分. 两侧对$x$取微分，由于$x$的增量$\mathrm{d}x$并不依赖于$x$的选取，取微分时可以视为常系数，那么

$$
\mathrm{d}^2 y=\mathrm{d}(\mathrm{d}y)=\mathrm{d}(y_x'\mathrm{d}x)=\mathrm{d}y_x'\mathrm{d}x=y_{xx}''\mathrm{d}x\mathrm{d}x=y_{xx}''\mathrm{d}x^2
$$

归纳地，我们有$\mathrm{d}^n y=y^{(n)}\mathrm{d}x^n$.

**高阶微分不具备形式不变性**. 考虑一个二阶可微的复合函数$\displaystyle x\xrightarrow{g} u\xrightarrow{f} y$. 倘若$u$为**自由的**自变量，我们有$\mathrm{d}^2y=y_{uu}''\mathrm{d}u^2$. 现在考虑$u$被$x$控制的情形，以$x$为自变量，我们有$\mathrm{d}^2y=y_{xx}''\mathrm{d}x^2$. 根据求导法则，我们有$y_{xx}''=(y_u'u_x')'=y_{uu}''(u_x)^2+y_u'u_{xx}''$，那么$\mathrm{d}^2 y=y_{uu}''(u_x)^2\mathrm{d}x^2+y_u'u_{xx}''\mathrm{d}x^2=y_{uu}''(u_x\mathrm{d}x)^2+y_u'(u_{xx}''\mathrm{d}x^2)=y_{uu}''\mathrm{d}u^2+y_u'\mathrm{d}^2u$. 可见，高阶微分不具备形式不变性，当$u$是自由的自变量，或者是非自由的中间变量时，高阶微分的表达式完全不同.

```{admonition} Example

为了更具体地说明，考虑这个例子：$x=t^2$而$y=x^2$. 那么有$y=t^4$，又因为$y''=12t^2$，故$\mathrm{d}^2y=12t^2\mathrm{d}t^2$. 通过直接代入表达式的方法得到$y$和$t$的关系式，这样得到的答案是没问题的.

但有人试图这样来做：因为$y=x^2$，故$\mathrm{d}^2y=2\mathrm{d}x^2$，又因为$x=t^2$，故$\mathrm{d}x=2t\mathrm{d}t$. 于是$\mathrm{d}^2y=2\mathrm{d}x^2=2(2t\mathrm{d}t)^2=8t^2\mathrm{d}t^2$. 得到了一个错误的答案！

这是因为此时$x$不是自由变量，而是中间变量，因此$\mathrm{d}^2y=2\mathrm{d}x^2$不成立，而是$\mathrm{d}^2y=2\mathrm{d}x^2+2\mathrm{d}^2x$，其中$\mathrm{d}^2x=2\mathrm{d}t^2$. 现在再次代入，得到$\mathrm{d}^2y=8t^2\mathrm{d}t^2+4t^2\mathrm{d}t^2=12t^2\mathrm{d}t^2$，这样就和第一种方法对上了.

总之，当$x$作为自由变量和中间变量时，高阶微分形式完全不同.

```

## 微分学应用1：中值定理和洛必达法则

### 中值定理

（1）**费马（Fermat）定理**：若$x_0$是$f$的一个极值点，且$f'(x_0)$存在，则必有$f'(x_0)=0$.

> 如果$f'(x_0)$不是0，那么就必然严格大于0或严格小于0，此时$f$在$x_0$的邻域内严格单调递增或递减，那么$x_0$就不可能是极值点了.

（2）**罗尔（Rolle）中值定理**：若$f$在$[a,b]$连续，在$(a,b)$可导，且$f(a)=f(b)$，则$\exists \xi\in(a,b)$使得$f'(\xi)=0$.

> 如果$f(x)$在区间内是定值，结论是显然的. 对于非平凡情形，则闭区间内的$f$必有最大值和最小值，且其中至少有一个不等于$f(a)$和$f(b)$，这个最值点必然也是极值点，因此由Fermat定理可知此处导数为0.

（3）**柯西（Cauchy）中值定理**：设$f,g$在$[a,b]$连续，在$(a,b)$可导，且$g'(x)\neq 0$，则$\exists \xi\in(a,b)$使得$\dfrac{f'(\xi)}{g'(\xi)}=\dfrac{f(b)-f(a)}{g(b)-g(a)}$. （由于$g'(x)\neq 0$，由Rolle中值定理可知肯定有$g(a)\neq g(b)$，故无须担心等式右侧的分母是否为0.）

> 构造辅助函数$F(x)=[f(x)-f(a)]-\dfrac{f(b)-f(a)}{g(b)-g(a)}[g(x)-g(a)]$，使用Rolle中值定理就能得到这一结论.

（4）**拉格朗日（Lagrange）中值定理**：设$f$在$[a,b]$连续，在$(a,b)$可导，则$\exists \xi\in(a,b)$使得$f'(\xi)=\dfrac{f(b)-f(a)}{b-a}$. 

> 显然，Lagrange中值定理是Cauchy中值定理在$g(x)=x$时的一个特例.

Lagrange中值定理的另外一种形式为：$f(b)=f(a)+f'(\xi)(b-a)$，其中$a < \xi < b$. 当然可以换一种写法：我们仍考虑$x_0$处一个很小的扰动$\Delta x$对函数值带来的影响，那么

$$
\Delta y = f(x_0+\Delta x)-f(x_0)=f'(x_0+\theta\Delta x)\Delta x,\quad \theta\in(0,1)
$$

```{tip}

目前，对于$\Delta y$的估计，我们已经有了两种方式：

$$
\Delta y = f'(x_0)\Delta x + o(\Delta x)
$$

$$
\Delta y = f'(x_0+\theta\Delta x)\Delta x,\,\theta \in (0,1)
$$

第一个公式来自微分的定义，第二个公式来自Lagrange中值定理. 在第一个公式中，我们不知道$o(\Delta x)$具体是多少，但知道它是$\Delta x$的高阶无穷小；在第二个公式中，我们不知道$\theta$具体是多少，但知道它在$(0,1)$这个范围内.

```

（5）**达布（Darboux）定理**：若$f$在$[a,b]$可导，则对于$x\in [a,b]$，$f'(x)$可以取遍$f'_+(a)$和$f'_{-}(b)$之间的每一个值.

### 洛必达法则

## 微分学应用2：泰勒公式 Appilication II: Taylor's Formula

### 泰勒多项式

泰勒公式的思想是用一个线性的多项式$P_n(x)=a_nx^n+\cdots+a_1x+a_0$去拟合一个非线性的可微函数$f(x)$的片段. 不难注意到有$a_k = \dfrac{P_n^{(k)}(0)}{k!}$. 更一般地，如果$P_n(x)$有$P_n(x)=a_n(x-x_0)^n+\cdots+a_1(x-x_0)+a_0$的形式，则有$a_k=\dfrac{P_n^{(k)}(x_0)}{k!}$. 现在考虑一个非线性的$n$**次可微**函数$f$，在$x_0$附近我们试图用上面这种多项式来拟合$f(x)$，那么通过对比系数，就应该有

$$
f(x)\approx P_n(x) = f(x_0)+f'(x_0)(x-x_0)+\cdots+\dfrac{f^{(n)}(x_0)}{n!}(x-x_0)^n
$$

称$P_n(x)=\displaystyle\sum_{k=0}^{n}\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k$称为$f$在$x_0$处的$n$阶**Taylor多项式**. 理论上多项式的阶数越高，那么拟合就应该越精准. 我们将拟合的误差$R_n(x):=f(x)-P_n(x)$称为**余项**（reminder）. 下面一小节提供了几种估计余项的形式.

> 容易验证，我们有$R_n(x_0)=R_n'(x_0)=\cdots=R_n^{(n)}(x_0)=0$. 这一点在下一小节的证明中会经常用到.

### 余项的形式

（1）**皮亚诺（Peano）余项**：如果$f$是$n$阶可导的，那么$R_n(x)=o((x-x_0)^n)$. 即Taylor多项式的拟合误差是$(x-x_0)^n$的高阶无穷小.

```{admonition} 证明过程
:class: dropdown, tip

即证$\displaystyle\lim_{x\to x_0}\frac{R_n(x)}{(x-x_0)^n}=0$. 使用$n-1$次L'Hospital法则，有

$$\begin{align*}
& \lim_{x\to x_0}\frac{f^{(n-1)}(x)-[f^{(n)}(x_0)(x-x_0)+f^{(n-1)}(x_0)]}{n!(x-x_0)} \\ = &\lim_{x\to x_0}\frac{1}{n!}\left[\frac{f^{(n-1)}(x)-f^{(n-1)}(x_0)}{x-x_0}-f^{(n)}(x_0)\right]=0
\end{align*}
$$

得证.

---

这里需要使用$n-1$次L'Hospital法则，而不是$n$次. 使用$n$次我们将会得到$\displaystyle\lim_{x\to x_0}\frac{f^{(n)}(x)-f^{(n)}(x_0)}{n!}$. 但是，条件只告诉我们$f$的$n$阶导数**存在**，而没有告诉我们$n$阶导数**连续**，那么这个极限就不一定为0.


```

（2）**拉格朗日（Lagrange）余项**：如果$f$是$n+1$阶可导的，那么$R_n(x)=\dfrac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}$. 其中$\xi$是某个介于$x$和$x_0$之间的数. 也可以写作$\xi=x_0+\theta(x-x_0)$，其中$\theta\in(0,1)$.

```{attention}

注意，Lagrange余项要求$f$是$n+1$阶可导的，这比上面的Peano余项要求要严格一些.

```

```{admonition} 证明过程
:class: tip, dropdown

对$\dfrac{R_n(x)}{(x-x_0)^{n+1}}$使用柯西中值定理即可. 我们有

$$
\begin{align*}
& \frac{R_n(x)}{(x-x_0)^{n+1}} = \frac{R_n(x)-R_n(x_0)}{(x-x_0)^{n+1}-(x_0-x_0)^{n+1}} \\
= & \frac{R_n'(\xi_1)}{(n+1)(\xi_1-x_0)^{n}} = \frac{R_n'(\xi_1) - R_n'(x_0)}{(n+1)[(\xi_1-x_0)^{n}-(x_0-x_0)^{n}]} \\
= & \frac{R_n''(\xi_2)}{(n+1)n(\xi_2-x_0)^{n-1}} = \frac{R_n''(\xi_2) - R_n''(x_0)}{(n+1)n[(\xi_2-x_0)^{n-1}-(x_0-x_0)^{n-1}]} \\
= & \cdots \\
= & \frac{R_n^{(n)}(\xi_n)}{(n+1)!(\xi_n-x_0)} = \frac{R_n^{(n)}(\xi_1) - R_n^{(n)}(x_0)}{(n+1)![(\xi_n-x_0)-(x_0-x_0)]} \\
= & \frac{R_n^{(n+1)}(\xi_{n+1})}{(n+1)!} = \frac{f^{(n+1)}(\xi_{n+1})}{(n+1)!}
\end{align*}
$$

其中$x_0 < \xi_{n+1} < \xi_n < \cdots < \xi_1 < x$或者$x_0 > \xi_{n+1} > \xi_n > \cdots > \xi_1 > x$，令$\xi=\xi_{n+1}$，就这样我们得到了

$$
R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}
$$

```

（3）**施勒米尔希-洛希（Schlömilch-Roche）余项**：设$f$是$n+1$阶可导的，我们有

$$
R_n(x)=\frac{f^{(n+1)}(\xi)}{n!p}(x-\xi)^{n-p+1}(x-x_0)^{p}
$$

其中$\xi$是$x$和$x_0$之间的某个数，$p>0$. 如果使用$\xi=x_0+\theta(x-x_0)$这一形式，可以得到

$$
R_n(x)=\frac{f^{(n+1)}(x_0+\theta(x-x_0))}{n!p}(1-\theta)^{n-p+1}(x-x_0)^{n+1}
$$

```{admonition} 推导过程
:class: dropdown, tip

我们知道$R_n=\displaystyle f(x)-\sum_{k=0}^{n}\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k$，我们把其中的$x_0$换成$z$，定义新的函数

$$
\varphi(z)= f(x)-\sum_{k=0}^{n}\frac{f^{(k)}(z)}{k!}(x-z)^k
$$

其中$z\in[x_0,x]$或者$[x,x_0]$，并且注意到端点处有$\varphi(x)=0$和$\varphi(x_0)=R_n(x)$.

假设$\psi$是一个可导的函数，那么使用Cauchy中值定理，有$\dfrac{\varphi(x)-\varphi(x_0)}{\psi(x)-\psi(x_0)}=\dfrac{\varphi'(\xi)}{\psi'(\xi)}$，于是

$$
-R_n(x)=\frac{\psi(x)-\psi(x_0)}{\psi'(\xi)}\varphi'(\xi)
$$

对$\varphi(z)$求导，我们不难发现

$$\begin{align*}
\varphi'(z) & = \frac{\mathrm{d}}{\mathrm{d}z}\left[-f(z)-\sum_{k=1}^{n}\frac{f^{(k)}(z)}{k!}(x-z)^k\right] \\
& = -f'(z)-\sum_{k=1}^{n}\left[\frac{f^{(k+1)}(z)}{k!}(x-z)^k-\frac{f^{(k)}(z)}{(k-1)!}(x-z)^{k-1} \right] \\
& = -\frac{f^{(n+1)}(z)}{n!}(x-z)^n
\end{align*}$$

于是$\displaystyle R_n(x)=\frac{\psi(x)-\psi(x_0)}{\psi'(\xi)}\frac{f^{(n+1)}(\xi)}{n!}(x-\xi)^n$. 别忘了这里$\psi$是一个可导函数即可. 那么为了简单一点，干脆取$\psi(z)=(x-z)^{p}$，其中$p>1$，那么$\displaystyle \frac{\psi(x)-\psi(x_0)}{\psi'(\xi)} = \frac{-(x-x_0)^p}{-p(x-\xi)^{p-1}}$，代入之前的式子，我们最终得到

$$
R_n(x)=\frac{f^{(n+1)}(\xi)}{n!p}(x-\xi)^{n-p+1}(x-x_0)^{p}
$$

如果使用$\xi=x_0+\theta(x-x_0)$这一形式，可以得到

$$
R_n(x)=\frac{f^{(n+1)}(x_0+\theta(x-x_0))}{n!p}(1-\theta)^{n-p+1}(x-x_0)^{n+1}
$$

---

事实上，我们不难发现，如果我们取$p=n+1$，就得到了Lagrange余项形式；而如果取$p=1$，就得到了Cauchy余项形式.

也可以选取其他的$p$，例如，选择$p=n$，那么有

$$
\mathrm{e}^x=1+x+\cdots+\frac{x^n}{n!}+\frac{\mathrm{e}^{\theta x}(1-\theta)x^{n+1}}{n!n}
$$

代入$x=1$，并且易证$0<\theta<1$时也有$0 < \mathrm{e}^\theta(1-\theta) < 1$，于是

$$
\mathrm{e} = 1 + 1 + \frac{1}{2!} + \cdots + \frac{1}{n!} + \frac{\eta}{n!n},\quad \eta\in(0,1)
$$

这个等式可以用于证明$\mathrm{e}$是无理数.

```

（4）**柯西（Cauchy）余项**：

（5）**积分余项**：


## 微分学应用3：函数特性的研究 Application III: Characteristics of Functions

### 单调性

首先考虑函数在某个区间$I$上的单调性，即一个函数$f$在区间上是否为常数/单调/严格单调. 下面，我们假定函数在区间内**是可导的**.

（1）常数：$f$在$I$上为常数当且仅当$f'$在$I$上恒为0.

> - 必要性可以由导数定义来说明，充分性可以由Lagrange中值定理来说明.
> - 该命题的一个推论是，若区间$I$上有$f'=g'$，则$I$上$f-g$是一个定值.

（2）单调性：$f$在$I$上单调递增当且仅当在$I$上总有$f'\geqslant 0$，$f$在$I$上单调递减当且仅当在$I$上总有$f'\leqslant 0$.

> 必要性可以由导数定义和极限保号性说明，充分性可以由Lagrange中值定理来说明.

（3）严格单调性：在满足（2）的条件下，如果$f'$在$I$的任意子区间内不恒为0，则其是严格单调的，反之也成立.                                         

> - "$f'$在$I$的任意子区间内不恒为0"指的是，如果对于任意的$x_1$，$x_2$，若$x_1 < x_2$且满足$f'(x_1)=f'(x_2)=0$，则必然能在两个数之间找到第三者$x_3$，使得$f'(x_3)\neq 0$.
> - 如果这一条件得不到满足，那么由（1）可得这个子区间上函数值为常数，不满足严格单调的定义.

类比上述过程，我们也可以考察函数$f$在某点$x_0$附近的单调性，只需要使用极限的保号性即可. $f'(x_0)\geqslant 0$或者让$f'(x_0)\leqslant 0$时有较为直接的结论，而当$f'(x_0)$时情况就比较复杂了.

### 极值和最值

首先回顾极值（点）和最值（点）的定义：

- 如果存在$x_0$，使得在其某个邻域$N(x_0)$内，满足对任意$x\in N(x_0)$都有$f(x)\leqslant f(x_0)$，则称$x_0$是$f$的一个极大值点，而$f(x_0)$为对应的极大值. 同理可以定义极小值（点）、以及严格极大/小值.

- 对于区间$I$，如果存在$x_0\in I$，使得对于$\forall x\in I$，都有$f(x)\leqslant f(x_0)$，则称$x_0$是$f$在$I$上的一个最大值点，而$f(x_0)$为对应的最大值.

寻找函数的最值或者极值是现实中经常遇到的一类问题（优化问题），然而这一问题实质上是困难的，因为我们并不能找到一个严格的办法（充要条件）来判定极值与最值，以及判定是极大还是极小值. 但是下面的一些充分不必要或者必要不充分条件可以一定程度上给我们一些思路.

（1）**必要不充分条件**：Fermat定理. 若$f$可导且$x_0$是其一个极值点，则必有$f'(x_0)=0$.

> - 前面已经给出了证明. 这一定理告诉我们，如果要寻找极值点，则只能从满足$f'(x)=0$的点中去筛查，而没有必要去关心那些导数不为0的点. 我们将导数为0的点称为**驻点**. 可以理解为函数在此“驻足”，然而，在短暂的驻足后，函数可能继续前进，也可能掉头后退. 正如上面所说，这不是一个充分条件. 因此不是所有的驻点都是极值点. 我们将那些非极值点的驻点称为鞍点.
> - 这一定理的条件是$f$可导. 如果没有这一条件，即允许$f$是非光滑的，那么函数的极值有可能在一些导数不存在（左右导数不等或者导数为无穷大）的点取得.

（2）**充分不必要条件**：若$f$可导且在$x_0$处导数为0，若$x_0$的左右两侧$f'$异号，则$x_0$必然是极值点. 特别地，若$x_0$左侧$f' > 0$而$x_0$右侧$f' < 0$，则$x_0$是一个极大值点. 反之，若$x_0$左侧$f' < 0$而$x_0$右侧$f' > 0$，则$x_0$是一个极小值点.

> - 这一结论可以直接由函数的单调性分析得出.

### 凹凸性和拐点

### 渐近线

### 插值问题