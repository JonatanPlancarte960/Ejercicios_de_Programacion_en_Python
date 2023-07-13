# 1. Use the ternary operator

a, b = 5, 10

# High is equal to a if a is higher than b or else b
high = a if a > b else b
print(high)

# 2. Use enumerate
# To get the index along with the value in a loop

list_ = ["a", "b", "c"]
for index, value in enumerate(list_):
    print(f"index: {index}, value: {value}")

# 3. lambda
# Anonymous functions (no name)

sum = lambda x, y: x + y
print(sum(5, 6))

print(sum(10, 5))

# 4. Map & filter functions
# Transform and filter the elements of a list

numbers = [1, 2, 3, 4, 5, 6]

square = list(map(lambda x: x ** 2, numbers))
peers = list(filter(lambda x: x % 2 == 0, numbers))

print(square)
print(peers)

# Exercise map
"""
words = ["python", "is", "fun"]
With map function convert everything to uppercase
["PYTHON", "IS", "FUN"]
"""

words = ["python", "is", "fun"]
uppercase = list(map(lambda x: x.upper(), words))

print(uppercase)

# Exercise filter
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Use filter for odd numbers and another filter for prime numbers
"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = list(filter(lambda x: x % 2 != 0, numbers))

# The all function is used to verify that all the elements of an iterable meet a certain condition
prime = list(filter(lambda x: all(x % i != 0 for i in range(2, x)) and x > 1, numbers))

print(odd)
print(prime)