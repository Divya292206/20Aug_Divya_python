# Write a Python program to handle file exceptions and use the finally block for closing the file.

try:
    file = open("output.txt", "r")   # Try to open the file
    data = file.read()
    print("File content:")
    print(data)

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: You don't have permission to read this file.")

finally:
    # This block always runs, even if an error occurs
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("File was never opened, so nothing to close.")
