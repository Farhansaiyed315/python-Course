
# Simple Definition:
# The walrus operator lets you assign a value to a variable as part of an expression (like inside an if, while, or list comprehension) — instead of doing it in a separate line.

# Why is it useful?
# Normally, assignment and condition checking are done separately:

value = input("Enter: ")
if value == "yes":
    print("You said yes!")


# With the walrus operator, you can do both in one line:

if (value := input("Enter: ")) == "yes":
    print("You said yes!")


# Example 1: Inside if condition

if (n := len("hello")) > 3:
    print(f"Length is {n}")























































