
# The shutil module in Python is part of the standard library and is used for file and directory operations. It stands for "shell utilities" and makes it easy to automate file management tasks like copying, moving, deleting, and archiving.


# Commonly Used shutil Functions

# | Function                                           | Description                                                 |
# | -------------------------------------------------- | ----------------------------------------------------------- |
# | `shutil.copy(src, dst)`                            | Copies file from `src` to `dst` (keeps file content only)   |
# | `shutil.copy2(src, dst)`                           | Same as `copy()` but also copies metadata (like timestamps) |
# | `shutil.copytree(src, dst)`                        | Copies entire directory (with subdirs and files)            |
# | `shutil.move(src, dst)`                            | Moves file or directory                                     |
# | `shutil.rmtree(path)`                              | Deletes entire directory tree (⚠️ Be careful!)              |
# | `shutil.disk_usage(path)`                          | Returns total, used, and free disk space                    |
# | `shutil.make_archive(base_name, format, root_dir)` | Creates an archive (`.zip`, `.tar`, etc.)                   |



# Copying a File

import shutil

shutil.copy("data.txt", "backup/data.txt")  # Just copies content


#  Moving a File

shutil.move("old_folder/report.pdf", "new_folder/report.pdf")


#   Deleting a Folder

shutil.rmtree("temporary_folder")


#  Creating a Zip Archive

shutil.make_archive("backup", "zip", "my_folder")  # Creates backup.zip of my_folder


# Checking Disk Space

usage = shutil.disk_usage("/")
print(f"Total: {usage.total}, Used: {usage.used}, Free: {usage.free}")


# Summary
# shutil = shell utility module.
#
# Use it when working with files/folders programmatically.
#
# It’s like Python doing file operations you normally do in File Explorer.












