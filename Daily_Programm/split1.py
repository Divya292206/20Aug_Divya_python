"""text = "I love Python"
print(text.split())

# Output: ['I', 'love', 'Python']

text = "apple,banana,cherry"
print(text.split('a'))

# Output: ['apple', 'banana', 'cherry']

text = "one two three four"
print(text.split(' ', 2))

# Output: ['one', 'two', 'three four']

text = "2024-06-15"
print(text.split('-'))

# Output: ['2024', '06', '15']

text = "a-b-c-d-e"
print(text.split('-', 3))

# Output: ['a', 'b', 'c', 'd-e']

# Demonstrating split() with different delimiters and maxsplit
text = "name:age:city"
print(text.split(':'))

# Output: ['name', 'age', 'city']"""

fnm,lnm=input("enter frist name and last name :").split() #same datatype
print("frist name is :",fnm)
print("last name is :",lnm)
