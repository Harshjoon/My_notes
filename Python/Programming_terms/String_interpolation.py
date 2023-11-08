# String interpolation

# The process of evaluating a string literal containing one or more placeholder
# , yeilding a result in which the placeholders are replaced with their
# corresponding values.


##################################################################
'''Example'''

name = "harsh"
age  = 24

#greeting = "My name is " + name + " and I am " + age + " years old."
#print(greeting) # this will give error

greeting = "My name is " + name + " and I am " + str(age) + " years old."
print(greeting) # this will give error

# correct way, using string interpolation
greeting = "My name is {} and I am {} years old.".format(name, age)
print(greeting)
