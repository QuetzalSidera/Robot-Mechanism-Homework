# 第 4 次作业解答

## 说明与假设

1. 第 1 题按标准平面 `3R` 串联机械臂处理，$\theta_1,\theta_2,\theta_3$ 为相邻杆件之间的转角，因此末端姿态角为

$$
\phi=\theta_1+\theta_2+\theta_3
$$

2. 第 2 题建立平面直角坐标系 $\Sigma\{A\}$，取

$$
A=(0,0),\qquad E=(L,0),\qquad C=(x,y)
$$

并记两个移动副的广义坐标分别为

$$
\rho_B,\ \rho_D
$$

它们分别表示左、右支链的伸长量。

## 运行方法

依赖文件： [requirements.txt](/Users/qianshuang/Desktop/homework1/forth/source/requirements.txt)

本次作业当前不包含额外 Python 绘图脚本，因此无需额外运行代码。

## 1. 平面三自由度串联机器人

### (1) 建立运动副旋量集，求秩，并给出一组运动旋量系与约束旋量系

取基座转轴中心为原点 $O$，$x$ 轴水平向右，$y$ 轴竖直向上，$z$ 轴垂直纸面向外。

令

$$
\alpha_1=\theta_1,\qquad
\alpha_2=\theta_1+\theta_2,\qquad
\alpha_3=\theta_1+\theta_2+\theta_3
$$

则三个转动副轴线均平行于 $z$ 轴，对应的运动副旋量可写为

$$
\begin{aligned}
S_1&=(0,0,1;\ 0,0,0)\\
S_2&=(0,0,1;\ l_1\sin\alpha_1,\ -l_1\cos\alpha_1,\ 0)\\
S_3&=(0,0,1;\ l_1\sin\alpha_1+l_2\sin\alpha_2,\ -l_1\cos\alpha_1-l_2\cos\alpha_2,\ 0)
\end{aligned}
$$

写成平面运动的 3 维表示

$$
\tilde S=
\begin{bmatrix}
1 & 1 & 1\\
0 & l_1\sin\alpha_1 & l_1\sin\alpha_1+l_2\sin\alpha_2\\
0 & -l_1\cos\alpha_1 & -l_1\cos\alpha_1-l_2\cos\alpha_2
\end{bmatrix}
$$

其行列式为

$$
\det(\tilde S)=l_1l_2\sin\theta_2
$$

因此在图示一般位形下，$\theta_2\neq k\pi$，故有

$$
\boxed{\operatorname{rank}(\tilde S)=3}
$$

由于图示位形不是共线位形，所以该机构在图示位形下具有完整的平面 3 自由度瞬时运动能力。

又因为平面刚体运动的标准运动旋量空间可由

$$
\begin{aligned}
T_x&=(0,0,0;\ 1,0,0)\\
T_y&=(0,0,0;\ 0,1,0)\\
R_z&=(0,0,1;\ 0,0,0)
\end{aligned}
$$

张成，所以可取一组等价的运动旋量系为

$$
\boxed{\{T_x,\ T_y,\ R_z\}}
$$

与该平面运动互易的一组约束旋量系可取为

$$
\begin{aligned}
W_1&=(0,0,1;\ 0,0,0)\\
W_2&=(0,0,0;\ 1,0,0)\\
W_3&=(0,0,0;\ 0,1,0)
\end{aligned}
$$

即

$$
\boxed{\{W_1,W_2,W_3\}}
$$

### (2) 利用等效运动副旋量系构造等效运动链，至少给出 3 组

由于该机构末端允许运动为平面刚体 3 自由度运动，只要运动副旋量能够张成

$$
\{T_x,\ T_y,\ R_z\}
$$

即可与原运动链等效。

可构造的等效运动链例如：

1. `R-P-P`

$$
\{R_z,\ T_x,\ T_y\}
$$

2. `P-R-P`

$$
\{T_x,\ R_z,\ T_y\}
$$

3. `P-P-R`

$$
\{T_x,\ T_y,\ R_z\}
$$

因此满足题意的 3 组等效运动链可写为

$$
\boxed{RPP,\ PRP,\ PPR}
$$

### (3) 用 POE 公式求正反解运动学，并写出 Jacobian 矩阵

为便于使用 POE，另取零位：令 $\theta_1=\theta_2=\theta_3=0$ 时三根杆全部沿 $x$ 轴正向排列。

此时末端初始位姿为

$$
M=
\begin{bmatrix}
1&0&0&l_1+l_2+l_3\\
0&1&0&0\\
0&0&1&0\\
0&0&0&1
\end{bmatrix}
$$

对应的空间旋量为

$$
\begin{aligned}
S_1&=(0,0,1;\ 0,0,0)\\
S_2&=(0,0,1;\ 0,-l_1,0)\\
S_3&=(0,0,1;\ 0,-(l_1+l_2),0)
\end{aligned}
$$

故 POE 形式为

$$
T(\theta)=e^{[S_1]\theta_1}e^{[S_2]\theta_2}e^{[S_3]\theta_3}M
$$

其正运动学结果为

$$
\boxed{
\begin{aligned}
x&=l_1\cos\theta_1+l_2\cos(\theta_1+\theta_2)+l_3\cos(\theta_1+\theta_2+\theta_3)\\
y&=l_1\sin\theta_1+l_2\sin(\theta_1+\theta_2)+l_3\sin(\theta_1+\theta_2+\theta_3)\\
\phi&=\theta_1+\theta_2+\theta_3
\end{aligned}}
$$

#### 逆运动学

给定目标位姿 $(x,y,\phi)$，先取腕点

$$
\begin{aligned}
x_w&=x-l_3\cos\phi\\
y_w&=y-l_3\sin\phi
\end{aligned}
$$

则

$$
\cos\theta_2=
\frac{x_w^2+y_w^2-l_1^2-l_2^2}{2l_1l_2}
$$

令

$$
\sin\theta_2=\pm\sqrt{1-\cos^2\theta_2}
$$

则

$$
\theta_2=\operatorname{atan2}(\sin\theta_2,\cos\theta_2)
$$

进一步有

$$
\theta_1=\operatorname{atan2}(y_w,x_w)-\operatorname{atan2}(l_2\sin\theta_2,\ l_1+l_2\cos\theta_2)
$$

最后

$$
\theta_3=\phi-\theta_1-\theta_2
$$

#### Jacobian 矩阵

取末端平面速度

$$
\dot X=
\begin{bmatrix}
\dot x\\
\dot y\\
\dot \phi
\end{bmatrix},
\qquad
\dot q=
\begin{bmatrix}
\dot\theta_1\\
\dot\theta_2\\
\dot\theta_3
\end{bmatrix}
$$

则

$$
\dot X=J(\theta)\dot q
$$

其中

$$
J(\theta)=
\begin{bmatrix}
-l_1s_1-l_2s_{12}-l_3s_{123} & -l_2s_{12}-l_3s_{123} & -l_3s_{123}\\
l_1c_1+l_2c_{12}+l_3c_{123} & l_2c_{12}+l_3c_{123} & l_3c_{123}\\
1 & 1 & 1
\end{bmatrix}
$$

### (4) 是否存在奇异位形？若存在，给出几何条件

存在奇异位形。

奇异条件由

$$
\det J=
l_1l_2\sin\theta_2
+l_1l_3\sin(\theta_2+\theta_3)
+l_2l_3\sin\theta_3
=0
$$

给出，即

$$
\boxed{
l_1l_2\sin\theta_2
+l_1l_3\sin(\theta_2+\theta_3)
+l_2l_3\sin\theta_3=0}
$$

其几何意义是：三个连杆向量形成的有向面积和为零，末端瞬时速度映射退化，机械臂不能在平面内实现任意瞬时位姿速度。

常见特例包括：

1. 三根杆完全伸直；
2. 三根杆折叠到同一直线上；
3. 虽未完全共线，但上式面积和恰好抵消时也会出现奇异。

## 2. 含两个移动副的平面机构

### (1) 自由度分析，以及 C 点相对于基座的自由度

该机构可视为一个平面 `R-P-R-P-R` 闭链。

计数如下：

$$
n=5,\qquad j_1=5
$$

按平面机构 Grübler-Kutzbach 公式

$$
M=3(n-1)-2j_1
$$

得

$$
M=3(5-1)-2\times 5=12-10=2
$$

因此该机构自由度为

$$
\boxed{2}
$$

由于输出只取为点 $C$ 的位置，所以 $C$ 点相对于基座可以实现

$$
\boxed{2T}
$$

即平面内两个平移自由度。

### (2) 建立环路约束方程，并以 B、D 为驱动副求逆解

取定坐标系

$$
A=(0,0),\qquad E=(L,0),\qquad C=(x,y)
$$

若左、右支链的伸长量分别为 $\rho_B,\rho_D$，则由两条支链长度约束有

$$
\left\{
\begin{aligned}
x^2+y^2&=\rho_B^2\\
(x-L)^2+y^2&=\rho_D^2
\end{aligned}
\right.
$$

这就是该机构的环路约束方程。

#### 正解：由驱动副 $\rho_B,\rho_D$ 求 $C$ 点坐标

两式相减得

$$
x=\frac{\rho_B^2-\rho_D^2+L^2}{2L}
$$

再代回得

$$
y=\pm\sqrt{\rho_B^2-x^2}
$$

故

$$
\boxed{
\begin{aligned}
x_C&=\frac{\rho_B^2-\rho_D^2+L^2}{2L}\\
y_C&=\pm\sqrt{\rho_B^2-\left(\frac{\rho_B^2-\rho_D^2+L^2}{2L}\right)^2}
\end{aligned}}
$$

上式对应上、下两种装配支路。图示工作模式取

$$
y_C\ge 0
$$

#### 逆解：由 $C$ 点坐标求驱动副变量

$$
\boxed{
\begin{aligned}
\rho_B&=\sqrt{x^2+y^2}\\
\rho_D&=\sqrt{(x-L)^2+y^2}
\end{aligned}}
$$

### (3) 速度 Jacobian 矩阵，以及 C 点工作空间求解方法

对约束方程对时间求导：

$$
\left\{
\begin{aligned}
x\dot x+y\dot y&=\rho_B\dot\rho_B\\
(x-L)\dot x+y\dot y&=\rho_D\dot\rho_D
\end{aligned}
\right.
$$

写成矩阵形式

$$
\underbrace{
\begin{bmatrix}
x & y\\
x-L & y
\end{bmatrix}}_{A}
\begin{bmatrix}
\dot x\\
\dot y
\end{bmatrix}
=
\underbrace{
\begin{bmatrix}
\rho_B & 0\\
0 & \rho_D
\end{bmatrix}}_{B}
\begin{bmatrix}
\dot\rho_B\\
\dot\rho_D
\end{bmatrix}
$$

因此速度 Jacobian 可写为

$$
\begin{bmatrix}
\dot x\\
\dot y
\end{bmatrix}
=
J
\begin{bmatrix}
\dot\rho_B\\
\dot\rho_D
\end{bmatrix},
\qquad
J=A^{-1}B
$$

其中

$$
\det A=Ly
$$

故当

$$
y=0
$$

时机构处于速度奇异状态，即

$$
\boxed{A,\ C,\ E\ \text{三点共线}}
$$

#### C 点可达工作空间的求解方法

若驱动副行程满足

$$
\rho_B\in[\rho_{B,\min},\rho_{B,\max}],\qquad
\rho_D\in[\rho_{D,\min},\rho_{D,\max}]
$$

则工作空间可以由以下方法求解：

1. **解析法**

由逆解公式得

$$
\sqrt{x^2+y^2}\in[\rho_{B,\min},\rho_{B,\max}]
$$

以及

$$
\sqrt{(x-L)^2+y^2}\in[\rho_{D,\min},\rho_{D,\max}]
$$

因此工作空间就是以 $A$、$E$ 为圆心的两个圆环区域的交集。

2. **数值法**

在 $(x,y)$ 平面上离散采样，对每个采样点检验

$$
\rho_B=\sqrt{x^2+y^2},\qquad
\rho_D=\sqrt{(x-L)^2+y^2}
$$

是否同时满足行程约束；满足者即为可达点。

此外，为保证正解存在，还应满足两圆相交条件

$$
|\rho_B-\rho_D|\le L\le \rho_B+\rho_D
$$

这也是工作空间边界求解时的重要判据。
