

#  What is match-case in Python?
# It’s a pattern matching feature that lets you
# compare a value against several patterns and execute
# code based on which pattern matches.
# No break statement
value = 2

match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Default case")



# Real Life Example:

day = "Monday"

match day:
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("Weekend is near")
    case "Sunday":
        print("Holiday!")
    case _:
        print("Just another day")



# Advanced Example with Tuple:

point = (0, 1)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y-axis at y={y}")
    case (x, 0):
        print(f"X-axis at x={x}")
    case (x, y):
        print(f"Point at x={x}, y={y}")