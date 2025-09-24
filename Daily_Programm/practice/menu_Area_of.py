"""print("---------------Menu-------------------")
print("1. Area of Circle")
print("2. Area of Rectangle")
print("3. Area of Triangle")
print("4. Exit")

choice = int(input("Enter your choice :"))

if choice == 1:
    r = float(input("Enter Area of circle:"))
    area = 3.14*r*r
    print("Area of Circle is :",area)

elif choice == 2:
    l = float(input("Enter Length of Rectangle:"))
    b = float(input("Enter Breadth of Rectangle:"))
    area = l*b
    print("Area of Rectangle is :",area)

elif choice == 3:
    l = float(input("Enter Height of Triangle:"))
    b = float(input("Enter Base of Triangle:"))
    area = 0.5*l*b
    print("Area of Triangle is :",area)

elif choice == 4:
    exit()
    

else:
    print("Invalid choice")


"""

"""import math

while True:
    print("\n--- Area Calculation Menu ---")
    print("1. Area of Circle")
    print("2. Area of Rectangle")
    print("3. Area of Square")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        r = float(input("Enter radius of the circle: "))
        area = math.pi * r * r
        print(f"Area of Circle = {area:.2f}")

    elif choice == '2':
        length = float(input("Enter length of the rectangle: "))
        breadth = float(input("Enter breadth of the rectangle: "))
        area = length * breadth
        print(f"Area of Rectangle = {area:.2f}")

    elif choice == '3':
        side = float(input("Enter side of the square: "))
        area = side * side
        print(f"Area of Square = {area:.2f}")

    elif choice == '4':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1 to 4.")
"""

