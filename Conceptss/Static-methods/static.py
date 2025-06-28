
# What is a Static Method?
# A static method is a method inside a class that doesn’t use self or cls.
#
# It doesn't care about the class or the object.
#
# It's like a normal function, but it lives inside a class.


# When do we use it?
# Use it when:
#
# The method logically belongs to the class, but it doesn’t need to access or modify class/object data.



class MyClass:
    @staticmethod
    def greet(name):
        print(f"Hey {name}, welcome to MyClass!")

# You can call it using the class name
MyClass.greet("Farhan")

# OR using an object (not recommended, but works)
obj = MyClass()
obj.greet("Saiyed")

# It doesn’t care who’s calling—class or object.


#  Example Use Case

class MathUtils:
    @staticmethod
    def is_even(num):
        return num % 2 == 0

print(MathUtils.is_even(10))  # True
print(MathUtils.is_even(3))   # False



#  Comparison Table

# | Feature          | Instance Method | Class Method   | Static Method   |
# | ---------------- | --------------- | -------------- | --------------- |
# | Access to `self` | ✅ Yes           | ❌ No           | ❌ No            |
# | Access to `cls`  | ❌ No            | ✅ Yes          | ❌ No            |
# | Uses decorator   | No              | `@classmethod` | `@staticmethod` |





















































