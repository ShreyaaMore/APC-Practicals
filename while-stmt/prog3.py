# Write a PYTHON program to print odd numbers up to n using while loop

n = int(input("Enter a number: "))

i = 1

while(i<=n):
    if(i%2!=0):
        print(i)
    i+=1
