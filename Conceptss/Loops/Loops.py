

#  Two Main Types of Loops in Python
# 1. for loop – Used when you know how many times to repeat

# Example: Print numbers from 1 to 5
for i in range(1, 6):
    print(i)


# while loop – Used when you want to repeat until something happens

# Example: Print numbers until 5
i = 1
while i <= 5:
    print(i)
    i += 1


# break and continue
# break – exit the loop early

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# continue – skip this loop round, go to next

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# Quick Real-Life Example

names = ["Farhan", "Ayaan", "Sara"]
for name in names:
    print("Hello", name)


# | Type       | When to Use                         |
# | ---------- | ----------------------------------- |
# | `for`      | When you know how many times        |
# | `while`    | When you repeat *until* a condition |
# | `break`    | To stop the loop completely         |
# | `continue` | To skip current loop and go next    |


# Some Advanced but Useful Loop Tricks

# Nested Loops
# Loops inside loops — mostly used in 2D data like matrix or tables

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")



# else with Loops
# Yes, for and while can have
# an else block that runs only if the loop doesn't break.

for i in range(5):
    print(i)
else:
    print("Loop finished without break")


for i in range(5):
    if i == 3:
        break
else:
    print("This will NOT run")





# Using enumerate()
# Gives index + value while looping

names = ["Farhan", "Ayaan", "Sara"]
for index, name in enumerate(names):
    print(index, name)




# Using zip()
# Used to loop through two (or more) lists together

names = ["Farhan", "Ayaan"]
ages = [20, 21]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")