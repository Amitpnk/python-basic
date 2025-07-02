# main.py
# Demonstrates importing and using a custom module

# Importing functions from our custom module
from mymodule.greetings import say_hello, say_goodbye

# Using imported functions
print(say_hello("Amit"))
print(say_goodbye("Amit"))


# Importing the greet function with a default greeting type
from mymodule.greetings import greet
# Using the greet function with different greeting types
print(greet("Amit", "hello"))
print(greet("Amit", "goodbye"))
print(greet("Amit", "unknown")) 

