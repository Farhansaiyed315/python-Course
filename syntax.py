
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


#  Python Syntax Part 3: Pro-Level Essentials

# ----------------------------------------
# 🧩 PACKAGES & MODULES
# ----------------------------------------

# mymodule.py
def welcome():
    print("Welcome to my module!")

# main.py
import mymodule
mymodule.welcome()

# Or import specific
from mymodule import welcome
welcome()

# ----------------------------------------
# 🧰 JSON (for APIs & data exchange)
import json

# Python to JSON
data = {"name": "Farhan", "age": 23}
json_str = json.dumps(data)
print(json_str)

# JSON to Python
parsed_data = json.loads(json_str)
print(parsed_data["name"])

# ----------------------------------------
# 📁 OS MODULE
import os

print(os.getcwd())           # current directory
os.mkdir("new_folder")       # make folder
os.rename("old.txt", "new.txt")  # rename file
os.remove("new.txt")         # delete file
os.rmdir("new_folder")       # remove folder

# ----------------------------------------
# 🕰 TIME & DATETIME
import time
import datetime

time.sleep(2)  # pause for 2 seconds

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# ----------------------------------------
# 📦 VIRTUAL ENVIRONMENT (CLI usage)
# These are shell commands (not Python code)
# python -m venv env
# env\Scripts\activate (Windows)
# source env/bin/activate (Linux/Mac)

# ----------------------------------------
# 📦 INSTALLING PACKAGES
# pip install package_name
# Example: pip install requests

# ----------------------------------------
# 🌐 HTTP REQUESTS (with requests module)
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())

# ----------------------------------------
# 📌 ADVANCED CLASS (Inheritance + super)
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} is driving")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving")

mycar = Car("Toyota", "Fortuner")
mycar.drive()

# ----------------------------------------
# 🧠 CLASS METHODS & STATIC METHODS
class User:
    users = 0

    def __init__(self):
        User.users += 1

    @classmethod
    def get_users(cls):
        return cls.users

    @staticmethod
    def greet():
        print("Welcome, user!")

print(User.get_users())
User.greet()

# ----------------------------------------
# 📥 EXTERNAL INPUT (CMD arguments)
import sys

print("Script name:", sys.argv[0])
if len(sys.argv) > 1:
    print("Arg:", sys.argv[1])

# ----------------------------------------
# 🎛 ENUM (useful for fixed choices)
from enum import Enum

class Status(Enum):
    SUCCESS = 1
    FAILURE = 0

print(Status.SUCCESS)
print(Status.SUCCESS.name)
print(Status.SUCCESS.value)

# ----------------------------------------
# 🔄 CONTEXT MANAGER (custom with `with`)
class MyContext:
    def __enter__(self):
        print("Enter block")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit block")

with MyContext():
    print("Inside context")

# ----------------------------------------
# 🔥 EXCEPTION CHAINING
try:
    try:
        raise ValueError("Inner error")
    except ValueError as e:
        raise RuntimeError("Outer error") from e
except RuntimeError as err:
    print(err.__cause__)

# ----------------------------------------
# 🧪 TESTING WITH ASSERT (simple test)
def double(x):
    return x * 2

assert double(2) == 4
assert double(5) == 10
# assert double(3) == 7  # This will fail!

