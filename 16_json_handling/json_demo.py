# json_demo.py
# Demonstrates working with JSON data in Python

import json

# ✅ Python dictionary (can be converted to JSON)
person = {
    "name": "Amit",
    "age": 30,
    "city": "Bangalore",
    "is_developer": True,
    "skills": ["Python", "C#", "Docker"]
}

# 📦 Convert Python dict to JSON string
json_string = json.dumps(person)
print("🔁 Python dict → JSON string:")
print(json_string)

# 📄 Write JSON to file
with open("person.json", "w") as file:
    json.dump(person, file)
print("\n✅ JSON written to person.json")

# 📖 Read JSON from file
with open("person.json", "r") as file:
    loaded_data = json.load(file)

print("\n📖 JSON read from file (converted to dict):")
print(loaded_data)

# 🔄 Convert JSON string back to Python dict
json_input = '{"name": "Sara", "age": 25, "city": "Delhi"}'
data = json.loads(json_input)

print("\n🔁 JSON string → Python dict:")
print(data)
