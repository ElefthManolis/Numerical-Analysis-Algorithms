import numpy as np
    
def gauss_seidel(a, x ,b):       
    n = len(a)
    x_out = np.zeros(len(x), dtype='f')                    
    for j in range(0, n):         
        
        d = b[j]                   
        for i in range(0, n):      
            if(j != i): 
                d-=a[j][i] * x[i] 
                
        x_out[j] = d / a[j][j]             
    return x_out

n = 10
A = np.zeros((n,n))
for i in range(0, n):
    for j in range(0, n):
        if i==j:
            A[i][j]=5
        if i+1==j or i==j+1:
            A[i][j]=-2
        


b = np.ones(n)
b[0]=3
b[n-1]=3
x = np.zeros(n, dtype='f')

while max(np.absolute(np.subtract(x, gauss_seidel(A,x,b))))>0.00005:
    x = gauss_seidel(A,x,b)
print(x)