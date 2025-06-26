# What is a Tuple in Python?
# A tuple is a collection of values, just like a list — but the main difference is:
#
# 🧊 Tuples are immutable, meaning you can’t change them after you create them.

# Basic Example:

my_tuple = (1, 2, 3)
print(my_tuple)


# Tuple vs List:
#
# | Feature  | Tuple               | List               |
# | -------- | ------------------- | ------------------ |
# | Syntax   | `(1, 2, 3)`         | `[1, 2, 3]`        |
# | Mutable? | ❌ No (can’t change) | ✅ Yes (can change) |
# | Faster?  | ✅ Yes (in general)  | ❌ Slower           |
# | Use case | Fixed data          | Changing data      |
#

#  Why use Tuples?
# To protect data from being changed (accidentally).
#
# They use less memory than lists.
#
# They are faster when looping or reading.

# Tuple Examples:

# Tuple with different data types
info = ("Farhan", 21, "BCA")
print(info)

# Accessing items
print(info[0])  # Output: Farhan

# Nested tuples
nested = ((1, 2), (3, 4))
print(nested[1][0])  # Output: 3

# Tuple with one element (important!)
one_item = (5,)
print(type(one_item))  # Output: <class 'tuple'>


# When to Use Tuples?
# When your data should not change (like days of the week).
#
# When you want faster performance.