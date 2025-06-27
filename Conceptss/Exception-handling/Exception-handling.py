
# What is Exception Handling in Python?
# Exception Handling is a way to manage errors that occur during the execution of a program.
# Instead of crashing the program, Python gives us tools to catch and handle the error.


# Why use Exception Handling?
# Because it helps you:
#
# Avoid program crashes
#
# Show user-friendly error messages
#
# Write clean and reliable code

#  Common Keywords in Python Exception Handling:

#  | Keyword   | Use                                                               |
# | --------- | ----------------------------------------------------------------- |
# | `try`     | Write code that might cause an error                              |
# | `except`  | Write code to handle the error                                    |
# | `else`    | Runs if no error occurs in the `try` block                        |
# | `finally` | Always runs, no matter what (used to clean up like closing files) |


# Summary Points to Write in Exam:
# try block runs the risky code
#
# except block handles the error
#
# else runs if no error occurs
#
# finally always runs (cleanup code)
#
# Helps avoid program crashes and handle errors smoothly


#  Basic Syntax:

try:
    # risky code
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("No error occurred.")
finally:
    print("This runs no matter what.")


# Example 1: Handling division by zero

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")


#  Example 2: Multiple Exceptions

try:
    a = int(input("Enter number: "))
    b = int(input("Enter another: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Please enter valid numbers.")




#  finally Example:

try:
    file = open("data.txt")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing program.")
















