# Program to check the current position of the file cursor

# Open the file in write mode
file = open("sample.txt", "w")

# Write some data into the file
file.write("Hello, this is a test file.")

# Check the current position of the file cursor
position = file.tell()

# Print the cursor position
print("Current file cursor position:", position)

# Close the file
file.close()
