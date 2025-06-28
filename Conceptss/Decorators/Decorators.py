

# What are Decorators?
# In Python, decorators are a way to add extra functionality to a function without changing its actual code.
#
# Think of it like adding a filter on a photo 📸 — the original photo stays the same, but it looks different because of the filter.

# When to Use Decorators?
# Logging what a function does
#
# Timing how long it takes
#
# Authentication checks
#
# Access control
#
# Caching results



#  Example Without Decorator:

def say_hello():
    print("Hello, Farhan!")

say_hello()


#  Now Add a Decorator

def my_decorator(func):
    def wrapper():
        print("Before function runs...")
        func()
        print("After function runs...")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, Farhan!")

say_hello()


# Real-World Example (Logging Decorator)


def log_function_call(func):
    def wrapper():
        print(f"Calling {func.__name__}")
        func()
        print(f"Finished {func.__name__}")
    return wrapper

@log_function_call
def process_data():
    print("Processing data...")

process_data()


# Bonus: Decorators with Arguments

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hi {name}!")

greet("Farhan")











