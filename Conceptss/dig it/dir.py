
#  dir()
# What it does:
# Returns a list of all the attributes and methods (including magic methods) of an object.
#
# Use case:
# You want to see what stuff (variables/functions) you can access on an object.


# class Student:
#     def __init__(self, name):
#         self.name = name
#
# s = Student("Farhan")
# print(dir(s))


# __dict__------------------------------------------------
# What it does:
# Gives you a dictionary containing all the instance variables of an object.
#
# Use case:
# You want to see the actual data stored in an object.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Farhan", 22)
print(s.__dict__)



#  help()--------------------------------------------------
# What it does:
# Shows the documentation of a class, function, or module — basically a built-in Python guide.
#
# Use case:
# You're confused about how something works? Call help() and it will explain.

help(str)

# A long but helpful explanation of how strings work in Python, with available methods and examples.

# | Function       | Purpose                     | Returns                   |
# | -------------- | --------------------------- | ------------------------- |
# | `dir(obj)`     | List all attributes/methods | List                      |
# | `obj.__dict__` | Show instance variables     | Dictionary                |
# | `help(obj)`    | Show documentation          | Text output (in terminal) |









