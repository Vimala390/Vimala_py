# 0 1 1 2 3 5 8 ....

n = int(input('Enter number :'))
a=0
b=1

if n > 0:
    print(a,end = " ")
    print(b,end = " ")
    for i in range(1,n):
        c = a+b
        a=b;b=c 
        print(c,end = " ") 
else:
    print('Number should be greater than zero')
    

    