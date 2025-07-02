# exception_handling.py
# Demonstrates how to handle exceptions in Python

# ✅ Try-Except block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero.")

# 🎯 Catching multiple exceptions
try:
    number = int("abc")
except ValueError as ve:
    print(f"❌ ValueError: {ve}")
except TypeError as te:
    print(f"❌ TypeError: {te}")

# ✅ Using else and finally
try:
    num1 = 5
    num2 = 2
    result = num1 / num2
except ZeroDivisionError:
    print("❌ Cannot divide by zero.")
else:
    print(f"✅ Division result: {result}")
finally:
    print("🔚 This block always runs (finally).")

# 🚨 Custom exception
def withdraw(balance, amount):
    if amount > balance:
        raise Exception("Insufficient funds!")
    return balance - amount

try:
    new_balance = withdraw(1000, 1500)
    print(f"New balance: {new_balance}")
except Exception as e:
    print(f"❌ Withdrawal error: {e}")
