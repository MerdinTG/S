# Python Exercises

## Task 1: Input/Output Operations
# Get user input and print it back.
name = input("Enter your name: ")
print(f"Hello, {name}!")

## Task 2: Arithmetic Operations
# Perform basic arithmetic operations.
a = 10
b = 5
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")

## Task 3: Temperature Conversion
# Convert Celsius to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

## Task 4: Comments
# This is a comment example.
# Comments can be used to explain code.

## Task 5: Rectangle Area Calculation
# Calculate the area of a rectangle.
length = float(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))
area = length * breadth
print(f"Area of the rectangle: {area}")

## Task 6: Data Type Validation
# Validate the data type of an input.
value = input("Enter a number: ")
if value.isdigit():
    print(f"You entered a valid number: {value}")
else:
    print("Invalid input! Please enter a number.")