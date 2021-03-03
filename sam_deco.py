def function1(function):
    def wrapper(*args,**kwargs):
        print('Hello')
        function(*args,**kwargs)
        print('Welcome to Python')
    return wrapper
@function1
def function2(name):
    return(f"{name}")    

function2("Vimala")





    