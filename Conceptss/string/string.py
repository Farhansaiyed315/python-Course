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


# Escape Characters in Strings
# Some characters can’t be typed directly (like quotes inside quotes). So we use escape characters (start with \).
#
# | Escape Code | Meaning      | Example                             |
# | ----------- | ------------ | ----------------------------------- |
# | `\n`        | New Line     | `"Hello\nWorld"` →                  |
# | Hello       |              |                                     |
# | World       |              |                                     |
# | `\t`        | Tab Space    | `"Hello\tWorld"` → `Hello    World` |
# | `\'`        | Single quote | `'I\'m fine'`                       |
# | `\"`        | Double quote | `"He said \"Hi\""`                  |
# | `\\`        | Backslash    | `"This is a backslash: \\"`         |
#

# Common String Methods Explained with Examples

text = "  python is awesome  "


#
# | Method             | What It Does                  | Example Output          |
# | ------------------ | ----------------------------- | ----------------------- |
# | `.strip()`         | Removes spaces from both ends | `"python is awesome"`   |
# | `.lstrip()`        | Removes left space            | `"python is awesome  "` |
# | `.rstrip()`        | Removes right space           | `"  python is awesome"` |
# | `.capitalize()`    | Capitalizes first letter      | `"Python is awesome"`   |
# | `.title()`         | Capitalizes all words         | `"Python Is Awesome"`   |
# | `.startswith("p")` | Checks if starts with "p"     | `True`                  |
# | `.endswith("e")`   | Checks if ends with "e"       | `True`                  |
# | `.count("s")`      | Counts how many times "s"     | `2`                     |
# | `.index("a")`      | First position of "a"         | `11`                    |
#


#  String Comparison

a = "hello"
b = "HELLO"

print(a == b)        # False
print(a.lower() == b.lower())  # True


#  Check for Substrings

txt = "I love Python"
print("Python" in txt)     # True
print("Java" not in txt)   # True


#  Join Strings (Reverse of split)

words = ['I', 'love', 'Python']
sentence = " ".join(words)
print(sentence)  # I love Python


 # Reversing a String
name4 = "Farhan"
print(name4[::-1])  # nahraF


# Check if String is Numeric/Alpha

s1 = "123"
s2 = "abc123"
print(s1.isdigit())  # True
print(s2.isalnum())  # True
print(s2.isalpha())  # False


# String as a List of Characters

for char in "Farhan":
    print(char)


 # Convert List to String

chars = ['P', 'y', 't', 'h', 'o', 'n']
word = ''.join(chars)
print(word)  # Python

 # String Formatting (3 Ways)

name5 = "Farhan"
age = 21

# 1. f-string (modern way)
print(f"My name is {name5}, I am {age}")

# 2. format() method
print("My name is {}, I am {}".format(name5, age))

# 3. % operator (old style)
print("My name is %s, I am %d" % (name5, age))

#  String Multiplication
# You can repeat strings using *

print("Hi! " * 3)   # Hi! Hi! Hi!

 # in and not in Keyword for Searching
# Very handy in real-world checks:

email = "farhan@gmail.com"
print("@" in email)        # True
print("yahoo" not in email) # True