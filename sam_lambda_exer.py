# Program to create a lambda function that returns a square value of a given number.
x = lambda a:a**2
print(x(int(input('Enter number: '))))

#Write a program to filter out even numbers from a list by using filter()
a_list = [1,2,3,4,5,6,7,8,9,10]
a_new = list(filter(lambda p:(p%2==0),a_list))
print(a_new)

#Write a program to find the squares of element in a list by using map() function.
b_list = [1,2,3,4,5,6,7,8,9,10]
b_new = list(map(lambda a:(a**2),b_list))
print(b_new)

#Write a reduce function on list.  Example: lst=[1,2,3,4,5]
from functools import reduce
lst=[1,2,3,4,5]
c_new = reduce(lambda a,b:(a+b),lst)
print(c_new)

#Write a decorator to increase the value of function by 2.
def sam_func(function):
    def inner_func():
        x=function()
        x+=2        
        return x
    return inner_func
@sam_func
def function1():
    x = int(input('enter number'))
    return x

#function1 = sam_func(function1)
print(function1())

#Write a program to create a generator that returns 
# a sequence of numbers from x to y.
def sam_gen(x,y):
    for i in range(x,y+1):
        print(i,end = " ")

sam_gen(int(input('Enter Number')),int(input('Enter Number')))