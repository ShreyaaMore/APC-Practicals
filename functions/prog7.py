# Write a function that accepts n and returns the sum of the first n natural numbers

def sum(n):
    s = 0
    for i in range(1,n+1):
        s = i + s
    return s

n = int(input("Enter a number: "))

print(f"Sum of {n} natural numbers is {sum(n)}")