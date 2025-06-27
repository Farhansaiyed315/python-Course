
# In Python, enumerate() is a built-in function
# that adds a counter to an iterable (like a list, tuple,
# or string) and returns it as an enumerate object
# (which is an iterator of tuples).



# enumerate(iterable, start=0)

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

#  Starting from a Different Index:
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

    #  Convert to List or Tuple:

    list(enumerate(fruits))
    # Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

    tuple(enumerate(fruits))
    # Output: ((0, 'apple'), (1, 'banana'), (2, 'cherry'))


# Use Case in Coding (Useful in Loops):

students = ['Ali', 'Farhan', 'Zoya']

for roll_no, name in enumerate(students, start=101):
    print(f"Roll No: {roll_no} - Name: {name}")


# enumerate() is helpful when you need both index and value from a list or any iterable.
#
# It's cleaner and more Pythonic than using range(len(...)).





















































