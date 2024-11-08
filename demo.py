# Sample Python Code: Basic Concepts and Operations

# 1. Variables and Data Types
name = "Gopika"  # String
age = 28         # Integer
height = 5.6     # Float
is_dev = True    # Boolean

# 2. Function Definition
def greet_user(name, age):
    """Function that greets the user and shows their age."""
    print(f"Hello {name}, you are {age} years old!")

# Calling the function
greet_user(name, age)

# 3. Conditional Statements
if age > 18:
    print(f"{name} is an adult.")
else:
    print(f"{name} is a minor.")

# 4. Loops (For and While Loops)
# For loop: Iterate over a range
for i in range(5):
    print(f"Iteration {i}")

# While loop: Continue until a condition is met
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1

# 5. Working with Lists
fruits = ["Apple", "Banana", "Cherry", "Date"]

# Access elements in a list
print(f"First fruit: {fruits[0]}")

# Add an element to the list
fruits.append("Elderberry")
print(f"Updated list: {fruits}")

# Iterate through the list
for fruit in fruits:
    print(f"Fruit: {fruit}")

# 6. Dictionary Example (Key-Value pairs)
person = {
    "name": "Gopika",
    "age": 28,
    "job": "DevOps Engineer"
}

# Accessing dictionary values
print(f"Name: {person['name']}, Job: {person['job']}")

# 7. Exception Handling
try:
    number = int(input("Enter a number: "))  # User input
    print(f"You entered: {number}")
except ValueError:
    print("That's not a valid number!")

# 8. Simple Class Definition
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}")

# Create an object of the Car class
car1 = Car("Toyota", "Camry")
car1.display_info()
