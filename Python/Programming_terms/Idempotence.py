# Idempotence

# The property of certain operation that can be applied multiple times
# without changing the result beyond initial condition.

# f(f(x)) = f(x)

##############################################
'''Example'''

def add_ten(num):
    return num + 10

print(add_ten(10))
print(add_ten(add_ten(10))) # not idempotence

print(abs(-10))
print(abs(abs(-10)))        # idempotence

a = 10                      # its also idempotence statement

