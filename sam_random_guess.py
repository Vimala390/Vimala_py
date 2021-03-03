import random as r
n=20
tg = int(n*r.random())+1
print(tg)
g=0
while g!=tg:
    g = int(input('enter val: '))
    if g>0:
        if g>tg:
            print('too large')
        elif g<tg:
            print('too small')
    else:
        print('sorry you are giving up !!')
        break
else:
    print('congratulations .. you find it')


import random as rn
print('Random number is :', rn.randint(0,9))
print('Number is :',rn.randrange(1,10,1))
# Use the random.choice function to randomly select an item 
# from a List or any sequence
lst = [1,2,3,'four','five',6,7,8]
print('random from list',rn.choice(lst))
print('random selection',rn.sample(lst,3)) # to print 3 values from list

