import numpy as np


def P_matrix(A, i):
    P = np.identity(len(A), dtype='f')
    max = abs(A[i][i])
    index = i
    for k in range(i, len(A)):
        if abs(A[k][i]) > max:
            max = abs(A[k][i])
            index = k
    P[[i, index]] = P[[index, i]]
    return P


def LU(A):
    P = np.identity(len(A), dtype='f')
    n = len(A)
    L = np.identity(n, dtype='f')
    for j in range(0, n-1):
        P = np.matmul(P_matrix(A, j), P)
        A = np.dot(P_matrix(A, j), A)

        for i in range(j+1, n):
            l = A[i][j]
            m = A[j][j]
            for k in range(j, n):
                A[i][k] = A[i][k] - (l/m)*A[j][k]
            L[i][j] = l/m
    return P, A, L


A = np.array([[2.0, 1.0, 5.0], [1.0, 2.0, 2.0], [4.0, 2.0, 8.0]], dtype='f')
b = np.array([9, 7, 16])

P, U, L = LU(A)
print(P)
print(L)
print(U)

b = np.dot(P, b)

y = np.zeros(len(L), dtype='f')
for i in range(0, len(L)):
    y[i] = b[i]/float(L[i][i])
    for k in range(0, i):
        y[i] -= y[k]*L[i][k]


x = np.ones(len(U), dtype='f')
for i in range(len(U)-1, -1, -1):
    x[i]=y[i]
    for j in range(len(U)-1, -1, -1):
            if i!=j:
                x[i] -= x[j]*U[i][j]

    x[i] = x[i] / U[i][i]

print(x)
