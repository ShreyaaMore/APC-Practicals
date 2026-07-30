# Write a PYTHON program that prints  1 2 4 8 16 32 … n2

n = int(input("Enter a number: "))
num = 1

for i in range(1,n+1):
    print(num)
    num *= 2
