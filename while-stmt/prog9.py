# Write a PYTHON program  find a factorial of given number using while loop

n = int(input("Enter a number:"))

fact = 1
i=1

while(i<=n):
    fact *= i
    i+=1

print(f"The factorial of {n} is {fact}")