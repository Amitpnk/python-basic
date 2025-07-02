# lists.py
# Demonstrates list operations in Python

# ✅ Creating a list
fruits = ["apple", "banana", "cherry"]

# 🔄 Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 🧪 Modifying list
fruits.append("orange")
print("After append:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

# 📌 List slicing
print("First two fruits:", fruits[:2])

# 🔁 Loop through list
print("All fruits:")
for fruit in fruits:
    print("-", fruit)

# 🎯 Check if item exists
if "apple" in fruits:
    print("✅ Apple is in the list.")

# 📦 List methods
fruits.sort()
print("Sorted fruits:", fruits)

# 🔁 List comprehension
upper_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", upper_fruits)
