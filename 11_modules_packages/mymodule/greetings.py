# greetings.py
# A simple custom module with reusable functions

def say_hello(name):
    return f"Hello, {name}!"

def say_goodbye(name):
    return f"Goodbye, {name}!"

# This module provides functions to greet users with different messages.
def greet(name, greeting_type='hello'):
    if greeting_type == 'hello':
        return say_hello(name)
    elif greeting_type == 'goodbye':
        return say_goodbye(name)
    else:
        return f"Unknown greeting type: {greeting_type}"