def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"

def calculate(func, a, b):
    return func(a, b)

a = 20
b = 5
print("Addition:", calculate(add, a, b))
print("Subtraction:", calculate(subtract, a, b))
print("Multiplication:", calculate(multiply, a, b))
print("Division:", calculate(divide, a, b))
