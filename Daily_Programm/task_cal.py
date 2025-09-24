x = int(input("enter your number1:"))
y = int(input("enter your number2:"))
z = int(input("enter your number3:"))
q = int(input("enter your number4:"))


if x<40 or y<40 or z<40 or q<40:
    print("fail")
else:
    total = x+y+z+q
    print("total :",total)
    per = total/4
    print("percentage :",per)

    if per>=90:od
        print("A Grade")
    elif per>=80:
        print("B Grade")
    elif per>=70:
        print("C Grade")
    elif per>=60:
        print("D Grade")
    else:
        print("Fail")
