# A string is a sequence of characters. It can contain letters, numbers, symbols, spaces—anything inside quotes.

# Examples of strings
name = "Farhan"
greet = 'Hello'
info = "12345"

# How to Create Strings

str1 = "Hello World"
str2 = 'Python is cool'


# You can also use triple quotes (''' or """) for multi-line strings:

multiline = """This is
a multi-line
string."""

#
# | Method               | Use                     | Example                                  |
# | -------------------- | ----------------------- | ---------------------------------------- |
# | `len()`              | Length of string        | `len("Hello")` → 5                       |
# | `.lower()`           | Convert to lowercase    | `"HELLO".lower()` → `'hello'`            |
# | `.upper()`           | Convert to uppercase    | `"hello".upper()` → `'HELLO'`            |
# | `.strip()`           | Remove extra spaces     | `"  hello  ".strip()` → `'hello'`        |
# | `.replace(old, new)` | Replace part of string  | `"Hello".replace("H", "J")` → `'Jello'`  |
# | `.split()`           | Break string into list  | `"a,b,c".split(",")` → `['a', 'b', 'c']` |
# | `.find()`            | Find index of substring | `"hello".find("l")` → `2`                |


# Indexing (position of each character)

word = "Python"
print(word[0])  # P
print(word[-1]) # n (last character)


# Slicing (cutting string)

word = "Python"
print(word[0:3])  # Pyt
print(word[2:])   # thon
print(word[:4])   # Pyth


# String Concatenation (Joining Strings)

first = "Hello"
second = "World"
result = first + " " + second
print(result)  # Hello World


# Looping Through Strings

for char in "Farhan":
    print(char)


# f-strings (Python 3.6+):

name1 = "Farhan"
age = 21
print(f"My name is {name1} and I am {age} years old.")

#  String is Immutable

name2 = "Farhan"
# name[0] = "M"  ❌ This will give error



