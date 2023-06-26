# Functions
# 1. allow for reusable code
# 2. allow for cleaner code
# 3. allow for testing
# 4. allow for debugging
# 5. allow for organization

# Syntax

# def function_name():
#     # code block
#     # code block

# function_name() call the function


def function_name():
    # print("Afternoon Session. Reccess")
    pass

function_name()

# function with parameters
# Parameter: is the variable listed inside the parentheses in 
# the function definition
def function_name(name) -> int:
    # print("Hello " + name)    
    pass

# Arg: is the value passed to the function
function_name("Overloaded function")


def add_multiple_numbers(*args):
    sum = 0
    for number in args:
        sum += number
    # print(sum)


add_multiple_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# using default parameters
def greetings(name = "Wilfred"):
    # print("Hello " + name)
    pass # do nothing


greetings() # defaults to Wilfred
greetings("Majaliwa") # overrides the default value


# Return a String value
def return_string_value():
    return "Hello World"


# Return a Integer value
def return_integer_value():
    return 100


# Return a Float value
def return_float_value():
    return 100.00


# Return a Boolean value
def return_boolean_value():
    return True


# Return a List value
def return_list_value():
    return [1, "Me", 3, 4, 5]



# Modules
# A module is a file containing a set of 
# functions to include in your application

# import the module
# math is a built-in module
import math

# use the module
# print(math.pi)

def product(x, y):
    return x * y

print(product(2, 3))


# import everything from the file
# from python_modules import * # import all

# # import specific functions
# from python_modules import add_two_numbers, subtract_two_numbers 

# use as if there is a conflict
import python_modules as pm # pm is the alias. 

print(pm.add_two_numbers(1, 2))
print(pm.subtract_two_numbers(1, 2))
print(pm.multiply_two_numbers(1, 2))
print(pm.divide_two_numbers(1, 2))


# cude root of a number
def cube_root(number):
    return math.pow(number, 1/3)

print(cube_root(27))



