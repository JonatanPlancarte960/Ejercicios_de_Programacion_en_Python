# Decorator - Decorator function
# Modify the behavior of a function or method

# This is decorator
def decorator(function):
    def new_function(*args, **kwargs):
        print("Decorator function")
        return function(*args, **kwargs)
    return new_function

@decorator
def sum(a, b):
    return a + b

print(sum(5, 3))

print("--------------------")

# Define a decorator

def my_decorator(function):
    def internal_function():
        print("Internal function")
        function()
    return internal_function

@my_decorator
def first_function():
    print("First Function")

first_function()

print("-----------------------")

import logging

def logger(function):
    def wrapper(*args, **kwargs):
        logging.info(f"Running {function.__name__}")
        result = function(*args, **kwargs)
        logging.info(" {function.__name__} finished with this result {result}")
        return result
    return wrapper

@logger
def sum(a, b):
    return a + b

print(sum(1, 3))