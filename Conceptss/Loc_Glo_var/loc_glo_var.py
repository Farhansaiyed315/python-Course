
#  Global Variable
# A variable that’s declared outside any function.
#
# It can be accessed and used anywhere in the code,
# even inside functions (if you don’t overwrite it).

x = 10  # Global variable

def show():
    print("Inside function:", x)

show()
print("Outside function:", x)

#  Local Variable
# A variable that’s declared inside a function.
#
# It only works inside that function. It doesn’t affect or access global variables unless specified.
#


def demo():
    x = 5  # Local variable
    print("Inside function:", x)

demo()
print("Outside function:", x)  # ❌ Error!


x = 100

def test():
    x = 50  # This is local
    print("Inside:", x)

test()
print("Outside:", x)

# If you want to change a global variable
# inside a function, use the global keyword.
x = 20

def modify():
    global x
    x = 99

modify()
print("After modifying:", x)


# | Feature        | Global Variable       | Local Variable           |
# | -------------- | --------------------- | ------------------------ |
# | Declared       | Outside all functions | Inside a function        |
# | Scope          | Entire program        | Only inside the function |
# | Accessed in fn | Yes                   | No (outside)             |
# | Modified in fn | Only using `global`   | Normal assignment        |












