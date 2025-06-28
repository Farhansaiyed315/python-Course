
#  What is a Class Method in Python?
# A class method is a method that:
#
# Works with the class itself instead of instances (objects).
#
# It takes cls as the first parameter (instead of self).
#
# It can modify class-level data (not instance data).
#
# It's defined using the @classmethod decorator.


#  Syntax:
#
# class ClassName:
#     @classmethod
#     # def method_name(cls, args):



#  Simple Example:

class Student:
    school_name = "ABC School"  # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name


# Using class method to change the class variable
Student.change_school("XYZ School")

s1 = Student("Farhan")
print(s1.school_name)  # Output: XYZ School


# Why use class methods?
# To access or modify class variables, especially when you don’t have an object yet.


# Difference Between @classmethod, @staticmethod, and normal methods:

# | Feature          | Instance Method      | Class Method        | Static Method             |
# | ---------------- | -------------------- | ------------------- | ------------------------- |
# | First arg        | `self`               | `cls`               | No specific first arg     |
# | Access instance? | ✅                    | ❌                   | ❌                         |
# | Access class?    | ✅ (via self)         | ✅                   | ❌                         |
# | Use case         | Object-specific data | Class-specific data | Utility methods (helpers) |


# Class Method for Alternative Constructors
# You can use a class method to create an object in a different way. Example:



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))

# Create object using class method
p1 = Person.from_string("Farhan,22")
print(p1.name)  # Farhan
print(p1.age)   # 22

#  In Short:
# Use @classmethod when you want to work with the class, not the object.
#
# It’s useful to change class variables, or create alternative constructors.




















