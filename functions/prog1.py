# Write a function factorial(n) that accepts an integer and returns its factorial.

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i

    return fact

result = factorial(5)
print(result)