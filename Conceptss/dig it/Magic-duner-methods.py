
#  What Are Magic/Dunder Methods?
# "Dunder" stands for Double UNDerscore — like __init__, __str__, __add__, etc.
#
# They are special methods in Python that start and end with double underscores. Python uses them behind the scenes to perform basic operations like:
#
# Creating objects
#
# Printing objects
#
# Adding objects
#
# Comparing objects



# Why Use Them?
# Magic methods let you customize your class behavior to act like built-in types (like strings, integers, etc).
#
# Example: Want to use + to add two objects? You can define __add__.

#  Final Tip
# You don’t need to memorize all of them now.
# Just remember: when you do something like +, print(), or len() on an object, Python is calling a magic method in the background.


#  Most Common Magic Methods (With Simple Use Cases)


# __init__(self, ...)
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Farhan")  # __init__ runs here


# __str__(self)

# String representation – runs when you use print()

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student name is {self.name}"

print(Student("Farhan"))  # ➝ "Student name is Farhan"


# __repr__(self)
# Unambiguous representation – used mostly in debugging.

def __repr__(self):
    return f"Student('{self.name}')"


# __add__(self, other)
# For + operator between objects

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

a = Number(5)
b = Number(10)
print(a + b)  # 15


#  __eq__(self, other)
# For == comparisons

def __eq__(self, other):
    return self.name == other.name


# __getitem__(self, index)
# Lets you use [] with objects

class Bag:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

b = Bag(["pen", "book"])
print(b[0])  # "pen"


















































