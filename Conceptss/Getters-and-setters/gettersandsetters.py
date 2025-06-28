

# What are Getters and Setters?
# In Python (and in OOP), getters and setters are used to access and modify the value of private variables in a class.
#
# ✅ Getter → "get" the value of a variable
# ✅ Setter → "set" (change/update) the value of a variable

#  Why do we need them?
# Sometimes, you don’t want your variables to be accessed or modified directly (for security, validation, or control). So you make them private using __ (double underscore), and access them safely with getters and setters.

class Student:
    def __init__(self, name):
        self.__name = name  # private variable

    # Getter method
    def get_name(self):
        return self.__name

    # Setter method
    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.strip() != "":
            self.__name = new_name
        else:
            print("Invalid name")

# Using the class
s1 = Student("Farhan")

print(s1.get_name())   # ✅ Get the name

s1.set_name("Zayn")    # ✅ Set a new name

print(s1.get_name())   # Output: Zayn

s1.set_name("")        # ❌ Invalid input


# In Short (For Exams):
# Getters and setters are used to access and modify
# private variables of a class in a safe and controlled way.
# In Python, we can define them manually using normal methods
# or use @property decorators for a cleaner syntax.
























































