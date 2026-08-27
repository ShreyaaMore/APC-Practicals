# Create a function that checks whether a given string or number is a palindrome

def rev(s):
    if s[::-1]==s:
        return("Palindrome")
    else:
        return("Not Palindrome")

s = input("Enter a string: ")  
print(rev(s)) 