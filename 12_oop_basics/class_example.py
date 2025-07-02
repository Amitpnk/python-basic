# class_example.py
# Demonstrates how to define and use a simple class

class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# Create objects
person1 = Person("Amit", 30)
person2 = Person("Swetha", 6)

# Call method
person1.introduce()
person2.introduce()
