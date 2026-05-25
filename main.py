# Write a Python program to create a calculator. Create individual functions for different operators - addition, subtraction, 
# division, multiplication and return the output value.


num1 = int(input("Enter the 1st Number: "))
num2 = int(input("Enter the 2nd Number: "))
operation = str(input("What operation do you want to perform: "))

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

if operation == "+":
    print(add(num1, num2))
elif operation == "-":
    print(sub(num1, num2))
elif operation == "*":
    print(multiply(num1, num2))
elif operation == "/":
    print(divide(num1, num2))
else:
    print("Invalid Operation")