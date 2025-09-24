while True:
    
    print("--------------Menu---------------")
    print("Enter Area Of Circle :")
    print("Enter Area Of Rectangle :")
    print("Enter Area Of Square :")
    print("Exit")

    choice = input("Enter Your choice(1-4) :")

    if choice == '1':
        r = float(input("Enter Area Of Radius :"))
        Area = 3.14 * r * r
        print("Area of Circle Is :",Area)

    elif choice == '2':
        l = float(input("Enter Area of Length :"))
        w = float(input("Enter Area Of Width :"))
        Area = l*w
        print("Area of Rectangle is :",Area)

    elif choice == '3':
        side = float(input("Enter Side of square :"))
        Square = side * side
        print("Square is :",Square)

    elif choice == '4':
        print("Exit programm!!")
        exit()
    
    else:
        print("Invaild choice !!")

        



