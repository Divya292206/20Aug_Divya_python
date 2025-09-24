# #string[start:end:step]


# # Reverse a string using slicing
# text = "hello"
# reversed_text = text[::-1]
# print("Original:", text)
# print("Reversed:", reversed_text)

# # Reverse a string using a loop
# text = "hello"
# reversed_text = ""
# for char in text:
#     reversed_text = char + reversed_text  # put character in front
# print("Reversed:", reversed_text)

# # Reverse a string using reversed() function
# text = "hello"
# reversed_text = "".join(reversed(text))
# print("Reversed:", reversed_text)

import time

text = "hello" * 1000000  # long string

# Slicing
start = time.time()
_ = text[::-1]
print("Slicing:", time.time() - start)

# Loop
start = time.time()
rev = ""
for char in text:
    rev = char + rev
    print("Loop:", time.time() - start)

# Reversed + join
start = time.time()
_ = "".join(reversed(text))
print("reversed() + join:", time.time() - start)

