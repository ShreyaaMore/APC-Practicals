# 1.	Create a Python module calculator.py containing functions for addition, subtraction, multiplication, and division. Create another program that imports the module and performs calculations based on user input.

import calculator

print("=== Simple Calculator ===")
print("Operations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1-4): ").strip()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print(f"Result: {num1} + {num2} = {calculator.add(num1, num2)}")
elif choice == "2":
    print(f"Result: {num1} - {num2} = {calculator.subtract(num1, num2)}")
elif choice == "3":
    print(f"Result: {num1} * {num2} = {calculator.multiply(num1, num2)}")
elif choice == "4":
    try:
        print(f"Result: {num1} / {num2} = {calculator.divide(num1, num2)}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
else:
    print("Invalid choice!")

