import calendar

year = int(input("Enter your Year :"))
month = int(input("Enter Your Month :"))

cal = calendar.month(year,month)
print(cal)