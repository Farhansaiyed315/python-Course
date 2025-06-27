# if __name__ == "__main__" in Python

# In Python, if __name__ == "__main__": is a common and important
# line of code. Let me explain it to you in simple,


# Why use this line?
# This line is used to separate code that should run
# only when the file is executed directly, not when it's
# imported elsewhere.

# file: myscript.py

def greet():
    print("Hello, world!")

if __name__ == "__main__":
    greet()


# But if you do this in another file:

# # file: another.py
#
# import myscript


#  So basically...
# if __name__ == "__main__": means:
#
# "Only run this part of the code if this file
# is being run directly, not when imported."


#  When should you use it?
# Whenever you’re writing a Python script and want to:
#
# Test something
#
# Run the main function
#
# Prevent certain code from running when your
# file is imported into another file




















