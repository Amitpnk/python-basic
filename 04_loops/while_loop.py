# while_loop.py
# Demonstrates the use of while-loops in Python

count = 1

print("🔁 Counting with while loop:")
while count <= 5:
    print(f"Count is: {count}")
    count += 1

# Example with user input (simulated here for demo)
# You can uncomment below to try interactive input

password = ""
while password != "python":
    password = input("Enter the password: ")
print("🔓 Access granted!")

# Infinite loop example (with break)
print("\n🛑 Infinite loop with break:")
x = 1
while True:
    print(f"x = {x}")
    x += 1
    if x > 3:
        break
