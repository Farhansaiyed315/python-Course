
#  Single Inheritance
# In single inheritance, a child class inherits from only one parent class.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()


#  Multiple Inheritance
# In multiple inheritance, a child class inherits from more than one parent class.

class Father:
    def skills(self):
        print("Father: Gardening")

class Mother:
    def hobbies(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def own_skill(self):
        print("Child: Playing")

c = Child()
c.skills()
c.hobbies()
c.own_skill()


# Multilevel Inheritance
# In multilevel inheritance, a class inherits from a child class which itself inherits from another class.

class Grandfather:
    def house(self):
        print("Grandfather: Owns a house")

class Father(Grandfather):
    def car(self):
        print("Father: Owns a car")

class Son(Father):
    def bike(self):
        print("Son: Owns a bike")

s = Son()
s.house()
s.car()
s.bike()


# Hierarchical Inheritance
# In hierarchical inheritance, multiple child classes inherit from a single parent class.
#
# 💻 Code Example:

class Parent:
    def message(self):
        print("Message from Parent")

class Child1(Parent):
    def child1_message(self):
        print("Message from Child1")

class Child2(Parent):
    def child2_message(self):
        print("Message from Child2")

c1 = Child1()
c2 = Child2()

c1.message()
c1.child1_message()

c2.message()
c2.child2_message()


#  Hybrid Inheritance
# Hybrid inheritance is a mix of two or more types of inheritance (like combination of multiple + multilevel etc).

class A:
    def featureA(self):
        print("Feature A")

class B(A):
    def featureB(self):
        print("Feature B")

class C:
    def featureC(self):
        print("Feature C")

class D(B, C):
    def featureD(self):
        print("Feature D")

d = D()
d.featureA()
d.featureB()
d.featureC()
d.featureD()


# Summary Table:

# | Inheritance Type | Description                                       |
# | ---------------- | ------------------------------------------------- |
# | Single           | One child, one parent                             |
# | Multiple         | One child, many parents                           |
# | Multilevel       | Grandparent → Parent → Child                      |
# | Hierarchical     | One parent, many children                         |
# | Hybrid           | Combination of multiple, single, multilevel, etc. |



