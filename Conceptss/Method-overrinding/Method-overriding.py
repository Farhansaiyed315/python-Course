
# What is Method Overriding?
# Method overriding is when a child class provides a specific implementation of a method that is already defined in its parent class.
#
# In short:
#
# Same method name in both parent and child class, but the child’s version replaces the parent’s version when used.


#  Why use it?
# To customize or change behavior of the parent class method in the child class.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # Overriding the parent class method
        print("Dog barks")

# Using the classes
a = Animal()
a.speak()  # Output: Animal speaks

d = Dog()
d.speak()  # Output: Dog barks ✅ (Overridden method)


#  Bonus: Calling Parent Method from Child
# If you still want to use the parent class method inside the child class, use super():

class Dog(Animal):
    def speak(self):
        super().speak()  # Calls parent method
        print("Dog barks")






































































