
# What is a Docstring in Python?
# A docstring (documentation string) is a special type of
# multi-line string used to document your code — like functions,
# classes, or modules. It's written inside triple quotes
# (""" """ or ''' ''') and placed right after the definition
# of a function, class, or module.
#
# It helps others (and your future self 😅)
# understand what your code does without needing to
# read the entire logic.

def function_name():
    """This is a docstring.
    It explains what the function does."""
    # code here

#  Example 1: Docstring for a Function

def greet(name):
    """This function greets the user with their name."""
    print("Hello", name)


#  Example 2: Docstring for a Class

class Person:
    """This class represents a person with name and age."""

    def __init__(self, name, age):
        """Initialize the name and age of the person."""
        self.name = name
        self.age = age


#  Why Use Docstrings?
# It improves code readability
#
# Helps when using help() function in Python
#
# Useful for documentation generation tools like Sphinx

# Quick One-Liner vs Multi-Line

def add(a, b):
    """Add two numbers"""  # One-liner


def add(a, b):
    """
    Add two numbers.

    Parameters:
    a (int): first number
    b (int): second number

    Returns:
    int: sum of a and b
    """  # Multi-line


