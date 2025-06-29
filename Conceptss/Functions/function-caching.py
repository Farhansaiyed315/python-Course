
# Function Caching in Python (Simple Human Language)
# Function caching is a way to store the results of expensive function calls so that when you call the same function with the same inputs again, Python can just give you the stored answer instead of recalculating it.
#
# This saves time and improves performance!

# Where is it used?
# Imagine a function that takes a long time to run, like downloading something, or doing heavy calculations like:

# How it works:
# @lru_cache is a decorator that wraps your function.
#
# It keeps a cache (dictionary-like structure) of function inputs and outputs.
#
# maxsize: limits how many results to remember. None means unlimited.


def slow_function(x):
    print("Running slow_function...")
    return x * x


#  Example:

from functools import lru_cache

@lru_cache(maxsize=None)  # unlimited cache
def slow_function(n):
    print(f"Calculating for {n}...")
    return n * n

print(slow_function(10))  # This will calculate
print(slow_function(10))  # This will fetch from cache (faster)


#  Bonus: View Cache Info

print(slow_function.cache_info())

#  Real-World Use Case:
# If you're building:
#
# APIs
#
# Recursive functions like Fibonacci
#
# Data processing that repeats often
#
# Caching can supercharge performance!





















































