#function can call time ststic value aaccept but create a dyanamic value
"""def add(a,b):
    return a+b
print(add(2,3))
print(add(5,7))
print(add(10,20))"""

"""def getdata(a,b):
    print("Addition is:",a+b)

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

getdata(a,b)"""

def studdata(id,name,city):
    print("ID:",id)
    print("Name:",name)
    print("City:",city)

n = int(input("Enter number of students: "))

for i in range(n):
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    city = input("Enter City: ")
    studdata(id,name,city)

    



