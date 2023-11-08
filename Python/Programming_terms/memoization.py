# Memoization

# Memoization is an optimization technique user primarily to speed up computer
# programs by storing the results of expensive function call and returning the 
# cached result when the same inputs occur again.

#################################################
'''Problem'''
# import time

# def expensive_func(num):
#     print("computing {}...".format(num))
#     time.sleep(1)
#     return num*num

# result = expensive_func(4)
# print(result)

# result = expensive_func(10)
# print(result)

# result = expensive_func(4) # already ran. would be useful if we had saved the values.
# print(result)

# result = expensive_func(10)
# print(result)

# Time to run = 4 sec

#################################################
'''Solution'''

import time

ef_cache = {}

def expensive_func(num):
    if num in ef_cache:
        return ef_cache[num]
    print("computing {}...".format(num))
    time.sleep(1)
    result = num*num
    ef_cache[num] = result
    return result

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)

result = expensive_func(4) 
print(result)

result = expensive_func(10)
print(result)

# Time to run = 2 sec


#################################################
'''Solution'''

 
