# tuples.py
# Demonstrates tuple usage in Python
# A tuple in Python is an ordered collection of items, similar to a list, but with a key distinction: immutability.

# ✅ Creating a tuple
coordinates = (10.5, 20.8)

# 📌 Accessing elements
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])

# ❌ Tuples are immutable
# coordinates[0] = 99  # This would raise an error

# 🎯 Single-element tuple (note the comma)
single = (42,)
print("Single-element tuple:", single)

# 🔁 Loop through a tuple
print("Coordinates:")
for value in coordinates:
    print(value)

# 🔁 Tuple unpacking
x, y = coordinates
print(f"Unpacked: x = {x}, y = {y}")
