# First Class Function

# A programming language has first class functions if it treats function as
# entity which supports all the operations generally available to all other
# entities

######################################################
# def square(x):
#     return x*x

# f = square(5)
# print(square)
# print(f)


######################################################
# def square(x):
#     return x*x

# def cube(x):
#     return x*x*x

# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result

# squares = my_map(square, [1,2,3,4,5])
# cubes   = my_map(cube, [1,2,3,4,5])
# print(squares)
# print(cubes)

###################################################### 
''' return a function from another function  '''

def logger(msg):
    def log_message():
        print("Log:", msg)
    return log_message

log_hi  = logger('Hi!')
log_hi()



