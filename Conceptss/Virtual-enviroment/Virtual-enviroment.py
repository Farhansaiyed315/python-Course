#  What is a Virtual Environment in Python?
# A virtual environment in Python is like a separate
# workspace that keeps your project’s dependencies isolated
# from the rest of your system.


# Why do we need it?
# Let’s say:
#
# Project A needs Django 3.2
#
# Project B needs Django 4.0
#
# If you install both globally, it’ll mess things up.
# But if you create separate virtual environments for
# each project,
# they can live peacefully with their own versions of libraries.


# How it works?
# It creates a local folder with its own Python
# interpreter and libraries.
# This way, you can install whatever you need just for
# that project.


#  Real-World Use Case
# You’re building:
#
# One project using Flask
#
# Another using FastAPI
#
# Keep them separate using virtual environments
# so that no package conflicts happen.


# | Term         | Meaning                                        |
# | ------------ | ---------------------------------------------- |
# | `venv`       | Built-in module to create virtual environments |
# | `pip`        | Tool to install packages                       |
# | `activate`   | Starts using the virtual environment           |
# | `deactivate` | Stops using it                                 |






