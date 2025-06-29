

# The time module in Python is used to work with time-related functions like getting the current time, pausing execution (sleep), and converting time formats. It's built-in, so you don't need to install anything—just import and use it!


#  Common Functions in time module

import time
print(time.time())  # Example: 1720000000.12345


#  time.sleep(seconds)
# Pauses the execution for the given number of seconds.

print("Start")
time.sleep(2)
print("End after 2 seconds")


# time.ctime(seconds)
# Converts seconds since epoch to a readable string.

print(time.ctime())              # Current time
print(time.ctime(1720000000))   # Convert any timestamp


# time.localtime(seconds)
# Returns a struct_time in local time.

local_time = time.localtime()
print(local_time)
print(local_time.tm_hour)  # Get only the hour


# time.strftime(format, time_object)
# Formats time into a string.

now = time.localtime()
formatted = time.strftime("%Y-%m-%d %H:%M:%S", now)
print(formatted)



# | Format Code | Meaning           |
# | ----------- | ----------------- |
# | `%Y`        | Year (e.g., 2025) |
# | `%m`        | Month (01–12)     |
# | `%d`        | Day (01–31)       |
# | `%H`        | Hour (00–23)      |
# | `%M`        | Minute (00–59)    |
# | `%S`        | Second (00–59)    |


# time.gmtime(seconds)
# Same as localtime() but returns UTC time.

print(time.gmtime())


# time.time_ns()
# Gives the current time in nanoseconds.

print(time.time_ns())  # Useful for high precision timing



#  Real-Life Example: Measure Execution Time

start = time.time()
# Do something
for i in range(1000000):
    pass
end = time.time()

print("Time taken:", end - start, "seconds")


# Summary Table

# | Function           | Use                                   |
# | ------------------ | ------------------------------------- |
# | `time.time()`      | Current time in seconds (float)       |
# | `time.sleep(x)`    | Wait for x seconds                    |
# | `time.ctime()`     | Convert seconds to readable string    |
# | `time.localtime()` | Get local time in struct\_time format |
# | `time.strftime()`  | Format time nicely as a string        |
# | `time.gmtime()`    | Get UTC time in struct\_time          |
# | `time.time_ns()`   | High-precision time in nanoseconds    |


















































