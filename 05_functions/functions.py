# functions.py
# Demonstrates how to define and use functions in Python

# 🧠 A simple function
def greet():
    print("Hello, welcome to Python functions!")

# ✅ Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

# 🎯 Function with return value
def add(a, b):
    return a + b

# 🔄 Function with default parameter
def power(base, exponent=2):
    return base ** exponent

# 📦 Function with multiple return values
def divide_and_remainder(x, y):
    quotient = x // y
    remainder = x % y
    return quotient, remainder

# 🔁 Function calling another function
def welcome_user(username):
    greet_user(username)
    print("Hope you're ready to code!")

# --- Main Execution ---
print("🚀 Function Demo Output:")

greet()

greet_user("Amit")

result = add(10, 5)
print(f"10 + 5 = {result}")

print(f"Power of 3 (default exponent): {power(3)}")
print(f"Power of 2^5: {power(2, 5)}")

q, r = divide_and_remainder(17, 4)
print(f"17 divided by 4: Quotient = {q}, Remainder = {r}")

welcome_user("Amit")
