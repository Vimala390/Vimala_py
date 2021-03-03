from numpy import *
n = int(input('Enter no. of elements :'))
array1 = array([])
for i in range(n):
    print(i)
    x = int(input('Enter array element ..: '))
    #array1.append(x)
    array1[i] = x

print(array1)