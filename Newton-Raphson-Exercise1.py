import math

def f(x):
    return math.exp(pow(math.sin(x), 3)) + pow(x, 6) - 2*pow(x, 4) - pow(x, 3) - 1



def f_derivative(x):
    return 3*math.exp(pow(math.sin(x), 3))*pow(math.sin(x), 2)*math.cos(x) + 6*pow(x,5)-8*pow(x,3)-3*pow(x,2)



def Newton_Raphson(x):
    loops=0
    xn=x
    xnn = xn-(f(xn)/f_derivative(xn))
    while abs(xnn-xn)>0.000005:
        loops +=1
        xn = xnn
        xnn = xn-(f(xn)/f_derivative(xn))

    print(xnn)
    print(loops)
        


Newton_Raphson(-1.5)
Newton_Raphson(-0.05)
Newton_Raphson(1.75)