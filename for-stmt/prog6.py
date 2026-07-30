# Write a PYTHON program to compute the cosine series
# cos(x) = 1 – x2 / 2! + x4 / 4! – x6 / 6! + … xn / n!

import math

n = int(input("Enter a number: "))
n = math.radians(n)
terms = 50

def factorial(num):
    f = 1
    for i in range(1, num+1):
        f = f * i
    return f

sum = 0
s = 1

for i in range(0, 2 * terms, 2):
    term = (n ** i) / factorial(i)
    sum += s * term
    s *= -1  

print(round(sum, 4))