import re

mystr = "Hello My name is Divya"

x = re.search("divya",mystr)

print(x)

if x:
    print("Sucesss!")
else:
    print("Error!")