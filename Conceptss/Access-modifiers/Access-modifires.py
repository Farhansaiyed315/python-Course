

#  Public (Default)
# Accessible from anywhere (inside or outside the class).
#
# No underscore is used.

class Student:
    def __init__(self, name):
        self.name = name  # public variable

    def show(self):  # public method
        print("Name:", self.name)

s = Student("Farhan")
print(s.name)  # ✅ Accessible
s.show()       # ✅ Accessible


# Protected (Use single underscore _)
# Accessible within the class and subclasses (child classes).
#
# By convention, it's for internal use only — still can be accessed from outside, but you shouldn't.


class Student:
    def __init__(self, name):
        self._name = name  # protected variable

    def _show(self):  # protected method
        print("Name:", self._name)
#
# s = Student("Farhan")
# print(s._name)   # ⚠️ Possible, but not recommended
# s._show()        # ⚠️ Possible, but not recommended
#
#



# Private (Use double underscore __)
# Accessible only inside the class.
#
# Name gets changed internally (name mangling), so accessing it from outside is tricky.


class Student:
    def __init__(self, name):
        self.__name = name  # private variable

    def __show(self):  # private method
        print("Name:", self.__name)

    def display(self):  # public method to access private stuff
        self.__show()
#
# s = Student("Farhan")
# # print(s.__name)    ❌ Error: Not accessible directly
# # s.__show()         ❌ Error: Not accessible directly
# s.display()          # ✅ Works, because we accessed __show inside the class
#



# Quick Summary Table:

# | Access Modifier | Syntax   | Access Scope              |
# | --------------- | -------- | ------------------------- |
# | Public          | `name`   | Everywhere                |
# | Protected       | `_name`  | Within class and subclass |
# | Private         | `__name` | Only within the class     |
#




























