import math
import numpy as np
import matplotlib.pyplot as plt


def f(x,a,b,c, d):
    return a*pow(x, 3)+b*pow(x, 2)+c*x+d 

x = np.array([-math.pi, -1, -0.5, -0.2, 0, 0.1, 0.35, 0.8, 1.1, math.pi])
y = np.zeros(10)
for i in range(0, 10):
    y[i] = math.sin(x[i])





A = np.zeros((10, 4))
for i in range(0, 10):
    for j in range(0, 4):
        if j==0:
            A[i][j] = pow(x[i], 3)
        if j==1:
            A[i][j] = pow(x[i], 2)
        if j==2:
            A[i][j] = x[i]
        if j==3:
            A[i][j] = 1



A_new = np.dot(A.T, A)
y_new = np.dot(A.T, y)
solution = np.linalg.solve(A_new, y_new)

a = solution[0]
b = solution[1]
c = solution[2]
d = solution[3]


z = np.linspace(-math.pi, math.pi,200)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(z, np.sin(z)-f(z,a,b,c,d), 'r')
print(a)
print(b)
print(c)
print(d)
print(math.sin(math.pi/3))
print(f(math.pi/3,a,b,c,d))
plt.show()

