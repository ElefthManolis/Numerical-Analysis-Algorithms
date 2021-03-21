import math
import random

def f(x):
    return 94*pow(math.cos(x), 3)-24*math.cos(x)+177*pow(math.sin(x), 2)-108*pow(math.sin(x), 4)-72*pow(math.cos(x), 3)*pow(math.sin(x), 2)-65

def bisection(a, b):
    loops = 0
    found = False
    if a>b:  #εδώ εναλλάσω τις τιμες των μεταβλητών a και b ώστε η μεταβλητή b να έχει μεγαλύτερη τιμή από την a
        temp = b
        b = a
        a = temp
    c = random.uniform(a,b)
    while abs(b-a)>0.000005 and not found:
        loops += 1
        if f(c)==0:
            found = True
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
        c = random.uniform(a,b)
    print(loops)
    print(c)
a1 = 2
b1 = 2.5

a2 = 1
b2 = 1.5

a3 = 0.5
b3 = 1

bisection(a1,b1)
bisection(a2,b2)
bisection(a3,b3)