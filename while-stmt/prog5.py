# Write a PYTHON program to print sum of odd numbers up to n using while loop

n = int(input("Enter a number: "))

i = 1
sum = 0
while(i<=n):
    if(i%2!=0):
        sum += i
    i+=1
print(sum)