# Write a PYTHON program to print Fibonacci series up to n using while loop

n = int(input("Enter a number: "))

a = 0
b = 1
count = 0

print("Fibonacci series:")

while count < n:
    print(a, end=" ")
    
    next_term = a + b
    
    a = b
    b = next_term
    
    count = count + 1
