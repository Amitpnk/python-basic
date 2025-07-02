# sets.py
# Demonstrates usage of sets in Python
# In Python, a set is an unordered collection of unique and immutable elements. It is a built-in data type that provides efficient operations for membership testing, removing duplicates, and performing mathematical set operations

# ✅ Creating sets
languages = {"Python", "Java", "C#", "Python"}  # Duplicates are removed

print("Languages set:", languages)

# ➕ Add and ➖ Remove
languages.add("Go")
languages.discard("Java")

print("\nAfter add and discard:", languages)

# 🎯 Membership test
if "Python" in languages:
    print("✅ Python is in the set.")

# 🔁 Loop through set
print("\nLoop through set:")
for lang in languages:
    print("-", lang)

# 🔄 Set operations
set1 = {"Python", "Java", "C++"}
set2 = {"C++", "Go", "Python"}

print("\nUnion:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
