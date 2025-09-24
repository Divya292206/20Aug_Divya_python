#Write a Python program to count how many times each character appears in a string.

input_string = "hello world"  # Example input string
char_count = {}  # Initialize an empty dictionary to store character counts
for char in input_string:  # Iterate through each character in the string
    if char in char_count:  # If the character is already in the dictionary
        char_count[char] += 1  # Increment its count by 1
    else:
        char_count[char] = 1  # Otherwise, initialize its count to 1
print("Character counts:", char_count)  # Print the dictionary with character counts

for char,count in char_count.items():
    print(f"'{char}': {count}")

