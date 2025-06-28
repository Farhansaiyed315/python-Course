
#  What is super in Python?
# super() is a built-in function in Python used inside a child class to call methods from the parent class.
#
# Basically, it's like saying:
#
# "Hey parent class, I need to use your stuff!"


#  Why use super()?
# To reuse code from the parent class
#
# Helps with multiple inheritance (more advanced)
#
# Keeps your code clean and DRY (Don't Repeat Yourself)


class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # calling Parent's greet
        print("Hello from Child")

c = Child()
c.greet()

#  Real-World Example: Constructor with super()

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)   # calling Person's __init__
        self.roll_no = roll_no

s = Student("Farhan", 101)
print(s.name)
print(s.roll_no)







































