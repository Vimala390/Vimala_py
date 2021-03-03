
#1) Write a program to sort the list elements using bubble sort technique.
from operator import *
lst = [90,21,10,13,23,12,25,31,1,2,89]
#lst_n = []
n = len(lst)
print(lst)
for i in range(n):
    #print(i)
   # print(n-i)
    for j in range(0,n-i-1):
        
        if gt(lst[j],lst[j+1]):
            lst[j],lst[j+1] = lst[j+1],lst[j]
            #lst_n.append(lst[j]) 
           # print(lst_n)
        else:
            #lst_n.append(j) 
            continue
print(lst)

#2) Python program to add two matrices and display the sum matrix using the lists.
x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[1,2,3],[4,5,6],[7,8,9]]
z = [[0,0,0],[0,0,0],[0,0,0]]
print(x)
print(y)
print(len(x[0]))
print(x[0])
for i in range(len(x)):
    for j in range(len(x[i])):
        z[i][j] = x[i][j]+y[i][j]
    
print(type(z))
#print(z)
for i in z:
    print(i)