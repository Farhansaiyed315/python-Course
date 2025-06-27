
#  What is if-else?
# if-else is used to make decisions in your code.
#
# Python reads conditions from top to bottom and runs the code
# block where the condition is True.

# if condition:
#     # code if condition is True
# else:
#     # code if condition is False


age = 18

if age >= 18:
    print("You can vote.")
else:
    print("You are too young to vote.")


marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")


# Example with Boolean:
is_raining = True

if is_raining:
    print("Take an umbrella ☔")
else:
    print("Enjoy the sunshine ☀️")


# Logical Example:
temp = 30

if temp > 35:
    print("It's very hot 🥵")
elif temp > 20 and temp <= 35:
    print("Nice weather 😎")
else:
    print("It's cold 🥶")


# Python Short-hand if-else (Ternary Operator)
# In Python, you can write an if-else statement in a
# single line using a short-hand format called the ternary
# operator.

# value_if_true if condition else value_if_false


age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)

a = 10
b = 20
larger = a if a > b else b
print(larger)


x = 5
print("Even") if x % 2 == 0 else print("Odd")


























