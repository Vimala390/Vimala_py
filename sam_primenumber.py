#  2 3 5 7 ...
n = int(input('enter number :'))

for i in range(2,n+1):
    x = True
    for j in range(2,i):
        if i%j == 0:
            x = False 
         
    if x:
        print(i,end=" ")



        