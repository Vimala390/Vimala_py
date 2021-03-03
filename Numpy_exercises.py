# Numpy version and configuration
import numpy as np 
print(np.__version__)
print(np.show_config())

# Create a null vector of size 10
a = np.zeros(10).reshape(2,5)
print(a)

# How to get the documentation of the numpy add function from the command line?
print(np.info(np.add))

# Create a null vector of size 10 but the fifth value which is 1.
b = np.zeros(10).reshape(2,5)
b[1,0] = 1
print(b)
print(np.ndim(b))

c = np.arange(10,50).reshape(5,8)
print(c)
#Reverse a vector (first element becomes last)
d = np.arange(10).reshape(2,5)
print(d[::-1])
 # 
e = np.arange(0,9).reshape(3,3)
print(e)
# Find indices of nonzero elements from [1,2,0,0,4,0]
a1 = np.array([1,2,0,0,4,0])
print(a1.nonzero())
# Create a 3x3 identity matrix 
a2 = np.eye(3)
print(a2)
# Create a 3x3x3 array with random values
a3 = np.arange(0,27).reshape(3,3,3)
print(a3)
a4 = np.random.random((3,3,3))
print(a4)
# Create a 2d array with 1 on the border and 0 inside
a5 = np.ones(10).reshape(2,5)
print(a5)
##
a7 = np.empty(3)
print(a7)
print(np.nan+0)
print(np.inf)
if np.nan == np.nan:
    print('True')
else:
    print('false')
