#create a table using file handling 1*1 =1 to 10*10=100

file = open("student_table.txt","a")
n = int(input("Enter the number to print table :"))

for i in range(1,11):
    result = n*i
    file.write(f"{n} * {i} ={result}\n")
    
   




# file = open("student_table.txt","a")

# for i in range(1,11):
#     file.write(f"i ={i} ")