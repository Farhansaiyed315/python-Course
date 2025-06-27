
#  What is a Set in Python?
# A set is a collection of unique items.
#
# It’s unordered (means items don’t have a fixed position).
#
# It doesn’t allow duplicates.
#
# It’s mutable (you can add/remove items).

my_set = {1, 2, 3, 4}
print(my_set)


my_set = set([1, 2, 3, 4])

# | Feature       | Description                               |
# | ------------- | ----------------------------------------- |
# | Unordered     | No indexing or slicing                    |
# | No Duplicates | Repeated values get removed automatically |
# | Mutable       | You can add/remove elements               |
# | Iterable      | Can be used in loops                      |


# | Method      | Use                                    |
# | ----------- | -------------------------------------- |
# | `add()`     | Add one item                           |
# | `update()`  | Add multiple items                     |
# | `remove()`  | Remove item (gives error if not found) |
# | `discard()` | Remove item (no error if not found)    |
# | `pop()`     | Remove random item                     |
# | `clear()`   | Remove all items                       |
# | `copy()`    | Copy set                               |


# | Operation            | Symbol | Example |     |     |
# | -------------------- | ------ | ------- | --- | --- |
# | Union                | \`     | \`      | \`a | b\` |
# | Intersection         | `&`    | `a & b` |     |     |
# | Difference           | `-`    | `a - b` |     |     |
# | Symmetric Difference | `^`    | `a ^ b` |     |     |


# When to Use Sets?
# When you want to store unique items.
#
# When you need fast membership testing (in keyword).
#
# When doing mathematical operations like union, intersection.



a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # union → {1, 2, 3, 4, 5}
print(a & b)  # intersection → {3}
print(a - b)  # only in a → {1, 2}
print(a ^ b)  # unique in a or b → {1, 2, 4, 5}


for item in my_set:
    print(item)



nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = set(nums)
print(unique_nums)  # Output: {1, 2, 3, 4, 5}






























