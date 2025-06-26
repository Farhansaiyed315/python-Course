# What is an f-string?
# An f-string is a way to insert variables or expressions inside
# a string. It's short for formatted string. Introduced in
# Python 3.6+, it's clean, fast, and easy to read.

name = "Farhan"
age = 21

print(f"My name is {name} and I am {age} years old.")


# You can even do math and functions inside it:
a = 10
b = 20
print(f"The sum of a and b is {a + b}")

# With functions:

def greet(name):
    return f"Hello, {name}!"

print(greet("Farhan"))


# Example with date:

import datetime

today = datetime.date.today()
print(f"Today's date is {today}")


# Loop + f-string:

for i in range(3):
    print(f"Index: {i}")


