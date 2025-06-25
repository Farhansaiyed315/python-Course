# What is a List in Python?
# A list is like a container or a box that holds multiple items — like numbers, words, or even other boxes (lists inside lists 😮).
#
# You can:
#
# Store many values in one variable
#
# Change them later (lists are mutable)
#
# Mix different data types (string, int, float, etc.)

# How to Create a List

my_list = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

# Accessing List Items
print ("here we are accesing the values")

print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[-1]) # cherry (negative = count from end)


# Looping Through a List
print("loop--------------------------------")
for fruit in fruits:
    print(fruit)

    list2 = ["farhan","faizan","fezal jii "]

    print(list2[-1])


    # | Method             | Use Case                      |
    # | ------------------ | ----------------------------- |
    # | `append()`         | Add item at the end           |
    # | `insert(index, x)` | Add item at specific position |
    # | `remove(x)`        | Remove specific item          |
    # | `pop()`            | Remove last item              |
    # | `sort()`           | Sort the list                 |
    # | `reverse()`        | Reverse the list              |
    # | `len()`            | Length of the list            |


    fruits.append("mango")  # Add mango
    fruits.remove("banana")  # Remove banana
    print(len(fruits))  # Count items

    # List Slicing (Grab parts of the list)

    numbers = [10, 20, 30, 40, 50]

    print(numbers[1:4])  # [20, 30, 40]
    print(numbers[:3])  # [10, 20, 30]
    print(numbers[-2:])  # [40, 50]

# Changing List Items

fruits[0] = "kiwi"
print(fruits)  # ['kiwi', 'cherry', 'mango']



# Lists can hold other lists

nested = [[1, 2], [3, 4]]
print(nested[0])     # [1, 2]
print(nested[0][1])  # 2