"""Module recursion_utils containing recursive mathematical functions."""

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci index cannot be negative.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_series(terms):
    return [fibonacci(i) for i in range(terms)]

def sum_of_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

def binary_conversion(n):
    if n < 0:
        raise ValueError("Binary conversion is defined for non-negative integers here.")
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return binary_conversion(n // 2) + str(n % 2)

