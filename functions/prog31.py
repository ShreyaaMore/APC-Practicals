def is_palindrome_recursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])

s = input("Enter a string: ")
if is_palindrome_recursive(s):
    print("Palindrome")
else:
    print("Not Palindrome")
