# decorators.py
# Demonstrates the use of decorators in Python

# ✅ A simple decorator
def simple_decorator(func):
    def wrapper():
        print("🎁 Before function call")
        func()
        print("🎁 After function call")
    return wrapper

# 🎯 Apply decorator manually
def greet():
    print("👋 Hello from greet()")

decorated_greet = simple_decorator(greet)
decorated_greet()

print("\n--- Using @decorator syntax ---")

# 💡 Using @ syntax
@simple_decorator
def say_hello():
    print("👋 Hello from say_hello()")

say_hello()

# 📦 Decorator with arguments
def log_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"📥 Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"📤 Result: {result}")
        return result
    return wrapper

@log_arguments
def add(a, b):
    return a + b

@log_arguments
def greet_user(name, age=30):
    return f"Hello {name}, age {age}"

print("\n--- Function with arguments ---")
add(5, 7)
greet_user("Amit", age=32)
