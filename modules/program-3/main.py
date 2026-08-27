# 3.	Create a module number_utils.py containing functions to check whether a number is prime, palindrome, Armstrong, or perfect. Import the required functions into a main program.

from number_utils import is_prime, is_palindrome, is_armstrong, is_perfect

num = int(input("Enter an integer to check its properties: "))

print(f"\nProperties of {num}:")
print(f"Prime Number     : {'Yes' if is_prime(num) else 'No'}")
print(f"Palindrome       : {'Yes' if is_palindrome(num) else 'No'}")
print(f"Armstrong Number : {'Yes' if is_armstrong(num) else 'No'}")
print(f"Perfect Number   : {'Yes' if is_perfect(num) else 'No'}")

