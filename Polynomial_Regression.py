import numpy as np
import math
import matplotlib.pyplot as plt


#Για την πολυωνυμική προσέγγιση χρησιμοποίησα την μέθοδο του Lagrange
def lagrange(p):
    n = len(p)
    def P(x):
        final = 0
        L = 1
        for j in range(0, n):
            def L(j, n):
                tot_mul = 1
                for i in range(0, n):
                    if i == j:
                        continue
                    tot_mul *= (x - p[i][0]) / float(p[j][0] - p[i][0])
                return tot_mul
            final += p[j][1]*L(j, n)
        return final
    return P


x = np.array([-math.pi, -1, -0.5, -0.2, 0, 0.1, 0.35, 0.8, 1.1, math.pi])

p = np.zeros((10, 2))
for i in range(0, 10):
    p[i][0] = x[i]
    p[i][1] = math.sin(x[i])

a = np.linspace(-math.pi, math.pi,200)
p_final = lagrange(p)
print(p_final(math.pi/3))
print(math.sin(math.pi/3))



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(a, np.sin(a)-p_final(a), 'r')
plt.show()



