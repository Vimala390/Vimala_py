#three integers satisfying a2+b2=c2
from math import *
n = 5
for a in range(1,n+1):
    for b in range(a,n):
        c_2 = a**2 + b**2
        c=int(sqrt(c_2))
        if (c_2 - c**2)==0:
            print(a,b,c)