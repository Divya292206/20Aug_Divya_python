#Write a Python program to calculate grades based on percentage using if-else ladder.

per = float(input("enter your percentage :"))

if per>=90:
    print("a grade")
elif per>=70:
    print("b garde")
elif per<=60:
    print("c grade")
elif per<=40:
    print("d grade")
else:
    print("fail")
