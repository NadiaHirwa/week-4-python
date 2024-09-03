class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old, and I am {self.gender}.")

# Prompting the user to input the person's details
name = input("Enter the person's name: ")
age = int(input("Enter the person's age: "))
gender = input("Enter the person's gender: ")

# Creating an instance of the Person class with user input
person = Person(name=name, age=age, gender=gender)

# Calling the introduce method to display the person's information
person.introduce()
