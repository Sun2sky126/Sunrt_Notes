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

（2）**一阶微分的形式不变性**. 考虑一个可微的复合函数$y=f(g(x))$，令$u=g(x)$，如果选择$u$为自变量，则有$\mathrm{d}y=y_u'\mathrm{d}u$. 如果选择$x$为自变量，有$\mathrm{d}y=y_x'\mathrm{d}x$. 根据复合函数导数的链式法则，我们又有$\mathrm{d}y=y_x'\mathrm{d}x=(y_u'u_x')\mathrm{d}x=y_u'(u_x'\mathrm{d}x)=y_u'\mathrm{d}u$. 我们又回来了！无论选择那个自变量，我们总能得到相同的形式，是为微分的形式不变性.

### 高阶微分

在表达式$\mathrm{d}y=y_x'\mathrm{d}x$中，如果再次考虑增量$\mathrm{d}x$对左侧$\mathrm{d}y$的影响，则可以得到高阶微分. 两侧对$x$取微分，由于$x$的增量$\mathrm{d}x$并不依赖于$x$的选取，取微分时可以视为常系数，那么

$$
\mathrm{d}^2 y=\mathrm{d}(\mathrm{d}y)=\mathrm{d}(y_x'\mathrm{d}x)=\mathrm{d}y_x'\mathrm{d}x=y_{xx}''\mathrm{d}x\mathrm{d}x=y_{xx}''\mathrm{d}x^2
$$

归纳地，我们有$\mathrm{d}^n y=y^{(n)}\mathrm{d}x^n$.

**高阶微分不具备形式不变性**. 考虑一个二阶可微的复合函数$\displaystyle x\xrightarrow{g} u\xrightarrow{f} y$. 倘若$u$为**自由的**自变量，我们有$\mathrm{d}^2y=y_{uu}''\mathrm{d}u^2$. 现在考虑$u$被$x$控制的情形，以$x$为自变量，我们有$\mathrm{d}^2y=y_{xx}''\mathrm{d}x^2$. 根据求导法则，我们有$y_{xx}''=(y_u'u_x')'=y_{uu}''(u_x)^2+y_u'u_{xx}''$，那么$\mathrm{d}^2 y=y_{uu}''(u_x)^2\mathrm{d}x^2+y_u'u_{xx}''\mathrm{d}x^2=y_{uu}''(u_x\mathrm{d}x)^2+y_u'(u_{xx}''\mathrm{d}x^2)=y_{uu}''\mathrm{d}u^2+y_u'\mathrm{d}^2u$. 可见，高阶微分不具备形式不变形，当$u$是自由的自变量，或者是非自由的中间变量时，高阶微分的表达式完全不同.

```{admonition} Example

为了更具体地说明，考虑这个例子：$x=t^2$而$y=x^2$. 那么有$y=t^4$，又因为$y''=12t^2$，故$\mathrm{d}^2y=12t^2\mathrm{d}t^2$. 通过直接代入表达式的方法得到$y$和$t$的关系式，这样得到的答案是没问题的.

但有人试图这样来做：因为$y=x^2$，故$\mathrm{d}^2y=2\mathrm{d}x^2$，又因为$x=t^2$，故$\mathrm{d}x=2t\mathrm{d}t$. 于是$\mathrm{d}^2y=2\mathrm{d}x^2=2(2t\mathrm{d}t)^2=8t^2\mathrm{d}t^2$. 得到了一个错误的答案！

这是因为此时$x$不是自由变量，而是中间变量，因此$\mathrm{d}^2y=2\mathrm{d}x^2$不成立，而是$\mathrm{d}^2y=2\mathrm{d}x^2+2\mathrm{d}^2x$，其中$\mathrm{d}^2x=2\mathrm{d}t^2$. 现在再次代入，得到$\mathrm{d}^2y=8t^2\mathrm{d}t^2+4t^2\mathrm{d}t^2=12t^2\mathrm{d}t^2$，这样就和第一种方法对上了.

总之，当$x$作为自由变量和中间变量时，高阶微分形式完全不同.

```

## 微分学应用1：函数特性的研究 Application I: Characteristics of Functions

## 微分学应用2：中值定理和洛必达法则

## 微分学应用3：泰勒公式