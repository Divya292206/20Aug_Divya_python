year = int(input("Enter a year :"))

if(year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap yaer".formate(year))
elif(year % 4 == 0) and (year % 100 != 0):
    print("{0} is leap year".formate(year))
else:
    print("{0} is not a leap yaer ".formate(year))