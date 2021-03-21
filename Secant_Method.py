import math

def f(x):
    return math.exp(pow(math.sin(x), 3)) + pow(x, 6) - 2*pow(x, 4) - pow(x, 3) - 1

def temnousa(x0, x1):
    loops=0
    xn=x0
    xnn = x1
    xnnn = xnn - (f(xnn)*(xnn-xn) / (f(xnn) - f(xn)))
    while abs(xnn-xn)>0.00005:
        loops +=1
        xn = xnn
        xnn = xnnn
        xnnn = xnn - ((f(xnn)*(xnn-xn)) / (f(xnn) - f(xn)))
    print(loops)
    print(xnnn)

temnousa(-1.3, -1.25)
temnousa(1.6, 1.7)
temnousa(0.5, 1.25)



