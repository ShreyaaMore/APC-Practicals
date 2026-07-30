# Write a PYTHON program to print the multiplication table

num = int(input("Enter a number: "))

i = 1

print(f"Multiplication Table of {num}:")

while i <= 10:
    result = num * i
    print(f"{num} x {i} = {result}")
    
    i = i + 1
