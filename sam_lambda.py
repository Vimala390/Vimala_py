x = lambda a:a*a
print(x(2))

def anew(x):
    return(lambda y:x+y)
p = anew(4)
print(p(8))
## filter () ..

a = [1,2,3,4,6,8,10]
a_new = list(filter(lambda a:(a%2==0),a))
print(a_new)

## map()

b = [2,3,4,5,6,7,8,9]
b_new = list(map(lambda b:(b%3==0),b))
print(b_new)
##Reduce(function,sequence)
from functools import reduce
c_new = reduce(lambda a,b:a+b,[1,2,3,4,5])
print(c_new)

d = lambda a,b:(a**2+2*a*b+b**2)
print(d(2,3))

# Higher order function
h_sam = lambda x,a_new:x+a_new(x)

print(h_sam(2,lambda x:x*2))

from functools import reduce
print((lambda *args:sum(args))(1,2,3,4))
lst = [2,3,4,5]
x = map(lambda x:x+1,filter(lambda x:x>=3,lst))
print(list(x))
y = reduce(lambda x:x+x,filter(lambda x:(x>=3),lst))
print(y)