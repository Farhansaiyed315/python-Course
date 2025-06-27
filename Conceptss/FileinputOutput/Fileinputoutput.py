
# File Input/Output in Python
# File I/O means reading from or writing
# to files stored on your computer using Python.

# | Mode  | Meaning                           |
# | ----- | --------------------------------- |
# | `'r'` | Read (default)                    |
# | `'w'` | Write (overwrites file)           |
# | `'a'` | Append (adds to file)             |
# | `'x'` | Create new file (error if exists) |
# | `'b'` | Binary mode                       |
# | `'t'` | Text mode (default)               |



# Opening a File

file = open("filename.txt", "mode")

# Writing to a File
file = open("notes.txt", "w")  # creates file if it doesn't exist
file.write("Hello, Python world!")
file.close()


# Or using with (auto closes the file):

with open("notes.txt", "w") as file:
    file.write("This is easier and safer.")


# Reading from a File

file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()


# You can also use:

file.readline()  # Reads one line
file.readlines()  # Reads all lines as a list


# Or the better way:

with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newlines


# Appending to a File

with open("notes.txt", "a") as file:
    file.write("\nAnother line added.")


#  Deleting a File (optional but useful)

import os

if os.path.exists("notes.txt"):
    os.remove("notes.txt")
else:
    print("File not found.")


#  Summary Table

# | Operation   | Code Example                          |
# | ----------- | ------------------------------------- |
# | Open file   | `open("file.txt", "r")`               |
# | Read file   | `read()`, `readline()`, `readlines()` |
# | Write file  | `write("data")`                       |
# | Append data | `open("file.txt", "a")`               |
# | Auto-close  | `with open(...) as f:`                |
# | Delete file | `os.remove("file.txt")`               |




















