# file_read_write.py
# Demonstrates reading and writing files in Python

# 📄 Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a file.\n")
    file.write("Learning Python file I/O is fun!\n")

print("✅ sample.txt file created and written.")

# 📖 Reading the whole file
with open("sample.txt", "r") as file:
    content = file.read()
    print("\n📖 Full file content:")
    print(content)

# 📘 Reading line by line
print("📘 Line by line:")
with open("sample.txt", "r") as file:
    for line in file:
        print(f"> {line.strip()}")

# ➕ Appending to the file
with open("sample.txt", "a") as file:
    file.write("This line was added later.\n")

print("\n✅ Line appended to sample.txt.")

# ✅ Verifying appended content
with open("sample.txt", "r") as file:
    print("\n📂 Updated file content:")
    print(file.read())
