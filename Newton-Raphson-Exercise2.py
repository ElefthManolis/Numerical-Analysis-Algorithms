import math

def f(x):
    return 94*pow(math.cos(x), 3)-24*math.cos(x)+177*pow(math.sin(x), 2)-108*pow(math.sin(x), 4)-72*pow(math.cos(x), 3)*pow(math.sin(x), 2)-65
    

def f_derivative(x):
    return -282*pow(math.cos(x),2)*math.sin(x) + 24*math.sin(x)+354*math.sin(x)*math.cos(x)-432*pow(math.sin(x),3)*math.cos(x)+216*pow(math.cos(x),2)*pow(math.sin(x),3)-144*pow(math.cos(x), 4)*math.sin(x)

def derivative2(x):
    return -432*math.cos(x)*pow(math.sin(x),4)+432*pow(math.sin(x),4)+1224*pow(math.cos(x),3)*pow(math.sin(x),2)-1296*pow(math.cos(x),2)*pow(math.sin(x),2)+564*math.cos(x)*pow(math.sin(x),2)-354*pow(math.sin(x),2)-144*pow(math.cos(x),5)-282*pow(math.cos(x),3)+354*pow(math.cos(x),2)+24*math.cos(x)


def Newton_Raphson(x):
    loops=0
    xn = x
    xnn = xn - (f(xn)/f_derivative(xn))-1/2*(pow(f(xn),2) * derivative2(xn) / pow(f_derivative(xn),3))
    while abs(xnn-xn)>0.000005:
        loops+=1
        xn=xnn
        xnn = xn - (f(xn)/f_derivative(xn))-((pow(f(xn),2) * derivative2(xn)) / (2*pow(f_derivative(xn),3)))

    print(xnn)
    print(loops)

Newton_Raphson(2.25)
Newton_Raphson(1.03)
Newton_Raphson(0.83)