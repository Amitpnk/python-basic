# variables.py
# Demonstrates variables and basic data types in Python

# 🟦 String (text)
name = "Amit"
language = 'Python'

# 🔢 Integer and Float (numbers)
age = 30
height_cm = 175.5

# ✅ Boolean (True or False)
is_developer = True
has_pet = False

# 🧪 Type Checking
print("📌 Data Types:")
print(f"name: {type(name)}")
print(f"age: {type(age)}")
print(f"height_cm: {type(height_cm)}")
print(f"is_developer: {type(is_developer)}")

# 🧠 Dynamic Typing: You can change variable types on the fly
age = "thirty"  # Now it's a string!
print(f"\nAfter change, age: {age} ({type(age)})")

# ➕ Basic Operations
print("\n📌 Basic Usage:")
print(f"My name is {name} and I am learning {language}.")
print(f"I am {height_cm} cm tall.")
print(f"Am I a developer? {is_developer}")
