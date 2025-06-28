
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



# seek(offset, whence=0)
# 👉 Purpose:
# Moves the file pointer (cursor) to a specific position in the file.


# offset: Number of bytes to move.
#
# whence: Tells from where to start the offset:
#
# 0 → from beginning (default)
#
# 1 → from current position
#
# 2 → from end of file

f = open("example.txt", "r")
f.seek(5)  # Move to 5th byte from beginning
print(f.read())  # Reads from 5th byte onwards
f.close()


#  tell()
# 👉 Purpose:
# Returns the current position of the file pointer (in bytes).

f = open("example.txt", "r")
print(f.tell())  # Usually returns 0 (start of file)
f.read(10)       # Read 10 bytes
print(f.tell())  # Now pointer is at position 10
f.close()

# Other Useful File Functions:

# | Function           | Purpose                                                                    |
# | ------------------ | -------------------------------------------------------------------------- |
# | `read(size)`       | Reads `size` bytes from the file. If not given, reads all.                 |
# | `readline()`       | Reads one full line.                                                       |
# | `readlines()`      | Reads all lines and returns a list.                                        |
# | `write(string)`    | Writes a string to the file.                                               |
# | `writelines(list)` | Writes a list of strings to the file.                                      |
# | `close()`          | Closes the file. Always use it or `with open(...)`.                        |
# | `flush()`          | Forces writing data to disk (used with `write()` sometimes).               |
# | `truncate(size)`   | Cuts the file at `size` bytes. If size not given, cuts at current pointer. |


#  Pro Tip: Use with open(...) to auto-close files

with open("example.txt", "r") as f:
    data = f.read()
    print(data)


# What is a Lambda Function?
# A lambda function is a short, one-line, anonymous function in Python.
# It's useful when you want to write a quick function without giving it a name.
#
# Think of it as a shortcut for small tasks — like a one-time-use function.
# (Perfect when you don’t wanna write a whole def block.)

# lambda arguments: expression

# It's like saying:

# def func(x):
#     return x + 2

# But in lambda, it becomes:

# lambda x: x + 2

# Add two numbers:

add = lambda a, b: a + b
print(add(5, 3))  # Output: 8


square = lambda x: x * x
print(square(4))  # Output: 16


nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Output: [1, 4, 9, 16]



nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]


# When to Use Lambda?
# ✅ When you need a quick function
# ✅ Used with map(), filter(), reduce()
# ✅ You don’t need to reuse the function elsewhere





















