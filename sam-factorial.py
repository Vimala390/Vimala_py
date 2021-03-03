x = int(input('enter val:'))
fact = 1
if x < 0:
    print('Number must be positive')
elif x ==0:
    print('factorial for 0 is 1')
else:
    for i in range(1,x+1):
        fact=fact*i
    print(fact)
