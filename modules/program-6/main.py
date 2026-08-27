# 6.	Create a module containing recursive functions for factorial, Fibonacci series, sum of digits, and binary conversion. Import and use these functions from another program.

import recursion_utils

num = int(input("Enter a positive integer: "))

print("\nRecursive Operations:")
print(f"Factorial of {num}              : {recursion_utils.factorial(num)}")
print(f"Fibonacci series ({num} terms)   : {recursion_utils.fibonacci_series(num)}")
print(f"Sum of digits of {num}          : {recursion_utils.sum_of_digits(num)}")
print(f"Binary conversion of {num}      : {recursion_utils.binary_conversion(num)}")

