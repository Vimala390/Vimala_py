#Write a program to modify or replace an existing element of a tuple with a new element.
#Example: 
#num= (10,20,30,40,50) and insert 90.
#Expected output: (10,20,90,40,50)
lst = [10,20,30,40,50]
lst[2] = 90
print(lst)
lst1 = tuple(lst)
print(lst1)
print(type(lst1))

