from math import *


def Sin1(x, e):
    sin_x = 0
    n=10


    while abs(((-1)**n)*((x**(2*n+1))/factorial(2*n+1))) < e:
        sin_x += ((-1)**n)*((x**(2*n+1))/factorial(2*n+1))
        if n>0:
            n -=1
        else:
            break
    print(sin_x)


x = 0.7

Sin1(x , 1)
print(sin(x))