#Write a Python program to create a parameterized function that takes two arguments and prints their sum.

def add_numbers(a, b):  # Define a function that takes two parameters
    return a + b  # Return the sum of the two parameters

# Example usage
num1 = 5
num2 = 10
result = add_numbers(num1, num2)  # Call the function with two arguments

print(f"The sum of {num1} and {num2} is: {result}")  # Print the result