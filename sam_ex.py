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