# Reverse the given string without using built-in reverse functions. 

s = input("Enter a string: ")

reverse = " "

for char in s:
    reverse = char + reverse
    
print(f"The reverse of {s} is {reverse}")