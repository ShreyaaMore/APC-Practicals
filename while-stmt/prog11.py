# Write a PYTHON program to find the sum of digits of given number

num = int(input("Enter a number: "))

original_num = num

digit_sum = 0

while num > 0:
    last_digit = num % 10
    
    digit_sum = digit_sum + last_digit
    
    num = num // 10

print(f"The sum of the digits of {original_num} is {digit_sum}")
