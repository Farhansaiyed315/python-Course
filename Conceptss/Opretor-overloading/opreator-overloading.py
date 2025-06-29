
# What is Operator Overloading?
# Operator Overloading means giving special meaning to standard operators (+, -, *, etc.) for user-defined objects (classes).
#
# Python lets us use built-in operators with custom behavior when working with objects of a class.
#
# 🔁 Example: Using + to add two numbers is normal.
# But with overloading, you can use + to add two objects like vectors, complex numbers, etc.



# Example: Operator Overloading with +

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)

    def __str__(self):
        return f"Total Pages: {self.pages}"

book1 = Book(100)
book2 = Book(150)

book3 = book1 + book2
print(book3)  # Output: Total Pages: 250


































































