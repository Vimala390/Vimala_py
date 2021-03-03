l_travel = input('are you travelling ..Y/N')
while l_travel=='Y':
    l_num = int(input('no.of people to travel..'))
    for i in range(1,l_num+1):
        l_name = input('enter name  ')
        l_age = int(input('enter age.. '))
        l_sex = input('enter male/female')
        print(l_name,end=" ")
        print(l_age,end=" ")
        print(l_sex,end=" ")
        print('\n')
    l_travel=input('did you miss anyone ..Y/N..')
