
# What is a Function?
# A function is like a reusable code box.
# You put some code inside it once, and then call it anytime you want.
# It helps to avoid repeating the same code again and again.

# def function_name():
#     # code block

def greet():
    print("Hello, welcome!")

greet()  # calling the function


def greet(name):
    print(f"Hello, {name}!")

greet("Farhan")


# Function with Return (Output):

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum is:", result)


#  Default Parameter:

def greet(name="friend"):
    print(f"Hey {name}!")

greet()         # uses default
greet("Farhan") # overrides default

# Keyword Arguments:

def intro(name, age):
    print(f"My name is {name} and I'm {age} years old.")

intro(age=21, name="Ayaan")  # order doesn't matter here


# Return Multiple Values:

def calc(a, b):
    return a+b, a-b, a*b

x, y, z = calc(10, 5)
print(x, y, z)

                # Types of Functions:

# | Type               | Description                         |
# | ------------------ | ----------------------------------- |
# | Built-in functions | `print()`, `len()`, `range()`, etc. |
# | User-defined       | You create them using `def`         |
# | Lambda functions   | One-line anonymous functions        |



# Lambda Function (Quick Mini Function):

add = lambda x, y: x + y
print(add(2, 3))  # Output: 5


# Real-World Mini Projects You Can Try with Functions:
# Calculator App
#
# Quiz App
#
# Login System
#
# BMI Checker
#
# Even/Odd Checker