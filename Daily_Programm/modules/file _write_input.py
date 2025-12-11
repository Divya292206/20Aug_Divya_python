file = open("new.txt","a")

n = int(input("Enter number of students :"))

for i in range(n):
    name = input("enter your name :")
    age = input("enter your age :")
    marks = input("enter your marks :")

    file.write(f"name ={name} age ={age} mark ={marks}\n-----------------------------\n")