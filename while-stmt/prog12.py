# Write a PYTHON program to check the entered  number is palindrome or not

num = int(input("Enter a number: "))

original_num = num

reversed_num = 0

while num > 0:
    last_digit = num % 10
    
    reversed_num = (reversed_num * 10) + last_digit
    
    num = num // 10

if original_num == reversed_num:
    print(f"{original_num} is a palindrome number.")
else:
    print(f"{original_num} is not a palindrome number.")
