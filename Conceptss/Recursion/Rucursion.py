
# What is Recursion?
# Recursion means a function calling itself to
# solve smaller parts of a bigger problem.
#
# 🧠 Think of it like:
#
# Breaking down a big task into smaller and smaller
# tasks — until it's so small that it’s super easy to solve.

# Every Recursive Function Must Have:
# Base Case – when to stop recursion
#
# Recursive Case – when to keep calling itself


#  When to Use Recursion
# Problems that can be broken into smaller subproblems
#
# Tree traversal (binary trees, decision trees)
#
# Backtracking (like Sudoku, N-Queens)
#
# Divide and conquer (Merge Sort, Quick Sort)
#
# Mathematical problems (factorial, power, GCD)

# | ✅ Pros                        | ❌ Cons                          |
# | ----------------------------- | ------------------------------- |
# | Easy to write and understand  | Risk of stack overflow          |
# | Cleaner and shorter code      | Slower than iteration           |
# | Great for tree/graph problems | Uses more memory (stack frames) |



def factorial(n):
    if n == 0:               # base case
        return 1
    else:
        return n * factorial(n - 1)  # recursive call

print(factorial(5))  # Output: 120


#  What's Happening?
# factorial(5) calls factorial(4)
#
# factorial(4) calls factorial(3)
#
# ...
#
# Until factorial(0) returns 1
#
# Then it multiplies everything back up

 # factorial(5)
# => 5 * factorial(4)
# => 5 * 4 * factorial(3)
# => 5 * 4 * 3 * factorial(2)
# => 5 * 4 * 3 * 2 * factorial(1)
# => 5 * 4 * 3 * 2 * 1 * factorial(0)
# => 5 * 4 * 3 * 2 * 1 * 1 = 120

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8


# Be Careful:
# Too much recursion can cause a stack overflow error
#
# Recursive code is clean but not always efficient
#
# Use loops when performance matters (like in Fibonacci)

# Recap (write this in your notes):
# Recursion = function calling itself
#
# Always have:
#
# Base case (stop condition)
#
# Recursive case (keep going)
#
# Useful for problems like:
#
# Factorial
#
# Fibonacci
#
# Tree/graph traversal


#   | Type                   | Example                                          | Explanation                            |
# | ---------------------- | ------------------------------------------------ | -------------------------------------- |
# | **Direct Recursion**   | A function calls **itself**                      | `f() -> f()`                           |
# | **Indirect Recursion** | A calls B, B calls A                             | `f() -> g() -> f()`                    |
# | **Tail Recursion**     | Recursive call is the **last thing** in function | Python doesn't optimize tail recursion |
# | **Head Recursion**     | Recursive call is **before** any operation       | `return f(n-1) + something`            |


#  Real-World Recursion Examples
# 📁 1. Sum of Natural Numbers

def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

print(sum_n(5))  # 15

# Best Practices
# Always define a base case
#
# Avoid too deep recursion (Python default limit is 1000 calls)
#
# Use sys.setrecursionlimit() to increase limit if needed, but ⚠️ risky!








