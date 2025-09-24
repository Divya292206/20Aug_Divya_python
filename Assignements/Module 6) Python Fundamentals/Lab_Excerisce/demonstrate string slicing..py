# Write a Python program to demonstrate string slicing.

text = "Python Programming"

# 1. Slice from index 0 to 6 (0 included, 6 excluded)
print(f"text[0:6] -> {text[0:6]}")

# 2. Slice from beginning to index 6
print(f"text[:6] -> {text[:6]}")

# 3. Slice from index 7 to end
print(f"text[7:] -> {text[7:]}")

# 4. Slice full string
print(f"text[:] -> {text[:]}")

# 5. Negative index slicing
print(f"text[-11:-1] -> {text[-11:-1]}")

# 6. Slice with step (every 2nd character)
print(f"text[::2] -> {text[::2]}")

# 7. Reverse string using slicing
print(f"text[::-1] -> {text[::-1]}")


