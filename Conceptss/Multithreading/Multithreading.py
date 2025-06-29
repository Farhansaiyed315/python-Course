
# What is Multithreading in Python?
# Multithreading means running multiple threads (small units of a process) at the same time. It's mainly used to do multiple tasks concurrently, especially when tasks involve waiting — like downloading files, handling user input, etc.
#
# 👉 Threads share the same memory space and can run independently.


#  Why Use Multithreading?
# To make your program faster when doing I/O-bound tasks (like network calls, file read/write).
#
# To perform multiple tasks at once, like a chat app listening for messages and sending them at the same time.

# Important Module: threading
# Python has a built-in module called threading for multithreading.


# Important Methods:

# | Method             | Use                                     |
# | ------------------ | --------------------------------------- |
# | `start()`          | Starts the thread                       |
# | `join()`           | Waits for the thread to finish          |
# | `name`             | Gets the name of the thread             |
# | `current_thread()` | Tells which thread is currently running |


# GIL Alert: What is GIL?
# GIL = Global Interpreter Lock
#
# In Python, GIL allows only one thread to execute Python bytecode at a time, even on multi-core CPUs. So multithreading is not effective for CPU-bound tasks (like complex math).
#
# But it's still useful for I/O-bound tasks.


# Real-life Use Cases:
# Downloading multiple files at once
#
# Handling multiple users in a web app
#
# Running background tasks (like autosaving



# Basic Example:

import threading
import time

def task():
    for i in range(5):
        print(f"Task running in {threading.current_thread().name}")
        time.sleep(1)

# Create two threads
t1 = threading.Thread(target=task, name="Thread-1")
t2 = threading.Thread(target=task, name="Thread-2")

# Start threads
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

print("Both threads finished!")








