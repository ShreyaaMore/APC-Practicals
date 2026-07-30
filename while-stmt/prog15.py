# Write a PYTHON program to print the largest of n numbers

n = int(input("How many numbers will you enter? "))

largest = float(input("Enter number 1: "))
count = 1

while count < n:
    num = float(input(f"Enter number {count + 1}: "))
    
    if num > largest:
        largest = num
        
    count += 1

print("The largest number is:", largest)