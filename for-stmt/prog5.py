# Write a PYTHON program to sum the given sequence : 1 + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n!

n = int(input("Enter a number: "))

sum = 0

def factorial(num):
    fact =1
    for i in range(1,num+1):
        fact = fact * i
    return fact

for i in range(n):
    sum += (1/factorial(i))

print(f"Sum: {sum}")
