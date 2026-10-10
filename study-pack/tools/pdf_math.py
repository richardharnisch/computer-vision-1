"""Explicit, PDF-only math notation. Never rewrite executable code.

The left column is exact authored prose; the right column is its LaTeX form.
Keep this table explicit: guessing where English ends and an equation starts
can silently change a question. Numeric arrays are parsed, not evaluated.
"""

import ast
from collections import Counter
from decimal import Decimal
import re


NOTATION = r"""
Xc = R Xw + t | X_c = R X_w + t
Xc=R@Xw+t | X_c=R X_w+t
C = -R @ t | C=-R t
C = -R.T @ t | C=-R^{\mathsf T}t
C = R.T @ t | C=R^{\mathsf T}t
C = t | C=t
Xc = 0 | X_c=0
R C + t = 0 | R C+t=0
C = -R^(-1)t = -R.T t | C=-R^{-1}t=-R^{\mathsf T}t
K[2,2] | K_{2,2}
i = Lg | i=Lg
g = [0,0,0] | g=\begin{bmatrix}0&0&0\end{bmatrix}
n = g / ||g|| | n=\frac{g}{\lVert g\rVert}
0 < r < 1 | 0<r<1
s = r^gamma | s=r^{\gamma}
0 < gamma < 1 | 0<\gamma<1
r^gamma | r^{\gamma}
sigma^2 = 3^2 + 4^2 = 25 | \sigma^2=3^2+4^2=25
a + i b | a+\mathrm{i}b
sqrt(a*a + b*b), arctan2(b, a) | \sqrt{a^2+b^2},\;\operatorname{arctan2}(b,a)
sqrt(a*a + b*b), arctan2(a, b) | \sqrt{a^2+b^2},\;\operatorname{arctan2}(a,b)
a + b, arctan2(a, b) | a+b,\;\operatorname{arctan2}(a,b)
a*a + b*b, arctan(b/a) | a^2+b^2,\;\arctan\!\left(\frac{b}{a}\right)
d(I*G)/dx = I*(dG/dx) | \frac{\partial(I*G)}{\partial x}=I*\frac{\partial G}{\partial x}
y = mx + b | y=mx+b
m = 0 | m=0
w^s | w^s
[Ix, Iy] | \begin{bmatrix}I_x&I_y\end{bmatrix}
A.T @ A | A^{\mathsf T}A
A @ A.T | AA^{\mathsf T}
A.T A | A^{\mathsf T}A
Ix^2 | I_x^2
Ix Iy | I_x I_y
Iy^2 | I_y^2
H = K2 R21 K1^(-1) | H=K_2 R_{21}K_1^{-1}
||h|| = 1 | \lVert h\rVert=1
min ||A h||^2 | \min_h\lVert Ah\rVert^2
h = 0 | h=0
TP = 0 | \mathrm{TP}=0
F x | Fx
C = [1,2,0] | C=\begin{bmatrix}1&2&0\end{bmatrix}
Xw = [3,5,4] | X_w=\begin{bmatrix}3&5&4\end{bmatrix}
Xc = R @ (Xw-C) | X_c=R(X_w-C)
q = K @ Xc | q=KX_c
u = q[0]/q[2] | u=\frac{q_0}{q_2}
Xw-C = [2,3,4] | X_w-C=\begin{bmatrix}2&3&4\end{bmatrix}
Xc = [-3,2,4] | X_c=\begin{bmatrix}-3&2&4\end{bmatrix}
q[0] = 800*(-3) + 20*2 + 320*4 = -1080 | q_0=800(-3)+20\cdot2+320\cdot4=-1080
u = -270 | u=-270
rho = ||g|| | \rho=\lVert g\rVert
L.T L = diag(1.28,1.28,2.44) | L^{\mathsf T}L=\operatorname{diag}(1.28,1.28,2.44)
L.T i = [0.384,0.064,1.66] | L^{\mathsf T}i=\begin{bmatrix}0.384&0.064&1.66\end{bmatrix}
g = [0.3,0.05,1.66/2.44] | g=\begin{bmatrix}0.3&0.05&1.66/2.44\end{bmatrix}
n proportional to [-p,-q,1] | n\propto\begin{bmatrix}-p&-q&1\end{bmatrix}
p = dz/dx | p=\frac{\partial z}{\partial x}
q = dz/dy | q=\frac{\partial z}{\partial y}
z(0,0) = 5 | z(0,0)=5
z(3,4) | z(3,4)
p = -2/2 = -1 | p=-\frac{2}{2}=-1
q = -(-1)/2 = 0.5 | q=-\frac{-1}{2}=0.5
z(3,4) = 5 + 3*(-1) + 4*0.5 = 4 | z(3,4)=5+3(-1)+4\cdot0.5=4
T(r) = floor(3 * CDF(r)) | T(r)=\lfloor3\operatorname{CDF}(r)\rfloor
CDF_min | \operatorname{CDF}_{\min}
T(1) | T(1)
CDF(1) = (1+3)/8 = 0.5 | \operatorname{CDF}(1)=\frac{1+3}{8}=0.5
floor(3*0.5) = 1 | \lfloor3\cdot0.5\rfloor=1
-2 + 1 + 4 + 5 = 8 | -2+1+4+5=8
F[k] = sum(n=0..3) f[n] exp(-2*pi*i*k*n/4) | F_k=\sum_{n=0}^{3}f_n\exp\!\left(-\frac{2\pi\mathrm{i}kn}{4}\right)
f = [1,2,3,4] | f=\begin{bmatrix}1&2&3&4\end{bmatrix}
F[1] | F_1
exp(-i*pi/2) = -i | \exp(-\mathrm{i}\pi/2)=-\mathrm{i}
exp(-i*pi) = -1 | \exp(-\mathrm{i}\pi)=-1
F[1] = 1 - 2i - 3 + 4i = -2 + 2i | F_1=1-2\mathrm{i}-3+4\mathrm{i}=-2+2\mathrm{i}
sqrt(4+4) = sqrt(8) | \sqrt{4+4}=\sqrt{8}
R = det(M) - k * trace(M)^2 | R=\det(M)-k\operatorname{tr}(M)^2
k = 0.04 | k=0.04
det(M) = 81-9 = 72 | \det(M)=81-9=72
trace(M) = 18 | \operatorname{tr}(M)=18
R = 72 - 0.04*324 = 59.04 | R=72-0.04\cdot324=59.04
Ix*u + Iy*v = -It | I_x u+I_y v=-I_t
A.T(-It) = [13,0] | A^{\mathsf T}(-I_t)=\begin{bmatrix}13&0\end{bmatrix}
6u+v=13 | 6u+v=13
u+2v=0 | u+2v=0
u=26/11 | u=\frac{26}{11}
v=-13/11 | v=-\frac{13}{11}
w = 0.6 | w=0.6
p = 0.99 | p=0.99
N = ceil(log(1-p) / log(1-w^4)) | N=\left\lceil\frac{\log(1-p)}{\log(1-w^4)}\right\rceil
0.6^4 = 0.1296 | 0.6^4=0.1296
N = 34 | N=34
H @ [5,4,1] = [11,2,1.5] | H\begin{bmatrix}5&4&1\end{bmatrix}^{\mathsf T}=\begin{bmatrix}11&2&1.5\end{bmatrix}^{\mathsf T}
x' = 11/1.5 = 7.3333 | x'=\frac{11}{1.5}=7.3333
(x,y) = (0.25,0.75) | (x,y)=(0.25,0.75)
I[0,0]=10 | I_{0,0}=10
I[0,1]=30 | I_{0,1}=30
I[1,0]=50 | I_{1,0}=50
I[1,1]=90 | I_{1,1}=90
I[y,x] | I_{y,x}
(1-x)(1-y), x(1-y), (1-x)y and xy | (1-x)(1-y),\;x(1-y),\;(1-x)y\text{ and }xy
1.875 + 1.875 + 28.125 + 16.875 = 48.75 | 1.875+1.875+28.125+16.875=48.75
TP=12, FP=2+4=6, FN=3+5=8 | \mathrm{TP}=12,\;\mathrm{FP}=2+4=6,\;\mathrm{FN}=3+5=8
F1 = 2TP/(2TP+FP+FN) = 24/38 = 0.6315789 | F_1=\frac{2\mathrm{TP}}{2\mathrm{TP}+\mathrm{FP}+\mathrm{FN}}=\frac{24}{38}=0.6315789
AP = (sum of precision at each relevant rank) / total relevant images | \mathrm{AP}=\frac{\text{sum of precision at each relevant rank}}{\text{total relevant images}}
AP = (1/1 + 2/3 + 3/5)/4 = 17/30 | \mathrm{AP}=\frac{1/1+2/3+3/5}{4}=\frac{17}{30}
[xmin,ymin,xmax,ymax] | [x_{\min},y_{\min},x_{\max},y_{\max}]
width = xmax-xmin | \text{width}=x_{\max}-x_{\min}
Union = 24+24-12 = 36 | \text{Union}=24+24-12=36
IoU = 12/36 = 1/3 | \mathrm{IoU}=\frac{12}{36}=\frac{1}{3}
H x W x Cin | H\times W\times C_{\mathrm{in}}
31 x 29 x 3 | 31\times29\times3
5 x 3 | 5\times3
2 x 2 | 2\times2
1 x 0 | 1\times0
Cout = 8 | C_{\mathrm{out}}=8
out = floor((in + 2*pad - kernel)/stride)+1 per axis | \text{out}=\left\lfloor\frac{\text{in}+2\cdot\text{pad}-\text{kernel}}{\text{stride}}\right\rfloor+1\text{ per axis}
Hout = floor((31+2-5)/2)+1 = 15 | H_{\mathrm{out}}=\left\lfloor\frac{31+2-5}{2}\right\rfloor+1=15
Wout = floor((29-3)/2)+1 = 14 | W_{\mathrm{out}}=\left\lfloor\frac{29-3}{2}\right\rfloor+1=14
Total = 15*14*8 = 1680 | \text{Total}=15\cdot14\cdot8=1680
5*3*3 = 45 | 5\cdot3\cdot3=45
8*(45+1) = 368 | 8(45+1)=368
7 x 7 x 16 | 7\times7\times16
7*7*16 = 784 | 7\cdot7\cdot16=784
784*10 | 784\cdot10
10 biases = 7850 | 10\text{ biases}=7850
3 x 3 | 3\times3
r_new = r_old + (kernel-1)*j_old | r_{\mathrm{new}}=r_{\mathrm{old}}+(\text{kernel}-1)j_{\mathrm{old}}
j_new = j_old*stride | j_{\mathrm{new}}=j_{\mathrm{old}}\cdot\text{stride}
r=j=1 | r=j=1
r=3,j=1 | r=3,\;j=1
r=4,j=2 | r=4,\;j=2
r=4+2*2=8,j=2 | r=4+2\cdot2=8,\;j=2
x2.T @ F @ x1 = 0 | x_2^{\mathsf T}Fx_1=0
l2=F@x1 | l_2=Fx_1
distance = abs(a*x+b*y+c)/sqrt(a*a+b*b) | \text{distance}=\frac{\lvert ax+by+c\rvert}{\sqrt{a^2+b^2}}
[a,b,c] | [a,b,c]
l2=[0,-1,7] | l_2=\begin{bmatrix}0&-1&7\end{bmatrix}
y=7 | y=7
y=9 | y=9
distance | -9+7 | / 1 = 2 | \text{distance}\;\frac{\lvert-9+7\rvert}{1}=2
R2.T @ R1.T | R_2^{\mathsf T}R_1^{\mathsf T}
R1.T @ R2.T | R_1^{\mathsf T}R_2^{\mathsf T}
R2 @ R1 | R_2 R_1
R1 @ R2 | R_1 R_2
R^(-1)=R.T | R^{-1}=R^{\mathsf T}
(max RGB + min RGB)/2 | \frac{\max(\mathrm{RGB})+\min(\mathrm{RGB})}{2}
Ltrue = 2 * Lused | L_{\mathrm{true}}=2L_{\mathrm{used}}
i = Lused ghat | i=L_{\mathrm{used}}\widehat g
i = 2 Lused gtrue | i=2L_{\mathrm{used}}g_{\mathrm{true}}
ghat = 2 gtrue | \widehat g=2g_{\mathrm{true}}
I = A * S | I=A\odot S
N+M-1 | N+M-1
Ix*Ix, Ix*Iy and Iy*Iy | I_x^2,\;I_x I_y\text{ and }I_y^2
lambda1 and lambda2 | \lambda_1\text{ and }\lambda_2
max(lambda1, lambda2) | \max(\lambda_1,\lambda_2)
lambda1 + lambda2 | \lambda_1+\lambda_2
min(lambda1, lambda2) | \min(\lambda_1,\lambda_2)
lambda1 - lambda2 | \lambda_1-\lambda_2
A>B>C | A>B>C
IoU(A,B)>threshold | \operatorname{IoU}(A,B)>\text{threshold}
IoU(B,C)>threshold | \operatorname{IoU}(B,C)>\text{threshold}
IoU(A,C)<threshold | \operatorname{IoU}(A,C)<\text{threshold}
C=-R.T@t | C=-R^{\mathsf T}t
R.T t = [-1,2,-3] | R^{\mathsf T}t=\begin{bmatrix}-1&2&-3\end{bmatrix}
C=[1,-2,3] | C=\begin{bmatrix}1&-2&3\end{bmatrix}
Distance = sqrt(1+4+9)=sqrt(14) | \text{Distance}=\sqrt{1+4+9}=\sqrt{14}
||t|| | \lVert t\rVert
target=(80+40+20)/3 | \text{target}=\frac{80+40+20}{3}
corrected = pixel/channel_means*target | \text{corrected}=\frac{\text{pixel}}{\text{channel means}}\cdot\text{target}
target = 140/3 | \text{target}=\frac{140}{3}
(30/40)*(140/3)=35 | \frac{30}{40}\cdot\frac{140}{3}=35
sum_j (w[j]*(L[j]@g-i[j]))^2 | \sum_j\bigl(w_j(L_j g-i_j)\bigr)^2
g[2] | g_2
delta=4*(.1-3*delta) | \delta=4(.1-3\delta)
delta=.4/13 | \delta=\frac{.4}{13}
g[2]=.6+.4/13=.6307692 | g_2=.6+\frac{.4}{13}=.6307692
I = Ia + kd*max(n dot l,0) + ks*max(v dot r,0)^s | I=I_a+k_d\max(n\cdot l,0)+k_s\max(v\cdot r,0)^s
Ia=0.1 | I_a=0.1
kd=0.6 | k_d=0.6
n dot l=0.5 | n\cdot l=0.5
ks=0.8 | k_s=0.8
v dot r=0.5 | v\cdot r=0.5
s=4 | s=4
Diffuse = .6*.5=.3 | \text{Diffuse}=.6\cdot.5=.3
specular = .8*(.5^4)=.05 | \text{specular}=.8(.5^4)=.05
I=.1+.3+.05=.45 | I=.1+.3+.05=.45
(70-50)/(150-50)=.2 | \frac{70-50}{150-50}=.2
Output=.2*255=51 | \text{Output}=.2\cdot255=51
count4-count8 | \text{count}_4-\text{count}_8
8-2=6 | 8-2=6
theta=degrees(atan2(Gy,Gx)) modulo 180 | \theta=\operatorname{degrees}(\operatorname{atan2}(G_y,G_x))\bmod180
Gx=[3,-3,0,2] | G_x=\begin{bmatrix}3&-3&0&2\end{bmatrix}
Gy=[4,-4,5,0] | G_y=\begin{bmatrix}4&-4&5&0\end{bmatrix}
5+5=10 | 5+5=10
F=-3-4i | F=-3-4\mathrm{i}
atan2(y,x) | \operatorname{atan2}(y,x)
-180 + atan(4/3) = -126.8699 | -180+\arctan(4/3)=-126.8699
atan(4/3) | \arctan(4/3)
A@[u,v] = -It | A\begin{bmatrix}u&v\end{bmatrix}^{\mathsf T}=-I_t
A.T(-It)=[29,10] | A^{\mathsf T}(-I_t)=\begin{bmatrix}29&10\end{bmatrix}
v=(-29+140)/83=111/83 | v=\frac{-29+140}{83}=\frac{111}{83}
[x,y,1] | [x,y,1]
A@P=targets | AP=\text{targets}
y=.5*2+3.5*3-1.25=10.25 | y=.5\cdot2+3.5\cdot3-1.25=10.25
d1/d2 < 0.75 | \frac{d_1}{d_2}<0.75
[.6,.8,.6,20/21,.25] | \begin{bmatrix}.6&.8&.6&20/21&.25\end{bmatrix}
5/3 | \frac{5}{3}
30/40=.75, 10/20=.5, 8/10=.8 | \frac{30}{40}=.75,\;\frac{10}{20}=.5,\;\frac{8}{10}=.8
Macro recall=(.75+.5+.8)/3=.6833333 | \text{Macro recall}=\frac{.75+.5+.8}{3}=.6833333
3/5>.5 | \frac{3}{5}>.5
dLoss/dW[1,1] | \frac{\partial\mathrm{Loss}}{\partial W_{1,1}}
upstream_gradient * the corresponding input value | \text{upstream gradient}\cdot\text{the corresponding input value}
W[1,1] | W_{1,1}
I[1,1]=-1 | I_{1,1}=-1
I[1,2]=4 | I_{1,2}=4
Gradient=2*(-1)+(-1)*4=-6 | \text{Gradient}=2(-1)+(-1)\cdot4=-6
9 x 9 x 8 | 9\times9\times8
8*5 | 8\cdot5
5 biases = 45 | 5\text{ biases}=45
S x S x (5*B+C) | S\times S\times(5B+C)
S=7, B=2 and C=4 | S=7,\;B=2\text{ and }C=4
2*5+4=14 | 2\cdot5+4=14
7*7=49 | 7\cdot7=49
49*14=686 | 49\cdot14=686
B*(5+C) | B(5+C)
f=1200 | f=1200
B=0.12 | B=0.12
uL=414, uR=390 | u_L=414,\;u_R=390
d=uL-uR | d=u_L-u_R
Z=f*B/d | Z=\frac{fB}{d}
d=24 | d=24
Z=1200*.12/24=6 | Z=\frac{1200\cdot.12}{24}=6
n_w = R.T @ n_c | n_w=R^{\mathsf T}n_c
n_w = R.T @ (n_c-t) | n_w=R^{\mathsf T}(n_c-t)
n_w = R @ n_c+t | n_w=Rn_c+t
n_w = K @ n_c | n_w=Kn_c
I=A*S | I=A\odot S
A'=cA and S'=S/c | A'=cA\text{ and }S'=\frac{S}{c}
z(0,0)=0 | z(0,0)=0
F[-k]=conj(F[k]) | F_{-k}=\overline{F_k}
I'=aI+b | I'=aI+b
a>0 | a>0
aI+b | aI+b
T @ H | TH
H @ T | HT
H + T | H+T
H.T @ T | H^{\mathsf T}T
source -> H -> reference -> T -> canvas | \text{source}\xrightarrow{H}\text{reference}\xrightarrow{T}\text{canvas}
prediction=0 | \text{prediction}=0
k=1 | k=1
[R,G,B,alpha*x,alpha*y] | [R,G,B,\alpha x,\alpha y]
[R,G,B] | [R,G,B]
H x W x C | H\times W\times C
H/2 x W/2 x 2C | \frac{H}{2}\times\frac{W}{2}\times2C
fx=800, fy=600, cx=320, cy=240 | f_x=800,\;f_y=600,\;c_x=320,\;c_y=240
fy'=300 | f_y'=300
cy'=(240-20)/2=110 | c_y'=\frac{240-20}{2}=110
v'=300*(1/2)+110=260 | v'=300\cdot\frac{1}{2}+110=260
1.05/4=.2625 | \frac{1.05}{4}=.2625
p(x,y)=dz/dx=y | p(x,y)=\frac{\partial z}{\partial x}=y
q(x,y)=dz/dy=2x | q(x,y)=\frac{\partial z}{\partial y}=2x
p=0 | p=0
y=0 | y=0
q=4 | q=4
x=2 | x=2
z_A=12 | z_A=12
q=0 | q=0
x=0 | x=0
p=3 | p=3
y=3 | y=3
z_B=6 | z_B=6
Difference=6 | \text{Difference}=6
dp/dy=1 | \frac{\partial p}{\partial y}=1
dq/dx=2 | \frac{\partial q}{\partial x}=2
I=rho*max(n dot l,0) | I=\rho\max(n\cdot l,0)
n=[2/3,-1/3,2/3] | n=\begin{bmatrix}2/3&-1/3&2/3\end{bmatrix}
l=[0,0.6,0.8] | l=\begin{bmatrix}0&0.6&0.8\end{bmatrix}
rho=0.75 | \rho=0.75
n dot l = (-1/3)*.6+(2/3)*.8=1/3 | n\cdot l=-\frac{1}{3}\cdot.6+\frac{2}{3}\cdot.8=\frac{1}{3}
I=.75/3=.25 | I=\frac{.75}{3}=.25
a=[0,0,10] | a=\begin{bmatrix}0&0&10\end{bmatrix}
b=[0,10,0] | b=\begin{bmatrix}0&10&0\end{bmatrix}
med(a+b)-med(a)-med(b) | \operatorname{med}(a+b)-\operatorname{med}(a)-\operatorname{med}(b)
a+b=[0,10,10] | a+b=\begin{bmatrix}0&10&10\end{bmatrix}
f=[1,0,2,0] | f=\begin{bmatrix}1&0&2&0\end{bmatrix}
h=[0,1,0,1] | h=\begin{bmatrix}0&1&0&1\end{bmatrix}
c[k]=sum(n=0..3) f[n]*h[(k-n) modulo 4] | c_k=\sum_{n=0}^{3}f_n h_{(k-n)\bmod4}
c[3] | c_3
c[3]=1*h[3]+0*h[2]+2*h[1]+0*h[0]=1+2=3 | c_3=1h_3+0h_2+2h_1+0h_0=1+2=3
>=9 | \ge9
>=4 and <9 | \ge4\text{ and }<9
Ix=[1,0,1,2] | I_x=\begin{bmatrix}1&0&1&2\end{bmatrix}
Iy=[0,2,1,0] | I_y=\begin{bmatrix}0&2&1&0\end{bmatrix}
M=[[sum(Ix^2),sum(Ix*Iy)],[sum(Ix*Iy),sum(Iy^2)]] | M=\begin{bmatrix}\sum I_x^2&\sum I_x I_y\\\sum I_x I_y&\sum I_y^2\end{bmatrix}
[[a,b],[b,d]] | \begin{bmatrix}a&b\\b&d\end{bmatrix}
lambda_min=(a+d-sqrt((a-d)^2+4*b*b))/2 | \lambda_{\min}=\frac{a+d-\sqrt{(a-d)^2+4b^2}}{2}
lambda_min=(11-sqrt(5))/2=4.381966 | \lambda_{\min}=\frac{11-\sqrt{5}}{2}=4.381966
[u,v]=[1.75,-0.5] | [u,v]=\begin{bmatrix}1.75&-0.5\end{bmatrix}
Magnitude=sqrt(14.25^2+3.25^2)=about 14.62 | \text{Magnitude}=\sqrt{14.25^2+3.25^2}\approx14.62
w=0.4 | w=0.4
N=ceil(log(1-p)/log(1-w^3)) | N=\left\lceil\frac{\log(1-p)}{\log(1-w^3)}\right\rceil
p=0.999 | p=0.999
w^3=.064 | w^3=.064
log(.001)/log(.936)=104.4417 | \frac{\log(.001)}{\log(.936)}=104.4417
H=[[a,b,c],[d,e,f],[g,h,1]] | H=\begin{bmatrix}a&b&c\\d&e&f\\g&h&1\end{bmatrix}
x'=(a*x+b*y+c)/(g*x+h*y+1), y'=(d*x+e*y+f)/(g*x+h*y+1) | x'=\frac{ax+by+c}{gx+hy+1},\quad y'=\frac{dx+ey+f}{gx+hy+1}
c=1,f=2 | c=1,\;f=2
a=3g+2,d=2g,b=h,e=4h+2 | a=3g+2,\;d=2g,\;b=h,\;e=4h+2
h=0,g=1 | h=0,\;g=1
x'=3.5/1.5=7/3 | x'=\frac{3.5}{1.5}=\frac{7}{3}
[D1,D2] | [D_1,D_2]
sqrt(D1)/sqrt(D2)<0.7 | \frac{\sqrt{D_1}}{\sqrt{D_2}}<0.7
D1/D2 | \frac{D_1}{D_2}
[2/3,3/4,1/2,5/6,1/2] | \begin{bmatrix}2/3&3/4&1/2&5/6&1/2\end{bmatrix}
3/6=.5 | \frac{3}{6}=.5
score>=0.6 | \text{score}\ge0.6
TP=2, FP=2, FN=1 | \mathrm{TP}=2,\;\mathrm{FP}=2,\;\mathrm{FN}=1
F1=4/(4+2+1)=4/7=.5714286 | F_1=\frac{4}{4+2+1}=\frac{4}{7}=.5714286
[0,1/2,1/3,2/4,3/5] | \begin{bmatrix}0&1/2&1/3&2/4&3/5\end{bmatrix}
[0,1/4,1/4,2/4,3/4] | \begin{bmatrix}0&1/4&1/4&2/4&3/4\end{bmatrix}
.25*.6 | .25\cdot.6
AP=.45 | \mathrm{AP}=.45
1 x 1 | 1\times1
64->16 | 64\to16
16->16 | 16\to16
16->64 | 16\to64
(64+1)*16=1040 | (64+1)\cdot16=1040
(3*3*16+1)*16=2320 | (3\cdot3\cdot16+1)\cdot16=2320
(16+1)*64=1088 | (16+1)\cdot64=1088
Total=4448 | \text{Total}=4448
3 x 3 x 3 | 3\times3\times3
3*3*3*2=54 | 3\cdot3\cdot3\cdot2=54
(54+1)*5=275 | (54+1)\cdot5=275
box_confidence=Pr(object)*IoU(predicted_box,GT) | \text{box confidence}=\Pr(\text{object})\cdot\operatorname{IoU}(\text{predicted box},\mathrm{GT})
class_specific_score=Pr(class|object)*box_confidence | \text{class-specific score}=\Pr(\text{class}\mid\text{object})\cdot\text{box confidence}
Pr(object)=0.75 | \Pr(\text{object})=0.75
IoU=0.6 | \mathrm{IoU}=0.6
Pr(class|object)=0.8 | \Pr(\text{class}\mid\text{object})=0.8
Box confidence=.75*.6=.45 | \text{Box confidence}=.75\cdot.6=.45
Class-specific score=.8*.45=.36 | \text{Class-specific score}=.8\cdot.45=.36
f=900 | f=900
B=0.2 | B=0.2
d=12 | d=12
delta_d=0.25 | \delta_d=0.25
|delta_Z| approximately (f*B/d^2)*|delta_d| | \lvert\delta_Z\rvert\approx\frac{fB}{d^2}\lvert\delta_d\rvert
180/144=1.25 | \frac{180}{144}=1.25
fx | f_x
fy | f_y
cx | c_x
cy | c_y
Xc | X_c
Xw | X_w
n_c | n_c
n_w | n_w
R1 | R_1
R2 | R_2
Ix | I_x
Iy | I_y
It | I_t
Ixx | I_{xx}
Iyy | I_{yy}
Ixy | I_{xy}
sigma | \sigma
alpha | \alpha
delta | \delta
"""

# The delimiter has spaces on both sides so probability/absolute-value bars
# remain part of the source. Split from the right for those two source spans.
MATH = dict(line.rsplit(" | ", 1) for line in NOTATION.strip().splitlines())
assert len(MATH) == len(NOTATION.strip().splitlines()), "Duplicate math span"
# Coordinate vectors in column-vector equations are printed compactly as
# transposed rows. Histograms, data rows and matrices keep their stated shape.
for source in (
    "g = [0,0,0]", "C = [1,2,0]", "Xw = [3,5,4]", "Xw-C = [2,3,4]",
    "Xc = [-3,2,4]", "L.T i = [0.384,0.064,1.66]", "g = [0.3,0.05,1.66/2.44]",
    "n proportional to [-p,-q,1]", "A.T(-It) = [13,0]", "l2=[0,-1,7]",
    "R.T t = [-1,2,-3]", "C=[1,-2,3]", "A.T(-It)=[29,10]",
    "n=[2/3,-1/3,2/3]", "l=[0,0.6,0.8]",
):
    MATH[source] += r"^{\mathsf T}"
PATTERN = re.compile("|".join(
    (r"(?<!\w)" if source[0].isalnum() else "") + re.escape(source)
    + (r"(?!\w)" if source[-1].isalnum() else "")
    for source in sorted(MATH, key=len, reverse=True)
))
ARRAY = re.compile(r"\[(?:\s*\[[^\[\]\n]+\]\s*,?)+\s*\]|\[[^\[\]\n]+\]")
NUMBER = re.compile(r"-?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?")


def numeric_array(source):
    try:
        values = ast.literal_eval(source)
    except (ValueError, SyntaxError):
        return None
    if not isinstance(values, list) or not values:
        return None
    rows = values if isinstance(values[0], list) else [values]
    if not all(isinstance(row, list) and len(row) == len(rows[0])
               and all(type(v) in (int, float) for v in row) for row in rows):
        return None
    return r"\begin{bmatrix}" + r"\\".join(
        "&".join(str(v) for v in row) for row in rows
    ) + r"\end{bmatrix}"


def chunks(text):
    """Yield (source, latex-or-None), with no discarded source characters."""
    position = 0
    # Select explicit notation first; arrays are recognized only in plain gaps.
    for match in PATTERN.finditer(text):
        yield from array_chunks(text[position:match.start()])
        yield match.group(), MATH[match.group()]
        position = match.end()
    yield from array_chunks(text[position:])


def array_chunks(text):
    position = 0
    for match in ARRAY.finditer(text):
        latex = numeric_array(match.group())
        if latex is not None:
            prefix = text[position:match.start()]
            assignment = re.search(r"\b([A-Za-z](?:[0-9]|[a-z])?)\s*=\s*$", prefix)
            if assignment:
                name = assignment[1]
                symbol = name[0] + "_{" + name[1:] + "}" if len(name) > 1 else name
                if name in ("x1", "x2", "t") and r"\\" not in latex:
                    latex += r"^{\mathsf T}"
                yield prefix[:assignment.start()], None
                yield prefix[assignment.start():] + match.group(), symbol + "=" + latex
            else:
                yield prefix, None
                yield match.group(), latex
            position = match.end()
    yield text[position:], None


def text_grid(code):
    """Render authored data tables as math; return None for non-data fences."""
    if (matrix := numeric_array(code.strip())) is not None:
        return matrix
    rows = code.strip().splitlines()
    named = []
    for row in rows:
        match = re.fullmatch(r"([IK])\s*=\s*(.*)", row)
        if match is None or (matrix := numeric_array(match[2])) is None:
            break
        named.append(match[1] + "&=" + matrix)
    else:
        return r"\begin{aligned}" + r"\\[6pt]".join(named) + r"\end{aligned}"
    split = [row.split() for row in rows]
    if all(all(NUMBER.fullmatch(v) for v in row) for row in split):
        if len({len(row) for row in split}) == 1:
            return r"\begin{bmatrix}" + r"\\".join("&".join(row) for row in split) + r"\end{bmatrix}"
    if split[0] == list("ABCD") and [row[0] for row in split[1:]] == list("ABCD"):
        def fraction(value):
            return r"\frac{" + value.replace("/", "}{") + "}" if "/" in value else value
        return (r"\begin{array}{c|rrrr}&A&B&C&D\\\hline "
                + r"\\[6pt]".join("&".join(fraction(v) for v in row) for row in split[1:]) + r"\end{array}")
    if all(re.fullmatch(r"\(\d,\d\) -> \(\d,\d\)", row) for row in rows):
        return r"\begin{aligned}" + r"\\".join(row.replace(" -> ", r"&\mapsto ") for row in rows) + r"\end{aligned}"
    return None


def numeric_atoms(text):
    """Numeric-content audit, independent of math layout and leading zeros."""
    return Counter(abs(Decimal(m.group())) for m in NUMBER.finditer(text))
