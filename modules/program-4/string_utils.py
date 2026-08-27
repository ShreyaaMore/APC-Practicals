"""Module string_utils containing common string manipulation functions."""

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

def count_words(s):
    return len(s.split())

def remove_spaces(s):
    return "".join(s.split())

