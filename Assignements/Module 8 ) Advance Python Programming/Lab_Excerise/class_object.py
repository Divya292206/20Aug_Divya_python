# Write a Python program to create a class and access the properties of the class using an object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Creating an object of the Person class
person1 = Person("Alice", 30)   
person1.display_info()  # Accessing the method to display properties
