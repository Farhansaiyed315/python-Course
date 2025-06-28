

# What is OOPs in Python?
# OOPs stands for Object-Oriented Programming. It’s a way of writing code using classes and objects to model real-world things.
#
# Python supports OOPs fully!

# Main Concepts of OOPs
# Class – Blueprint/template for creating objects.
#
# Object – Real-world entity created from a class.
#
# Inheritance – One class can inherit properties from another.
#
# Encapsulation – Hiding the internal details, only showing necessary stuff.
#
# Polymorphism – Same function name behaves differently based on the context.
#
# Abstraction – Hiding complex logic and showing only the important features.

#  Class and Object

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating object
s1 = Student("Farhan", 21)
s1.display()


#  Inheritance------------------------------------------

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()  # Output: Dog barks


#  Encapsulation--------------------------------------------

class Person:
    def __init__(self):
        self.__name = "Private Name"  # __ makes it private

    def show(self):
        print(self.__name)

p = Person()
p.show()


# Polymorphism----------------------------------------------

class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly")

for animal in [Bird(), Penguin()]:
    animal.fly()


#  Abstraction (using ABC module)------------------------------

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

c = Car()
c.start()


# | Concept           | Explanation                                             |
# | ----------------- | ------------------------------------------------------- |
# | **Class**         | Blueprint for objects                                   |
# | **Object**        | Instance of a class                                     |
# | **Inheritance**   | Child class uses parent class features                  |
# | **Encapsulation** | Hiding data using private/protected attributes          |
# | **Polymorphism**  | Same method name works differently in different classes |
# | **Abstraction**   | Hiding internal code, only showing necessary info       |




#  What is a Constructor in Python?
# A constructor is a special method used to initialize objects when a class is created.
#
# In Python, the constructor method is always written as:

# def __init__(self):
#     # initialization code


# Why Use Constructor?
# Automatically assigns values to object properties
#
# Saves time when creating multiple objects
#
# Keeps your code clean and organized



#  Basic Constructor Example

class Student:
    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating object
s1 = Student("Farhan", 21)
s1.display()


# Types of Constructors in Python

# | Type                          | Description     | Example                     |
# | ----------------------------- | --------------- | --------------------------- |
# | **Default constructor**       | No arguments    | `def __init__(self):`       |
# | **Parameterized constructor** | Takes arguments | `def __init__(self, name):` |



#  Default Constructor

class Demo:
    def __init__(self):
        print("Default constructor called")

obj = Demo()


#  Parameterized Constructor

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show(self):
        print(f"{self.brand} - {self.year}")

c1 = Car("BMW", 2022)
c1.show()


# Bonus: Can We Have Multiple Constructors?
# Python does not support multiple __init__() methods like Java/C++. But we can use default values or classmethods to mimic it.

class User:
    def __init__(self, name="Guest"):
        self.name = name

u1 = User()
u2 = User("Farhan")

print(u1.name)  # Guest
print(u2.name)  # Farhan











