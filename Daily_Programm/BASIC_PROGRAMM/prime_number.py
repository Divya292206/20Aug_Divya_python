n = int(input("enter number :"))

if n > 1:
    for i in range(2,n):
        if n%1 == 0:
            print("not prime")
            break
        else:
            print("prime number")

else:
    print("not prime")

