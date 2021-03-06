import math
import numpy as np

 
def cholesky(A):
    n = len(A)
    lower = np.zeros((n,n))
 
    # Decomposing a matrix
    # into Lower Triangular
    for i in range(n): 
        for j in range(i + 1): 
            sum1 = 0
 
            # sum1mation for diagnols
            if (j == i): 
                for k in range(j):
                    sum1 += pow(lower[j][k], 2)
                lower[j][j] = float(math.sqrt(A[j][j] - sum1))
            else:
                 
                # Evaluating L(i, j)
                # using L(j, j)
                for k in range(j):
                    sum1 += (lower[i][k] *lower[j][k])
                if(lower[j][j] > 0):
                    lower[i][j] = int((A[i][j] - sum1) /
                                               lower[j][j])
 
    return lower
    
 


A = np.array([[4, 12, -16],
            [12, 37, -43],
            [-16, -43, 98]], dtype='f')

b = np.array([0, 6, 39], dtype='f')
L = cholesky(A)
print(L)



