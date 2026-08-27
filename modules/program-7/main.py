# 7.	Create a package named mathutils containing:
# a)	basic.py – arithmetic operations 
# b)	number.py – prime, Armstrong, palindrome functions 
# c)	statistics.py – mean, maximum, minimum 
# Create a main program that imports functions from each module.

from mathutils.basic import add, multiply
from mathutils.number import is_prime, is_armstrong, is_palindrome
from mathutils.statistics import mean, maximum, minimum

print("mathutils Package example:")

a, b = 15, 4
print(f"Basic: {a} + {b} = {add(a, b)}, {a} * {b} = {multiply(a, b)}")

test_num = 153
print(f"Number {test_num}:")
print(f" - Prime?      {is_prime(test_num)}")
print(f" - Armstrong?  {is_armstrong(test_num)}")
print(f" - Palindrome? {is_palindrome(test_num)}")

dataset = [12, 45, 67, 89, 34, 23, 90]
print(f"Dataset: {dataset}")
print(f" - Mean:    {mean(dataset):.2f}")
print(f" - Maximum: {maximum(dataset)}")
print(f" - Minimum: {minimum(dataset)}")

