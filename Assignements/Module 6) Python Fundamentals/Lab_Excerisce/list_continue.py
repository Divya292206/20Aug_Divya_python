#Write a Python program to skip 'banana' in a list using the continue statement. 

List1 = ['apple', 'banana', 'mango'] 

item = 'banana'

for fruit in List1:
    if item == fruit:
        continue
    print(fruit)