#Write a program to create an array by taking the input values and also search for position of an element in it.
#Note:  Program should start like "How many elements?"
#Use numpy to perform mathematical operations on a single dimension array.
#Example: Add, subtraction, multiplication, divide etc
from numpy import *
array1 = array(input('Enter array val1'))
array2 = array(input('Enter array val2'))
#print(x)
print(type(array1))
print(type(array2))
array1= array([1,2,3,4,5])
array2 = array([2,3,4,5,6])
array3 = array1+array2
array4 = array2 - array1
array5 = array1 * array2
array6 = array2/array1
print(array3)
print(array4)
print(array5)
print(array6)


