# inheritance.py
# Demonstrates class inheritance in Python

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")

# Derived class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

# Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()
cat.speak()
