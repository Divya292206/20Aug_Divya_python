#Program to create a file and print a string into the file

# Open a file in write mode
file = open("output.txt", "w")

# Print (write) a string into the file
print("Hello, this text is written into the file!", file=file)

# Close the file
file.close()

print("File created and string printed successfully!")
