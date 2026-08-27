# 4.	Create a module string_utils.py containing functions to count vowels, reverse a string, check palindrome, count words, and remove spaces.

import string_utils

text = input("Enter a string: ")

print("\nString Operations:")
print(f"Original String    : {text}")
print(f"Number of Vowels   : {string_utils.count_vowels(text)}")
print(f"Reversed String    : {string_utils.reverse_string(text)}")
print(f"Is Palindrome      : {'Yes' if string_utils.is_palindrome(text) else 'No'}")
print(f"Total Words        : {string_utils.count_words(text)}")
print(f"Without Spaces     : {string_utils.remove_spaces(text)}")

