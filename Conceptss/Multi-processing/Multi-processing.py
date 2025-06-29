
# What is Multiprocessing in Python?
# Multiprocessing means running multiple processes at the same time, each with its own Python interpreter and memory space.
#
# 📌 Use it when your task is CPU-bound (like complex math, image processing, etc.) and you want to fully use all CPU cores 💪.


# Difference between Threading vs Multiprocessing


# | Feature  | Threading 🧵              | Multiprocessing 🧠               |
# | -------- | ------------------------- | -------------------------------- |
# | Use Case | I/O-bound tasks           | CPU-bound tasks                  |
# | Speed    | Slower for CPU-heavy      | Faster for CPU-heavy             |
# | Memory   | Shared memory             | Separate memory                  |
# | Crashes  | One thread crashes, risky | One process crashes, others safe |



#  Using the multiprocessing module

import multiprocessing

def worker():
    print("Worker process running...")

if __name__ == "__main__":
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()


#  Run Multiple Processes

import multiprocessing

def show(i):
    print(f"Process {i} running...")

if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=show, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

#  Example with CPU work (math heavy task)

import multiprocessing

def square(n):
    print(f"Square of {n} is {n * n}")

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    procs = []

    for n in nums:
        p = multiprocessing.Process(target=square, args=(n,))
        procs.append(p)
        p.start()

    for p in procs:
        p.join()


#  Built-in Tools in multiprocessing:
#
# | Tool      | Use                                        |
# | --------- | ------------------------------------------ |
# | `Process` | Run a function in a separate process       |
# | `Pool`    | Run multiple processes easily with mapping |
# | `Queue`   | Share data between processes safely        |
# | `Lock`    | Avoid race conditions                      |



#  Using Pool (simpler method for multiple inputs)

from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == "__main__":
    with Pool() as pool:
        result = pool.map(square, [1, 2, 3, 4, 5])
        print(result)


#  Real-Life Use Cases:
# Processing images in bulk
#
# Data analysis
#
# Machine learning model training
#
# Video/audio processing





















































