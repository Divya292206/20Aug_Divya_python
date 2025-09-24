# list = ['apple','banana','mango']

# #search = input("enter the fruit :")
# search_item = 'mango'

# for fruit in list:
#     if fruit == search_item:
#         print(fruit)


# List of fruits
list1 = ['apple', 'banana', 'mango']

# String to search
search_item = 'mango'

# Loop through the list
found = False
for fruit in list1:
    if fruit == search_item:
        print(f"'{search_item}' found in the list!")
        found = True
        break

if not found:
    print(f"'{search_item}' not found in the list.")
