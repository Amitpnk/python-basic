# for_loop.py
# Demonstrates the use of for-loops in Python

# Looping through a list
fruits = ["apple", "banana", "cherry"]

print("🍎 Fruit List:")
for fruit in fruits:
    print(f"- {fruit}")

# Using range() to loop through numbers
print("\n🔢 Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# Looping through a string
word = "Python"
print("\n📝 Characters in word:")
for char in word:
    print(char)

# Using break and continue
print("\n🎯 break and continue example:")
for i in range(1, 10):
    if i == 5:
        print("Skipped 5 using continue")
        continue
    if i == 8:
        print("Stopped at 8 using break")
        break
    print(f"Processing: {i}")
