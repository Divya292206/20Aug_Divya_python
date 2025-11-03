#Write a Python program to print custom exceptions.

class MyError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise MyError("Number cannot be negative!")
    print("You entered:", num)

except MyError as e:
    print("Custom Exception:", e)
