"""
A simple program to calculate the area of a rectangle
following PEP 8 guidelines (indentation, comments, variables).
"""

# Define the function to calculate area
def calculate_area(length, width):
    area = length * width    # Formula for area
    return area


# Main program (runs immediately when file is executed or imported)
# Define variables with descriptive names
rectangle_length = 5.0
rectangle_width = 3.0

# Calculate area using the function
rectangle_area = calculate_area(rectangle_length, rectangle_width)

# Print the result
print(f"The area of the rectangle is: {rectangle_area}")
