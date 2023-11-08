# Mutable/Immutable

# An immutable object is an object whose state cannot be modified after
# it is created. This is in contrast to a mutable object which can be 
# modified after it is created.

#############################################
'''immutable examples'''

# # strings are immutable
# a = 'corey'
# print(a)
# print("address of a: {}".format(id(a)))

# a = 'john' # immutable doesn't mean we cannot reassign it.
# print(a)
# print("address of a: {}".format(id(a)))

# a = 'corey'
# a[0] = "J" # This will give an error


#############################################
''' mutable objects '''

# # a list is mutable
# a = [1,2,3,4,5,6]
# print(a)
# print("address of a: {}".format(id(a)))

# a[0] = 6
# print(a)
# print("address of a: {}".format(id(a)))

#############################################

