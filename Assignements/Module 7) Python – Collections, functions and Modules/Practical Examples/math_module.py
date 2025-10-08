#) Write a Python program to demonstrate the use of functions from the math module.

import math

def calculate_square_root(number):
    return math.sqrt(number)

def calculate_factorial(number):
    return math.factorial(number)

# Example usage
num = 16
print(f"The square root of {num} is: {calculate_square_root(num)}")
num = 5
print(f"The factorial of {num} is: {calculate_factorial(num)}")
