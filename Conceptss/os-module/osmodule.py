
# The os module in Python lets you interact with the
# operating system. It helps you do things like:
#
# Work with files and folders (create, delete, rename, etc.)
#
# Run terminal/command-line commands
#
# Get information about your system (like current directory,
# file paths, etc.)

# How to use it?

# import os

# Commonly Used os Module Functions


# | Function                  | What it does                                                                    |
# | ------------------------- | ------------------------------------------------------------------------------- |
# | `os.name`                 | Returns the name of the OS (like `'nt'` for Windows, `'posix'` for Linux/macOS) |
# | `os.getcwd()`             | Returns the current working directory                                           |
# | `os.chdir(path)`          | Changes the current directory to `path`                                         |
# | `os.listdir(path)`        | Lists files and folders in the given path                                       |
# | `os.mkdir("folder")`      | Creates a new folder                                                            |
# | `os.makedirs("a/b/c")`    | Creates nested folders (like `mkdir -p`)                                        |
# | `os.remove("file.txt")`   | Deletes a file                                                                  |
# | `os.rmdir("folder")`      | Removes an empty folder                                                         |
# | `os.rename("old", "new")` | Renames a file or folder                                                        |
# | `os.path.exists("file")`  | Checks if a file or folder exists                                               |
# | `os.path.isfile("file")`  | Checks if it's a file                                                           |
# | `os.path.isdir("folder")` | Checks if it's a folder                                                         |


import os

# Get current working directory
print("Current directory:", os.getcwd())

# Create a folder
os.mkdir("test_folder")

# Check if folder exists
if os.path.exists("test_folder"):
    print("Folder created successfully!")

# Rename folder
os.rename("test_folder", "my_folder")

# List all files/folders
print("Files in current dir:", os.listdir())

# Delete the folder
os.rmdir("my_folder")
print("Folder deleted!")



# If you're working with file paths, use:

os.path.join("folder", "file.txt")







































