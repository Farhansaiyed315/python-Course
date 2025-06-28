
#  Instance Variables
# Belong to: an object (instance) of the class.
#
# Created using: self
#
# Unique to each object.
#
# You define them like this: self.name = "Farhan"


# Example:

class Student:
    def __init__(self, name):
        self.name = name  # instance variable

s1 = Student("Farhan")
s2 = Student("Ayaan")

print(s1.name)  # Farhan
print(s2.name)  # Ayaan



# Class Variables
# Belong to: the class itself, not individual objects.
#
# Shared by all objects of the class.
#
# You define them outside of any method in the class.


class Student:
    college = "IGNOU"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

s1 = Student("Farhan")
s2 = Student("Ayaan")

print(s1.college)  # IGNOU
print(s2.college)  # IGNOU



# Difference Table

# | Feature             | Instance Variable           | Class Variable                 |
# | ------------------- | --------------------------- | ------------------------------ |
# | Defined using       | `self.variable`             | Directly in class (`variable`) |
# | Belongs to          | Each object                 | Whole class                    |
# | Unique for each obj | Yes                         | No (shared)                    |
# | When it's created   | Inside `__init__` or method | Outside any method             |



# One more twist:
# You can access class variables from objects, but if you assign a value using self.variable, it becomes an instance variable, shadowing the class one.


class Student:
    college = "IGNOU"

s1 = Student()
s1.college = "DU"  # creates an instance variable

print(Student.college)  # IGNOU
print(s1.college)       # DU



# Summary:
# Use instance variables when each object needs its own data.
# Use class variables when all objects need shared data.

























































