print('Welcome to the bank...')
l_balance=60.23
l_chance=1
while l_chance <=3:
    x_pin=int(input('Enter ATM pin:'))
    if x_pin=='1234':
        print('1.enter 1 for Balance enquiry')
        print('2.enter 2 for cash withdrawl')
        print('3.enter 3 for deposit')
        print('4.enter 4 for statement')
        y_input=int(input('please enter your responce'))
        if y_input==1:
            print('your balance is ..')
            print(l_balance)
        elif y_input==2