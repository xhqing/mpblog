## 什么是数据中心化？

数据中心化可以理解为把样本集的中心平移到坐标原点的位置，或理解为把坐标平移到样本集中心的位置，这个“中心”就是样本均值，因此容易理解平移后的样本均值为$\boldsymbol{0}$。

具体地，假设样本集$D$中的某一个样本为$\boldsymbol{x}_i$，共有$m$个样本，样本均值矢量记为$\boldsymbol{\mu}$，平移后的样本记为$\boldsymbol x_i'$，则
$$
\boldsymbol x_i' = \boldsymbol{x}_i-\boldsymbol{\mu}
$$
记平移后的均值为$\boldsymbol{\mu}'$，则
$$
\begin{aligned}
\boldsymbol{\mu}' &= \frac{1}{m}\sum_{i=1}^m\boldsymbol x_i' \\
&= \frac{1}{m}\sum_{i=1}^m\left(\boldsymbol{x}_i-\boldsymbol{\mu}\right) \\
&= \boldsymbol{0}
\end{aligned}
$$
以上就是中心化(Zero-Centered)处理，就是每个样本都减去均值矢量，很简单。

现在来进一步研究一下中心化处理后样本集的方差是否发生变化，假设原始样本集的方差矢量为$\boldsymbol{v}$，中心化处理后的样本集的方差矢量为$\boldsymbol{v}'$，特征维数为$d$，原坐标的单位正交基矢量为$\boldsymbol{e}_j$，$j=1,\cdots,d$，则
$$
\begin{aligned}
\boldsymbol{v} &= \sum_{j=1}^d\left(\frac{1}{m}\sum_{i=1}^m\left(\boldsymbol{x}_i-\boldsymbol{\mu}\right)\left(\boldsymbol{x}_i-\boldsymbol{\mu}\right)^{\mathrm T}\circ \mathbf I\right)\boldsymbol{e}_j \\
&= \sum_{j=1}^d\left(\frac{1}{m}\sum_{i=1}^m\boldsymbol x_i'\boldsymbol x_i'^{\mathrm T}\circ \mathbf I\right)\boldsymbol{e}_j\\
&= \boldsymbol{v}'
\end{aligned}
$$
其中$\mathbf I$为$d$阶单位方阵。

由以上简单分析知道数据中心化处理后方差是没有发生变化的，可以理解为所有样本整体进行平移，样本的离散程度没有发生任何变化，或者可以更简单的理解为所有样本点本身在空间中的位置没有变，只是坐标进行了平移，所以样本集整体的任何特性都不会发生变化，仅仅是表示它们的坐标发生了变化。

## 什么是数据标准化？

标准化(Standardization/Normalization)方法有非常多种，一般情况下提及"标准化"默认是指经过标准化处理后所有特征的均值均为$0$，标准差均为$1$的标准化。由此可见，标准化是在中心化的基础上对标准差做了进一步处理，使得每一个特征的标准差均为$1$。

具体地，假设原始数据集的均值矢量记为$\boldsymbol{\mu}$，标准差矢量记为$\boldsymbol{\sigma}$，并且$\boldsymbol{\sigma}$的所有元素均为非$0$元素，样本集$D$中的某一个样本记为$\boldsymbol{x}_i$，标准化后的样本记为$\boldsymbol{x}_i'$，则对原始数据集的标准化可以定义为
$$
\boldsymbol {x}_i'\circ\boldsymbol{\sigma} = \boldsymbol{x}_i-\boldsymbol{\mu}
$$

假设原始数据集共有$m$个样本，记标准化后的均值矢量为$\boldsymbol{\mu}'$，则
$$
\begin{aligned}
\boldsymbol{\sigma}\circ\boldsymbol{\mu}' &= \boldsymbol{\sigma}\circ\frac{1}{m}\sum_{i=1}^m\boldsymbol x_i'\\
&= \frac{1}{m}\sum_{i=1}^m\left(\boldsymbol x_i'\circ\boldsymbol{\sigma}\right)\\
&= \frac{1}{m}\sum_{i=1}^m\left(\boldsymbol{x}_i-\boldsymbol{\mu}\right)\\
&= \boldsymbol{0}
\end{aligned}
$$
由于$\boldsymbol{\sigma}$的所有元素均为非$0$元素，因此$\boldsymbol{\mu}'=\boldsymbol{0}$，也就是说，标准化处理后所有特征的均值均为$0$。

现在来进一步研究一下标准化处理后样本集的方差是否发生变化，假设原始样本集的方差矢量为$\boldsymbol{v}=\boldsymbol{\sigma}\circ\boldsymbol{\sigma}$，标准化处理后的样本集的方差矢量为$\boldsymbol{v}'=\boldsymbol{\sigma}'\circ\boldsymbol{\sigma}'$，特征维数为$d$，原坐标的单位正交基矢量为$\boldsymbol{e}_j$，$j=1,\cdots,d$，则
$$
\begin{aligned}
\boldsymbol{v} &= \sum_{j=1}^d\left(\frac{1}{m}\sum_{i=1}^m\left(\boldsymbol{x}_i-\boldsymbol{\mu}\right)\left(\boldsymbol{x}_i-\boldsymbol{\mu}\right)^{\mathrm T}\circ \mathbf I\right)\boldsymbol{e}_j \\
&= \sum_{j=1}^d\left(\frac{1}{m}\sum_{i=1}^m\left({\boldsymbol x}_i'\circ\boldsymbol{\sigma}\right)\left({\boldsymbol x}_i'\circ\boldsymbol{\sigma}\right)^{\mathrm T}\circ \mathbf I\right)\boldsymbol{e}_j\\
&= \sum_{j=1}^d\left(\frac{1}{m}\sum_{i=1}^m\left({\boldsymbol x}_i'{\boldsymbol x}_i'^{\mathrm T}\right)\circ\left(\boldsymbol{\sigma}\boldsymbol{\sigma}^{\mathrm T}\right)\circ \mathbf I\right)\boldsymbol{e}_j\\
&=\left(\frac{1}{m}\sum_{i=1}^m\left({\boldsymbol x}_i'{\boldsymbol x}_i'^{\mathrm T}\right)\circ\left(\boldsymbol{\sigma}\boldsymbol{\sigma}^{\mathrm T}\right)\circ \mathbf I\right)\sum_{j=1}^d\boldsymbol{e}_j\\
&=\left(\frac{1}{m}\sum_{i=1}^m\left({\boldsymbol x}_i'{\boldsymbol x}_i'^{\mathrm T}\right)\circ\mathbf I\right)\circ\left(\left(\boldsymbol{\sigma}\boldsymbol{\sigma}^{\mathrm T}\right)\circ \mathbf I\right)\sum_{j=1}^d\boldsymbol{e}_j\\
&=\left(\frac{1}{m}\sum_{i=1}^m\left({\boldsymbol x}_i'{\boldsymbol x}_i'^{\mathrm T}\right)\circ\mathbf I\sum_{j=1}^d\boldsymbol{e}_j\right)\circ\left(\left(\left(\boldsymbol{\sigma}\boldsymbol{\sigma}^{\mathrm T}\right)\circ \mathbf I\right)\sum_{j=1}^d\boldsymbol{e}_j\right)\\
&=\boldsymbol{v}'\circ\boldsymbol{v}
\end{aligned}
$$
其中$\mathbf I$为$d$阶单位方阵。由以上推导可以看出$\boldsymbol{v}'$为元素全为$1$的矢量，也就是说，标准化后的所有特征的方差和标准差均为$1$。以下是原始数据，中心化后的数据和标准化后的数据在二维特征下的样本点分布图，可以看出中心化后的数据以坐标原点为对称中心，而标准化后的数据不仅以坐标原点为对称中心而且在各个维度上的离散程度是一样的。
![image-20220124111332166](img/image-20220124111332166.png)

经常看到网络上有一些博文提到标准化处理后的特征都会服从标准正态分布，我对这个结论是非常质疑的，现在我尝试用最严谨的逻辑来研究一下这个问题。

为了简单起见，这里暂时仅讨论特征为一维的情况，首先，服从标准正态分布的数据确实是均值为$0$且标准差为$1$，但这只能说明均值为$0$且标准差为$1$是数据服从标准正态分布的必要条件，那么它是不是充分条件呢？

假设原始数据样本点记为$x$，均值记为$\mu$，非$0$标准差记为$\sigma$，标准化处理后的样本记为$x’$，则
$$
x' = \frac{x-\mu}{\sigma}
$$
假设原始数据$x$服从如下的正态分布
$$
f\left(x\right) = \frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{\left(x-\mu\right)^2}{2\sigma^2}\right)
$$
则标准化处理后$x'$的代数关系如下
$$
\begin{aligned}
f\left(\sigma x'+\mu\right) &= \frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(\sigma x'+\mu-\mu)^2}{2\sigma^2}\right)\\
&= \frac{1}{\sigma}\frac{1}{\sqrt{2\pi}}\exp\left(-\frac{x'^2}{2}\right)\\
&=\frac{1}{\sigma}g\left(x'\right)
\end{aligned}
$$
也即
$$
\sigma f\left(x\right) = g\left(x'\right)=\frac{1}{\sqrt{2\pi}}\exp\left(-\frac{x'^2}{2}\right)
$$
由以上推导可以看出，在原始数据$x$服从形如$f\left(x\right)$的正态分布的前提下，标准化变换后的$x'$服从形如$g\left(x'\right)$的标准正态分布，并且有$\sigma f\left(x\right)=g\left(x'\right)$的关系。但是实际情况中原始数据是很难得会服从正态分布的，如果原始数据不服从正态分布，标准化处理后的数据是否会服从标准正态分布呢？

为了能够证伪在任何情况下标准化处理后的数据都能够服从标准正态分布，需要举一个反例，假设原始数据$x$服从均匀分布$f\left(x\right)$，则
$$
f\left(x\right)=
\begin{cases}
\frac{1}{b-a}, &a<x<b \\
0, &\text{其他} 
\end{cases}
$$




## 什么是数据归一化？



## 什么是数据正态化？

