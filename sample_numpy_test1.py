# Numpy is most useful feature is n-dimensional array object
import numpy as np 
import time
a = np.array([1,2,3])
print(a)
print(type(a))
#print(ndim(a))
print(a.itemsize)
print(a.size)
a1 = np.arange(1000)
print(a1.size)
l1 = np.arange(1000)
l2 = np.arange(1000)

print('numpy .....')
start = time.time()
result = l1 + l2
#print(result)
print((time.time() - start)*1000)

####################################################
# Basic Array operations ##########################
###################################################
import numpy as np 
b1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('Basic Array operations...........')
print(b1)
print(b1.size)
print(b1.ndim)
print(b1.itemsize) ## byte size of each element
print(type(b1)) # data type of array
print(b1.dtype) ## data type of element
b2 = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype = np.float64)
print(type(b2))
print(b2.itemsize); print(b2); print(b2.shape)

####################################
# create zeros array
#################################
b3 = np.zeros((3,2),dtype = np.int32)
print(b3)
b4 = np.ones((3,3)); print(b4)
b5 = np.arange(1,5)
print(b5)
b6 = np.arange(1,5,2); print(b6)
b7 = np.linspace(1,5,10); print(b7)
l1 = np.array([[1,2],[3,4],[5,6]])
print(l1.size)
print(l1.shape)
print(l1.reshape(2,3))
print(l1.reshape(2,3))
print(l1.ravel()) # to flatten the array
##########################################
##### Mathematical Functions
##########################################
print(l1.min())
print(l1.max())
print(l1.mean())
print(l1.sum())
print(l1.sum(axis=0))
print(l1.sum(axis=1))
print(np.sqrt(l1))
print(np.std(l1))

###########################
# Product of two matrices
###########################
l1 = np.array([[1,2],[3,4]])
l2 = np.array([[1,2],[3,4]])
print('******** Product of two matrices *********')
print(l1.dot(l2))

#########################################################
# Indexing and slicing
#########################################################

n1 = np.array([1,2,3,4,5,6])
print(n1[0:3])
print(n1[-2:])

n2 = np.array([[1,2,3],[4,5,7],[8,9,1]])
print(n2[1:2,0])
print(n2[1,2])
print(n2[0,0])
print(n2[-2])
print(n2[:,1:3])
#######################################################
# Iterating through Array
#######################################################
n3 = np.array([[1,2,3],[4,5,7],[8,9,1]])
print(n3)
for row in n3:
    print(row)

for cell in n3.flat:
    print(cell,end = ' ')


#######################################################
# Stacking together two arrays
#######################################################
n4 = np.arange(6).reshape(3,2)
n5 = np.arange(6,12).reshape(3,2)
print(n4)
print(n5)
n7 = np.vstack((n4,n5))
print(n7)
print(np.hstack((n4,n5)))

# Splitting array
n8 = np.arange(30).reshape(2,15)
print(n8)

result = np.hsplit(n8,5)
print(result[0])

############################################################
# Indexing with Boolean array
############################################################
p = np.arange(12).reshape(3,4)
print(p)