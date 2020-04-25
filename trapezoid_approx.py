from math import *
import sys

def trapeziod_approx(f,a,b,n):
    h=(b-a)/float(n)
    s=(f(a)+f(b))/2
    for i in range(1,n):
        s=s+f(a+i*h)
    return s*h

f_formula = sys.argv[1]
a = eval(sys.argv[2])
b = eval(sys.argv[3])

if len(sys.argv)>4:
    n = int(sys.argv[4])
else:
    n=10

code = """
def g(x):
    return %s""" % f_formula
exec(code)

I = trapeziod_approx(g,a,b,n)
print(I)

    

