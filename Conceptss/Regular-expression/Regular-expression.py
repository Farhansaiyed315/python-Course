
# What is a Regular Expression (RegEx)?
# Regular Expression is a pattern used to match text or string data.
#
# In Python, you use the re module to work with regular expressions.

# Basic Functions You’ll Use:

# | Function       | Description                                             |
# | -------------- | ------------------------------------------------------- |
# | `re.match()`   | Matches pattern **only at the beginning** of the string |
# | `re.search()`  | Searches pattern **anywhere** in the string             |
# | `re.findall()` | Returns a list of **all matches**                       |
# | `re.sub()`     | **Substitute** part of string with another string       |
# | `re.split()`   | Splits string using the regex pattern                   |

#  Example 1: match()

import re

text = "Python is fun"
result = re.match("Python", text)

print(result.group())  # Output: Python


# Example 2: search()

# text = "Learning Python is fun"
# result = re.search("Python", text)
#
# print(result.group())  # Output: Python

#  Example 3: findall()

text = "My number is 999 and my friend's is 888"
result = re.findall(r"\d+", text)

print(result)  # Output: ['999', '888']


#  Example 4: sub()

text = "Python is awesome"
result = re.sub("awesome", "powerful", text)

print(result)  # Output: Python is powerful


# Example 5: split()


text = "apple,banana,orange"
result = re.split(",", text)

print(result)  # Output: ['apple', 'banana', 'orange']


# Common Regex Patterns:

# | Pattern | Meaning                            |    |
# | ------- | ---------------------------------- | -- |
# | `.`     | Any character except newline       |    |
# | `\d`    | Digit (0-9)                        |    |
# | `\D`    | Non-digit                          |    |
# | `\w`    | Word character (a-z, A-Z, 0-9, \_) |    |
# | `\W`    | Non-word character                 |    |
# | `\s`    | Whitespace                         |    |
# | `\S`    | Non-whitespace                     |    |
# | `^`     | Start of string                    |    |
# | `$`     | End of string                      |    |
# | `*`     | 0 or more times                    |    |
# | `+`     | 1 or more times                    |    |
# | `{n}`   | Exactly n times                    |    |
# | \`      | \`                                 | OR |
# | `[...]` | Set of characters                  |    |
# | `( )`   | Grouping                           |    |





#  Sample Task (with Solution):
# Find all emails in a given text:


import re

text = "My email is test@example.com and yours is hello@world.net"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

print(emails)
# Output: ['test@example.com', 'hello@world.net']




















































