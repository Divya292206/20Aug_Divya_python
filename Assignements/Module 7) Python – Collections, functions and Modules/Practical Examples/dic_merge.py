#Write a Python program to merge two lists into one dictionary using a loop.

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

merged_dict = {}
for i in range(len(list1)):
    merged_dict[list1[i]] = list2[i]
print(merged_dict)

