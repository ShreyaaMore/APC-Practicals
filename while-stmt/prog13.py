# Write a PYTHON program to reverse the given number.

num = int(input("Enter a number: "))

original_num = num

reversed_num = 0

while num > 0:
    last_digit = num % 10
    
    reversed_num = (reversed_num * 10) + last_digit
    
    num = num // 10

print(f"The reverse of {original_num} is {reversed_num}")
