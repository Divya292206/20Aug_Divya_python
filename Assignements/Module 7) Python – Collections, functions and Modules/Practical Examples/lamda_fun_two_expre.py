#Write a Python program to create a lambda function with two expressions.

lambda_function = lambda x, y: (x + y, x * y)  # Lambda function with two expressions: sum and product

# Example usage
num1 = 5
num2 = 10
sum_result, product_result = lambda_function(num1, num2)  # Call the lambda function with two arguments
print(f"The sum of {num1} and {num2} is: {sum_result}")  # Print the sum result
print(f"The product of {num1} and {num2} is: {product_result}")  # Print the product result