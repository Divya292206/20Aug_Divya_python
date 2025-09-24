text = "   Hello, Python World!  "

print(f"Original string: '{text}'\n")

# 1. Convert to uppercase
print(f"Uppercase: '{text.upper()}'")

# 2. Convert to lowercase
print(f"Lowercase: '{text.lower()}'")

# 3. Remove leading and trailing spaces
print(f"Stripped: '{text.strip()}'")

# 4. Replace a substring
print(f"Replace 'Python' with 'Java': '{text.replace('Python', 'Java')}'")

# 5. Check if string starts or ends with a substring
print(f"Starts with '   Hello': {text.startswith('   Hello')}")
print(f"Ends with 'World!  ': {text.endswith('World!  ')}")

# 6. Find the position of a substring
print(f"Position of 'Python': {text.find('Python')}")

# 7. Split string into a list
words = text.strip().split()  # strip first, then split by spaces
print(f"Split into words: {words}")

# 8. Join list back into string with '-'
joined_text = '-'.join(words)
print(f"Joined with '-': '{joined_text}'")

# 9. Check string properties
print(f"Is alphabetic? {text.isalpha()}")
print(f"Is alphanumeric? {text.replace(' ', '').replace(',', '').replace('!', '').isalnum()}")
print(f"Is whitespace? {'   '.isspace()}")
