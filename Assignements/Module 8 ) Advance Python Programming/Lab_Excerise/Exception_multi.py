#Write a Python program to handle multiple exceptions (e.g., file not found, division by zero). 

try:
    # Trying to open a file
    file = open("myfile.txt", "r")
    number = int(input("Enter a number to divide 100 by: "))
    result = 100 / number
    print("Result:", result)

except FileNotFoundError:
    print("Error: The file was not found.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter a valid number.")

except Exception as e:
    print("Some other error occurred:", e)

else:
    print("Program executed successfully!")

finally:
    print("Program finished (finally block executed).")
