#Slicing a tuple to access ranges of elements. 

# my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90)
# print(my_tuple[2:5])  # Elements from index 2 to 4
# print(my_tuple[:4])   # Elements from start to index 3
# print(my_tuple[5:])   # Elements from index 5 to end
# print(my_tuple[-5:-2]) # Elements from index -5 to -3
# print(my_tuple[:])    # All elements
# print(my_tuple[::-1]) # All elements in reverse order
# print(my_tuple[::2]) # Every second element

tuple = ('D','I','V','Y','A')
#print(tuple[::-1])

# Write a Python program to access alternate values between index 1 and 5 in a tuple. 
print(tuple[1:6:2])
