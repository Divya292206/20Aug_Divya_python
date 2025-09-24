"""1 
2 3
4 5 6 
7 8 9 10"""

#using nested loop print the pattern

# n=1
# for i in range(1,5):
#     for j in range(i):
#         print(n, end=" ")
#         n+=1
#     print(" ")

# for i in range(1,6):
#     for j in range(i):
#         print(i,end = "")
#     print(" ")

# for i in range(1,6):
#     for j in range(i):
#         print(j+1,end = "")
#     print(" ")

for i in range(5 , 0 ,-1):
    print("*" * i)

for i in range(5 , 0 , -1):
    for j in range(i):
        print(i, end = "")
    print("")

for i in range(5 , 0 , -1):
    for j in range(i):
        print(j+1, end = "")
    print("")

ch = 65

for i in range(65,70):
    for j in range(i):
        print(chr(ch),end = "")
    print(" ")
