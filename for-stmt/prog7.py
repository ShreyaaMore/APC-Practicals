# Write a short PYTHON program to check weather the square root of number is prime or  not.

n = int(input("Enter a number: "))
prime = True
sq = n**0.5

for i in range(2,int(sq/2)):
    if sq%i==0:
        print(f"The square root of {n} is not prime.")
        prime = False

if prime:
    print(f"The square root of {n} is prime")