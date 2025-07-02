# string_operations.py
# Demonstrates string manipulation in Python

# ✅ Creating strings
name = "Amit"
greeting = "Hello, " + name + "!"
print(greeting)

# 🎯 f-strings (formatted strings)
age = 30
print(f"My name is {name} and I am {age} years old.")

# 🔁 Multiline strings
message = """This is a
multiline
string."""
print("\nMultiline message:")
print(message)

# 📏 String length
print("\nLength of name:", len(name))

# 🔠 String methods
sample = "  python programming  "

print("\nOriginal:", sample)
print("Upper:", sample.upper())
print("Lower:", sample.lower())
print("Title:", sample.title())
print("Stripped:", sample.strip())

# 🔍 Searching and replacing
print("\nDoes it contain 'python'? :", "python" in sample)
print("Replace 'python' with 'Python':", sample.replace("python", "Python"))

# 🔗 Splitting and joining
sentence = "Learn Python With Amit"
words = sentence.split()
print("\nWords:", words)

joined = "-".join(words)
print("Joined with - :", joined)

# 🎯 Indexing and slicing
print("\nFirst letter:", name[0])
print("Last letter:", name[-1])
print("First 2 letters:", name[:2])
