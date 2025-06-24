
# ----------------------------------------
# 🧠 BASIC PYTHON SYNTAX
# ----------------------------------------

# Comments
# This is a single-line comment

"""
This is a
multi-line comment
"""

print("Hello, World!")  # Output something

# ----------------------------------------
# 🔢 VARIABLES & DATA TYPES
# ----------------------------------------

name = "Farhan"
age = 23
height = 5.9
is_coder = True
nothing = None

# ----------------------------------------
# 🧺 COLLECTIONS
# ----------------------------------------

# List
fruits = ["apple", "banana", "mango"]
print(fruits[0])

# Tuple
point = (10, 20)

# Set
unique_numbers = {1, 2, 3}

# Dictionary
person = {"name": "Farhan", "age": 23}
print(person["name"])

# ----------------------------------------
# 🔁 IF-ELSE STATEMENTS
# ----------------------------------------

if age > 18:
    print("Adult")
elif age == 18:
    print("Just turned adult")
else:
    print("Kid")

# ----------------------------------------
# 🔁 LOOPS
# ----------------------------------------

# While loop
i = 0
while i < 5:
    print(i)
    i += 1

# For loop
for fruit in fruits:
    print(fruit)

# Range loop
for i in range(1, 6):
    print(i)

# Loop Control
for i in range(5):
    if i == 3:
        continue
    if i == 4:
        break
    print(i)

# ----------------------------------------
# 🔧 FUNCTIONS
# ----------------------------------------

def greet(name):
    return "Hello " + name

print(greet("Farhan"))

# Default Arguments
def welcome(name="Bro"):
    print("Welcome", name)

welcome()
welcome("Farhan")

# Return multiple values
def calc(a, b):
    return a + b, a * b

sum_result, product = calc(2, 3)
print(sum_result, product)

# Args and Kwargs
def show(*args, **kwargs):
    print(args)
    print(kwargs)

show(1, 2, name="Farhan", age=23)

# Lambda function
add = lambda x, y: x + y
print(add(5, 3))

# ----------------------------------------
# 🧱 CLASSES & OBJECTS
# ----------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("Hi, I'm", self.name)

p1 = Person("Farhan", 23)
p1.intro()

# ----------------------------------------
# 🎲 LIST COMPREHENSION
# ----------------------------------------

squares = [x*x for x in range(1, 6)]
print(squares)

# ----------------------------------------
# 🧪 STRING METHODS
# ----------------------------------------

text = "  hello python  "
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("h", "H"))
print(text.split())

# ----------------------------------------
# ⚙️ LIST METHODS
# ----------------------------------------

fruits.append("orange")
fruits.remove("banana")
fruits.sort()
fruits.reverse()
print(len(fruits))

# ----------------------------------------
# 🎯 MAP, FILTER, REDUCE
# ----------------------------------------

nums = [1, 2, 3]

# map
doubled = list(map(lambda x: x * 2, nums))
print(doubled)

# filter
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)

# reduce
from functools import reduce
total = reduce(lambda a, b: a + b, nums)
print(total)

# ----------------------------------------
# 📚 WITH STATEMENT (FILE HANDLING)
# ----------------------------------------

with open("file.txt", "w") as f:
    f.write("Hello Farhan")

with open("file.txt", "r") as f:
    print(f.read())

# ----------------------------------------
# 📤 INPUT & OUTPUT
# ----------------------------------------

# name = input("Enter your name: ")
# print("Hello", name)

# ----------------------------------------
# 🎛 ENUMERATE & ZIP
# ----------------------------------------

names = ["Farhan", "Ali"]
ages = [23, 22]

for i, name in enumerate(names):
    print(i, name)

for name, age in zip(names, ages):
    print(name, age)

# ----------------------------------------
# 💣 TRY-EXCEPT
# ----------------------------------------

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("Success")
finally:
    print("Always runs")

# Raise custom error
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by 0!")
    return x / y

# ----------------------------------------
# 📦 MODULE IMPORT
# ----------------------------------------

import math
print(math.sqrt(25))

from math import pi, sqrt
print(pi, sqrt(16))

# ----------------------------------------
# 🧩 TYPE HINTING
# ----------------------------------------

def add_nums(a: int, b: int) -> int:
    return a + b

# ----------------------------------------
# 🚦 TERNARY OPERATOR
# ----------------------------------------

age = 17
msg = "Adult" if age >= 18 else "Teen"
print(msg)

# ----------------------------------------
# 🧊 SET METHODS
# ----------------------------------------

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))       # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}
print(a.difference(b))  # {1, 2}

# ----------------------------------------
# 🔑 DICTIONARY METHODS
# ----------------------------------------

person = {"name": "Farhan", "age": 23}

print(person.keys())    # dict_keys(['name', 'age'])
print(person.values())  # dict_values(['Farhan', 23])
print(person.items())   # dict_items([('name', 'Farhan'), ('age', 23)])

# Loop through dictionary
for key, value in person.items():
    print(key, value)

# ----------------------------------------
# 🧩 TYPE CASTING
# ----------------------------------------

x = "123"
x_int = int(x)

y = 100
y_str = str(y)

list_from_tuple = list((1, 2, 3))

# ----------------------------------------
# 🧪 ASSERTIONS
# Used for debugging
assert 2 + 2 == 4
# assert 2 + 2 == 5  # This will raise AssertionError

# ----------------------------------------
# 🔄 RECURSION
# Function calling itself
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

# ----------------------------------------
# 🧠 GLOBAL vs LOCAL VARIABLES
# ----------------------------------------

x = 10  # global

def my_func():
    global x
    x = 5
    print("Inside:", x)

my_func()
print("Outside:", x)

# ----------------------------------------
# 📂 FILE MODES
# 'r' – read only
# 'w' – write (overwrite)
# 'a' – append
# 'r+' – read + write

# ----------------------------------------
# 📚 DOCSTRINGS
def add(a, b):
    """This function adds two numbers."""
    return a + b

print(add.__doc__)

# ----------------------------------------
# 🧪 EXCEPTIONS – MULTIPLE
try:
    num = int("abc")
    result = 10 / 0
except ValueError:
    print("Conversion error")
except ZeroDivisionError:
    print("Zero error")

# ----------------------------------------
# 📦 __name__ == "__main__"
def say_hi():
    print("Hi from main!")

if __name__ == "__main__":
    say_hi()

# ----------------------------------------
# 🧪 GENERATORS (yield)
def count_up(limit):
    i = 1
    while i <= limit:
        yield i
        i += 1

for num in count_up(5):
    print(num)

# ----------------------------------------
# 🔄 ITERATORS
nums = [1, 2, 3]
it = iter(nums)
print(next(it))
print(next(it))

# ----------------------------------------
# 🧱 INHERITANCE (OOP)
class Animal:
    def speak(self):
        print("Animal Sound")

class Dog(Animal):
    def speak(self):
        print("Bark!")

d = Dog()
d.speak()

# ----------------------------------------
# 🧠 PROPERTY DECORATOR
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

p = Product(100)
print(p.price)

# ----------------------------------------
# 💡 DECORATORS
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# ----------------------------------------
# 🔄 COMPREHENSIONS
# Set
nums = [1, 2, 2, 3]
unique = {x for x in nums}

# Dictionary
squares = {x: x*x for x in range(1, 4)}

# ----------------------------------------
# 🛠 UTILITY: pass, del, is, in
pass  # placeholder

del x  # delete variable

# 'is' and 'in'
a = [1, 2]
b = a
print(a is b)       # True
print(2 in a)       # True
