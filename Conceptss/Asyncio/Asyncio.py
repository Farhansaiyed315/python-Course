
#  What is asyncio?
# asyncio is a Python module used for writing asynchronous code – that means you can run multiple tasks at once without waiting for one to finish before starting the next.
#
# 👉 Think of it like:
#
# Instead of standing in a line to do 3 tasks one-by-one (sync), you send WhatsApp messages to 3 friends and each replies whenever they’re ready (async).


# Why Use asyncio?
# To handle I/O-bound operations efficiently (like downloading files, API calls, database reads).
#
# Improves performance without using threads or processes.
#
# Perfect for network apps, bots, or anything where waiting is involved.

# Key Terms in asyncio

# | Term         | Meaning                                              |
# | ------------ | ---------------------------------------------------- |
# | `async def`  | Defines an asynchronous function                     |
# | `await`      | Tells Python to **wait** for an async task to finish |
# | `event loop` | Controls and runs all async tasks                    |
# | `coroutine`  | A special function that can pause and resume         |


import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(2)  # Pause for 2 seconds (non-blocking)
    print("World")

async def main():
    await say_hello()

asyncio.run(main())


# Run Multiple Tasks Together:

import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 done")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 done")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

# Bonus Tip (when you're ready):
# If you're combining asyncio with things like APIs or databases, you can use:
#
# aiohttp for async HTTP requests
#
# aiosqlite for async database access








