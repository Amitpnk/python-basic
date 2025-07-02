# comprehension.py
# Demonstrates list comprehensions in Python

# ✅ Basic list comprehension
squares = [x * x for x in range(1, 6)]
print("🔢 Squares from 1 to 5:", squares)

# 🎯 List comprehension with condition (if)
even_numbers = [x for x in range(10) if x % 2 == 0]
print("✅ Even numbers from 0 to 9:", even_numbers)

# 🔁 With else condition
parity = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print("🔄 Even/Odd list:", parity)

# 🧪 From existing list
names = ["Amit", "john", "Sara", "alice"]
capitalized = [name.capitalize() for name in names]
print("🧍 Capitalized names:", capitalized)

# 🧵 Nested loops in comprehension
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print("🔁 All (x, y) pairs:", pairs)

# 📄 Using with strings
words = ["python", "rocks"]
upper_letters = [char.upper() for word in words for char in word]
print("🔠 All uppercase letters:", upper_letters)
