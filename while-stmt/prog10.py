# Write a PYTHON program to check the entered number is prime or not

num = int(input("Enter a number: "))

is_prime = True

if num <= 1:
    is_prime = False
else:
    divisor = 2
    
    while divisor <= num // 2:
        if num % divisor == 0:
            is_prime = False  
            break             
        divisor = divisor + 1

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
