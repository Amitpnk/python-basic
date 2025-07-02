# lambda_examples.py
# Demonstrates lambda functions and higher-order functions

from functools import reduce

# ✅ Lambda function (anonymous function)
square = lambda x: x * x
print("🔢 Square of 5:", square(5))

# 🧠 Lambda with multiple arguments
add = lambda a, b: a + b
print("➕ Add 3 and 7:", add(3, 7))

# 🔁 Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print("📌 Squares using map:", squared)

# 🎯 Using lambda with filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("✅ Even numbers using filter:", evens)

# 🧮 Using lambda with reduce()
product = reduce(lambda x, y: x * y, numbers)
print("✖️ Product using reduce:", product)

# 🗂️ Sorting with lambda
students = [("Amit", 90), ("John", 75), ("Sara", 88)]
# Sort by score (second element)
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print("🏅 Students sorted by score (desc):", sorted_by_score)
