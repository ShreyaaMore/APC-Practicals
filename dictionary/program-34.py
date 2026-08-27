# 34. Take a string, use a dictionary to find the first character that occurs more than once.

text = input("Enter a string: ")

def first_repeating_char(s):
    seen = {}
    for char in s:
        if char in seen:
            return char
        seen[char] = True
    return None

result = first_repeating_char(text)
print(f"String: '{text}'")
if result:
    print(f"First character that occurs more than once: '{result}'")
else:
    print("No repeating character found.")
