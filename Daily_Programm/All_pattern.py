def star_triangle():
    print("\n1. Star Triangle")
    rows = 5
    for i in range(1, rows+1):
        print("*" * i)

def number_triangle():
    print("\n2. Number Triangle")
    rows = 5
    for i in range(1, rows+1):
        for j in range(1, i+1):
            print(j, end="")
        print()

def inverted_star():
    print("\n3. Inverted Star Triangle")
    rows = 5
    for i in range(rows, 0, -1):
        print("*" * i)

def inverted_number():
    print("\n4. Inverted Number Triangle")
    rows = 5
    for i in range(rows, 0, -1):
        for j in range(1, i+1):
            print(j, end="")
        print()

def star_pyramid():
    print("\n5. Star Pyramid")
    rows = 5
    for i in range(rows):
        print(" "*(rows-i-1) + "*"*(2*i+1))

def number_pyramid():
    print("\n6. Number Pyramid")
    rows = 5
    for i in range(1, rows+1):
        print(" "*(rows-i), end="")
        for j in range(1, i+1):
            print(j, end="")
        for j in range(i-1, 0, -1):
            print(j, end="")
        print()

def diamond():
    print("\n7. Diamond Pattern")
    rows = 5
    for i in range(rows):
        print(" "*(rows-i-1) + "*"*(2*i+1))
    for i in range(rows-2, -1, -1):
        print(" "*(rows-i-1) + "*"*(2*i+1))

def alphabet_pattern():
    print("\n8. Alphabet Pattern")
    rows = 5
    ch = 65
    for i in range(rows):
        for j in range(i+1):
            print(chr(ch), end=" ")
            ch += 1
        print()

def floyd():
    print("\n9. Floyd's Triangle")
    rows = 5
    num = 1
    for i in range(1, rows+1):
        for j in range(1, i+1):
            print(num, end=" ")
            num += 1
        print()

def hollow_square():
    print("\n10. Hollow Square")
    n = 5
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def pascal():
    print("\n11. Pascal's Triangle")
    rows = 5
    for i in range(rows):
        print(" " * (rows - i), end="")
        num = 1
        for j in range(i+1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        print()

def zero_one_triangle():
    print("\n12. 0-1 Triangle")
    rows = 5
    for i in range(1, rows+1):
        for j in range(1, i+1):
            print("1" if (i+j)%2==0 else "0", end=" ")
        print()

def butterfly():
    print("\n13. Butterfly Pattern")
    rows = 5
    for i in range(1, rows+1):
        print("*" * i + " " * (2*(rows-i)) + "*" * i)
    for i in range(rows, 0, -1):
        print("*" * i + " " * (2*(rows-i)) + "*" * i)

def hollow_diamond():
    print("\n14. Hollow Diamond")
    rows = 5
    for i in range(rows):
        print(" "*(rows-i-1) + "*" + " "*(2*i-1) + ("*" if i>0 else ""))
    for i in range(rows-2, -1, -1):
        print(" "*(rows-i-1) + "*" + " "*(2*i-1) + ("*" if i>0 else ""))

def hourglass():
    print("\n15. Hourglass Pattern")
    rows = 5
    for i in range(rows, 0, -1):
        print(" "*(rows-i) + "*"*(2*i-1))
    for i in range(2, rows+1):
        print(" "*(rows-i) + "*"*(2*i-1))


# Run all patterns
star_triangle()
number_triangle()
inverted_star()
inverted_number()
star_pyramid()
number_pyramid()
diamond()
alphabet_pattern()
floyd()
hollow_square()
pascal()
zero_one_triangle()
butterfly()
hollow_diamond()
hourglass()
