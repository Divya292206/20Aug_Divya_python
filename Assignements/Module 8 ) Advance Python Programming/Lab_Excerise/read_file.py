# Program to read a file and print its data on the console

# Open the file in read mode
file = open("output.txt", "r")

# Read the data from the file
data = file.read()

# Print the data on the console
print("File content:")
print(data)

# Close the file
file.close()

