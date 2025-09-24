"""A
A B 
A B C 
A B C D"""


# for i in range(65,70):
#     for j in range(65,i+1):
#         print(chr(j),end = "")
#     print("")


"""A
B C
D E F
G H I J"""

# ch = 65
# for i in range(1,6):
#     for j in range(i):
#         print(chr(ch),end = " ")
#         ch +=1
#     print("")

 """# # # # #
      # # # #
        # # #
          # #
            #"""
 

# for i in range(5,0,-1):
#      for j in range(5-i):
#          print(" ",end = " ")
#      for k in range(i):
#          print("#",end = " ")
#      print("")# Pyramid pattern



"""5 4 3 2 1
     4 3 2 1
       3 2 1
         2 1
           1"""


for i in range(5,0,-1):
    for j in range(5-i):  
        print(" ",end = " ")
    for k in range(i):
        print(i-k,end = " ")
    print("")