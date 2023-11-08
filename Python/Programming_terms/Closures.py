# Closures

''' A function return a function with execution '''

# def outer_func():
#     message = 'Hi'    

#     def inner_func():
#         print(message)  # free variable inside inner func

#     return inner_func() # return function with execution
    
# outer_func()

############################################################
''' A function return a function like an object '''

# def outer_func():
#     message = 'Hi'    

#     def inner_func():
#         print(message)   # free variable inside inner func

#     return inner_func    # return function without execution
    
# my_func = outer_func()
# my_func()                # this will execute this function
# print(my_func.__name__)  # print the name of the function where its defined

############################################################

'''
In simple terms.
A Closure is a inner function that remembers and has access to variables
and local scopes in which it was created.
'''

############################################################
''' Add parameters to a function '''

# def outer_func(msg):
#     message = msg
#     def inner_func():
#         print(message)
#     return inner_func

# hi_func     = outer_func('Hi')
# hello_func  = outer_func('Hello')

# hi_func()
# hello_func()

############################################################
''' Example '''

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def log_func(*args): # *args means any number of arguments
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

add_logger    = logger(add)
sub_logger    = logger(sub)

add_logger(3,3)
add_logger(4,5)

sub_logger(10,5)
sub_logger(20,10)

# what closure allowed here is that we created a log file "example.log"
# which logged which function are we running and what argument you are using.
