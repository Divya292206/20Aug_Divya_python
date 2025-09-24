# Write a Python program to check if a number is prime using if-else

num = int(input("Enter a number: "))

if num > 1:
    # Check divisibility
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        # This else belongs to the for loop, not the if
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
