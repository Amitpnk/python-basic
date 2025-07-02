# dictionaries.py
# Demonstrates usage of dictionaries in Python
# In Python, a dictionary is a built-in data structure used to store data in key-value pairs

# ✅ Creating a dictionary
person = {
    "name": "Amit",
    "age": 30,
    "city": "Bangalore"
}

# 🔍 Accessing values
print("Name:", person["name"])
print("Age:", person.get("age"))  # Safe access

# 🆕 Adding or updating values
person["email"] = "amit.naik8103@gmail.com"
person["age"] = 31

print("\nUpdated dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# ❌ Removing an item
del person["city"]

print("\nAfter deleting 'city':", person)

# 🔁 Loop through keys and values
print("\nKeys:")
for key in person:
    print("-", key)

print("\nValues:")
for value in person.values():
    print("-", value)
