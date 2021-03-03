x = int(input('enter val:'))
i = 10
while i in range(10,20):
    if i == x:
        print('correct ...')
        break
    else:
        if i > x:
            #continue
            print('val is greater')
        elif i < x:
            #continue
            print('val is less')
        else:
            print('none')
    i+=1