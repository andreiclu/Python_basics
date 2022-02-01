import math
import unittest


def eqtwo(a,b,c):
    delta = b*b - 4*a*c
    if delta<0:
        print ("No solutions for this eq")
    elif delta==0:
        x1= x2 = -b /( 2 * a)
        return x1,x2
    elif delta>0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        return x1,x2

print(eqtwo(2,3,1))

