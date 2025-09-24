#using dictionary to take input from user key and value wise


user_info = {}
n = int(input("Enter number of users: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_info[key] = value  

print(user_info)


    
