
# What is a Dictionary in Python?
# A dictionary is like a real-life dictionary where you look up a word (key) and get its meaning (value).
#
# 💡 In Python:
# A dictionary is a collection of key-value pairs.
#
# Each key is unique
#
# The value can be of any data type


#  Real-life Use Case:
# Dictionaries are used when:
#
# You need to store data as label: value
#
# Like student info, product info, user login data, etc.



my_dict = {
    "name": "Farhan",
    "age": 25,
    "course": "BCA"
}

# | Key    | Value  |
# | ------ | ------ |
# | name   | Farhan |
# | age    | 25     |
# | course | BCA    |

print(my_dict["name"])  # Output: Farhan

my_dict["college"] = "IGNOU"

my_dict["age"] = 26

del my_dict["course"]

# | Method           | What it does                          | Example                              |
# | ---------------- | ------------------------------------- | ------------------------------------ |
# | `.keys()`        | Returns all keys                      | `my_dict.keys()`                     |
# | `.values()`      | Returns all values                    | `my_dict.values()`                   |
# | `.items()`       | Returns all key-value pairs           | `my_dict.items()`                    |
# | `.get("key")`    | Safer way to access value             | `my_dict.get("age")`                 |
# | `.update({...})` | Add or update multiple key-values     | `my_dict.update({"city": "Mumbai"})` |
# | `.pop("key")`    | Removes the key and returns its value | `my_dict.pop("age")`                 |
# | `.clear()`       | Clears everything                     | `my_dict.clear()`                    |


# Looping through dictionary:

for key, value in my_dict.items():
    print(key, "=>", value)

# Example Program:

student = {
    "name": "Farhan",
    "age": 25,
    "course": "BCA"
}

# Add new data
student["city"] = "Mumbai"

# Print all key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")



student = {"name": "Farhan", "age": 25}
print(student.get("name"))      # Output: Farhan
print(student.get("city", "N/A"))  # Output: N/A (default value)


print(student.keys())  # Output: dict_keys(['name', 'age'])




print(student.values())  # Output: dict_values(['Farhan', 25])



print(student.items())
# Output: dict_items([('name', 'Farhan'), ('age', 25)])


student.update({"city": "Mumbai"})
print(student)
# Output: {'name': 'Farhan', 'age': 25, 'city': 'Mumbai'}


age = student.pop("age")
print(age)       # Output: 25
print(student)   # Output: {'name': 'Farhan', 'city': 'Mumbai'}


student.popitem()
print(student)
# Output: {'name': 'Farhan'} (city removed)

student.clear()
print(student)  # Output: {}

# Returns a shallow copy of the dictionary.
new_student = student.copy()


keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)
# Output: {'a': 0, 'b': 0, 'c': 0}



# | Method       | Use Case Example                      |
# | ------------ | ------------------------------------- |
# | `.get()`     | Get value safely                      |
# | `.keys()`    | Get all keys                          |
# | `.values()`  | Get all values                        |
# | `.items()`   | Get all key-value pairs               |
# | `.update()`  | Add or update keys                    |
# | `.pop()`     | Remove key and return its value       |
# | `.popitem()` | Remove last item                      |
# | `.clear()`   | Delete everything                     |
# | `.copy()`    | Copy the dictionary                   |
# | `fromkeys()` | Make new dict with given keys + value |







