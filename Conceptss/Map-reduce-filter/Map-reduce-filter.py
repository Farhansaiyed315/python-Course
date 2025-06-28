
# What is map() in Python?
# The map() function is used to apply a function
# to each item in a list (or any iterable).
#
# It’s like saying:
#
# “Hey Python, go apply this function to every item in
# the list and give me the new list.”


# What does map() do?
# Takes two inputs:
# 👉 A function (can be a lambda or normal function)
# 👉 An iterable (like a list, tuple, etc.)
#
# It returns a map object, which you can convert into
# a list using list().

# map(function, iterable)

numbers = [1, 2, 3, 4]

# Square each number
result = map(lambda x: x**2, numbers)

# Convert to list to see result
print(list(result))  # Output: [1, 4, 9, 16]

# In simple words:
# map() helps us to do something to every item in a list without writing a loop.
#
# It’s like shortcutting this:

squares = []
for x in numbers:
    squares.append(x**2)


# Imagine you have a list of prices in rupees and want to
# convert them to dollars (just an example):


# rupees = [100, 200, 300]
# dollars = list(map(lambda x: x / 83, rupees))
# print(dollars)





#       REDUCE-------------------------------------------------

#  When to use:
# Summing up numbers
#
# Multiplying values
#
# Finding max/min (custom logic)
#
# Combining strings, etc.




#  What is reduce() in Python?
# The reduce() function is used to reduce (or combine)
# all items in a list into one single value.
#
# Think of it like: "Combine everything step by step using a function."

# to use reduce() you need to import it:
from functools import reduce

numbers = [1, 2, 3, 4]

# Add all numbers
result = reduce(lambda x, y: x + y, numbers)
print(result)




#                        Filter

#
# What is filter() in Python?
# The filter() function is used to filter out items from a list (or any iterable) based on a condition.
#
# Think of it like: “Show me only the items that match this condition.”


# Simple Example:

numbers = [1, 2, 3, 4, 5, 6]

# Filter even numbers
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))  # Output: [2, 4, 6]


# Another Example – Filter names that start with "A":

names = ["Ali", "Farhan", "Ayaan", "Zaid"]

result = filter(lambda name: name.startswith("A"), names)
print(list(result))  # Output: ['Ali', 'Ayaan']


 #  In easy words:

 # | Feature  | Description                             |
# | -------- | --------------------------------------- |
# | Purpose  | Keep only those items that match a rule |
# | Returns  | A filter object → Convert to list()     |
# | Function | Must return `True` or `False`           |


#  Real-life Example:
# You have a list of marks and want to get only passing students (marks >= 33):

# marks = [12, 45, 67, 30, 90]
#
# passed = list(filter(lambda x: x >= 33, marks))
# print(passed)  # Output: [45, 67, 90]

















