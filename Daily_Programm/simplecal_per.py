no1 = int(input("enter your number1:"))
no2 = int(input("enter your number2:"))
no3 = int(input("enter your number3:"))

total = no1 + no2 + no3 
print("total :",total)
per = total/3
print("percentage :",per)

if per>=90:
    print("A Grade")
elif per>=80:
    print("B Grade")
elif per>=70:
    print("C Grade")
elif per>=60:
    print("D Grade")
else:
    print("Fail")


