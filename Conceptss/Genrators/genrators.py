

# What are Generators in Python?
# Generators are a special type of function that returns values one at a time using the yield keyword instead of returning all values at once like return.
#
# They are memory-efficient and useful when you’re dealing with large data.
#



# 💡 Why use Generators?
# Save memory: They don’t store all values in memory.
#
# Faster: Values are generated only when needed (on the fly).
#
# Perfect for loops: Easily used in for loops or any iterable situation

# Generator vs Normal Function

# | Normal Function             | Generator Function                     |
# | --------------------------- | -------------------------------------- |
# | Uses `return`               | Uses `yield`                           |
# | Returns once                | Can return multiple times (one by one) |
# | Stores everything in memory | Only one value at a time in memory     |

#  Summary Points (for exam or revision):
# Generator is a function that uses yield to return values one at a time.
#
# More memory efficient than lists.
#
# Ideal for working with large datasets.
#
# Can be used in loops or converted to lists using list(gen).
#
# Generator expressions are like list comprehensions but use (



# How to create a Generator?

# Using yield in a function
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

for value in gen:
    print(value)


# Real Example: Generator for Even Numbers

def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)


# Generator Expression (Shortcut)
# Just like list comprehensions but with () instead of [].
#

gen = (x*x for x in range(5))

for val in gen:
    print(val)








