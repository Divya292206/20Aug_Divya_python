# Write a Python program to check if a person is eligible to donate blood using a nested if.

Age = int(input("enter your age :"))

if Age>=18:
    Weight = int(input("enter your weight :"))
    if Weight>=50:
        print("you are eligible to donate blood")
    else:
        print("you are not eligible to donate blood")
else:
    print("you are not eligible to donate blood")
    

