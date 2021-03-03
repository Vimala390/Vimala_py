def prime_num(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

x = int(input('enter number : '))
if prime_num(x):
    print('given number is prime ..')
else:
    print('given number is NOT Prime ..')
