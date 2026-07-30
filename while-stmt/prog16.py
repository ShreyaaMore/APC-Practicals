# Write a PYTHON program to print smallest of n numbers

n = int(input("How many numbers will you enter? "))

smallest = float(input("Enter number 1: "))
count = 1

while count < n:
    num = float(input(f"Enter number {count + 1}: "))
    
    if num < smallest:
        smallest = num
        
    count += 1

print("The smallest number is:", smallest)
