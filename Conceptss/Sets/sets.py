
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


# | Method             | Description                                  | Example            |
# | ------------------ | -------------------------------------------- | ------------------ |
# | `add(item)`        | Adds a single item to the set                | `s.add(10)`        |
# | `update(iterable)` | Adds multiple items from a list, tuple, etc. | `s.update([4, 5])` |
# | `remove(item)`     | Removes the item; throws error if not found  | `s.remove(3)`      |
# | `discard(item)`    | Removes the item; no error if not found      | `s.discard(5)`     |
# | `pop()`            | Removes and returns a random item            | `s.pop()`          |
# | `clear()`          | Removes all items from the set               | `s.clear()`        |
# | `copy()`           | Returns a shallow copy of the set            | `s2 = s.copy()`    |



# Set Operations (Using Methods)

# | Method                       | Description                                   | Example                       |
# | ---------------------------- | --------------------------------------------- | ----------------------------- |
# | `union(set2)`                | Returns a new set with all elements from both | `s1.union(s2)`                |
# | `intersection(set2)`         | Returns common elements                       | `s1.intersection(s2)`         |
# | `difference(set2)`           | Elements in `s1` not in `s2`                  | `s1.difference(s2)`           |
# | `symmetric_difference(set2)` | Elements not common in both sets              | `s1.symmetric_difference(s2)` |



a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))  # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}
print(a.difference(b))  # {1, 2}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
























