def func1(name):
    return f"Hello {name}"

def func2(name):
    return 'How are you doing ..'

def func3(func4):
    return func4('Dear ..')

print(func3(func1))
print(func3(func2))

##inner functions..
def func(n):
    def func1():
        return 'Welcome'
    
    def func2():
        return 'Python'
    if n == 1:
        return func1()
    else:
        return func2()
    
a = func(1)
b = func(2)

print(a)
print(b)

#########################
def function1(function):
    def wrapper():
        print('Hello..')
        function()
        print('Welcome to Python ..')
    return wrapper
def function2():
    print('Vimala')

function3 = function1(function2)
function3()
##print(func3)

def function1(function):
    def sam():
        print('Hello..')
        function()
        print('Welcome to Python ..')
    return sam
@function1
def function2():
    print('Vimala')

function2()

#############
def sam_func(function):
    def inner_func():
        x=function()
        x+=2        
        return x
    return inner_func
@sam_func
def function1():
    x = int(input('enter number'))
    return x

#function1 = sam_func(function1)
print(function1())



