# Type casting means converting one data type into another.
#
# For example:
#
# Changing an integer into a string
#
# Changing a string into a float
# #
# Why do we use it?
# Because sometimes we need to:
#
# Do math on values that are strings (like "100")
#
# Convert user input (which is always a string) to numbers
#
# Make data compatible with different operations


# 1. Implicit Type Casting (Python does it automatically)

x = 5       # int
y = 2.5     # float

z = x + y   # int + float = float
print(z)    # Output: 7.5
print(type(z))  # Output: <class 'float'>


#
#  Explicit Type Casting (You do it manually)
# You use built-in functions like:
#
# int() – converts to integer
#
# float() – converts to float
#
# str() – converts to string
#
# bool() – converts to boolean
#


# String to Int
num = "42"
print(int(num) + 10)

# Float to Int
x = 3.9
print(int(x))          # Output: 3 (decimal part removed)

# INt to string.

age = 20
print("Age is " + str(age))


# Any to boolean.
print(bool(0))       # False
print(bool(100))     # True
print(bool(""))      # False
print(bool("Hi"))    # True





