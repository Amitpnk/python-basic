# if_else.py
# Demonstrates conditional statements in Python

age = 25

# Simple if
if age >= 18:
    print("✅ You are an adult.")

# if-else
if age < 18:
    print("❌ You are a minor.")
else:
    print("✅ You are eligible to vote.")

# if-elif-else
marks = 90

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print(f"🎓 Your grade is: {grade}")

# Nested if
is_logged_in = True
is_admin = False

if is_logged_in:
    print("👋 Welcome, user.")
    if is_admin:
        print("🔒 Access to admin panel granted.")
    else:
        print("⚠️ Admin access denied.")
else:
    print("🔐 Please log in first.")
