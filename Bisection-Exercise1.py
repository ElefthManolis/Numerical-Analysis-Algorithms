import math

def f(x):
    return math.exp(pow(math.sin(x), 3)) + pow(x, 6) - 2*pow(x, 4) - pow(x, 3) - 1

def bisection(a, b):
    loops = 0
    found = False
    if a>b:  #εδώ εναλλάσω τις τιμες των μεταβλητών a και b ώστε η μεταβλητή b να έχει μεγαλύτερη τιμή από την a
        temp = b
        b = a
        a = temp
    
    while abs(b-a)>0.00001 and not found:
        loops += 1
        c = (a+b)/2
        if f(c)==0:
            print(c)
            found = True
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
    print(loops)
    print(c)
    


a1 = -1.5
b1 = -1

a2 = 1.5
b2 = 1.7

a3=-0.2
b3 = 0.2

bisection(a1, b1)
bisection(a2, b2)
bisection(a3,b3)