a = input("Enter Number1 :")
b = input("Enter Number2 :")

print(f"Original value : a = {a} b = {b}")

temp = a
a = b
b = temp

print(f"Swap value : a = {a} b = {b}")