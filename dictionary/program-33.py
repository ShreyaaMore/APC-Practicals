# 33. Take a string, use a dictionary to find the first character that occurs only once.

text = input("Enter a string: ")

def first_unique_char(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    for char in s:
        if char_counts[char] == 1:
            return char
    return None

result = first_unique_char(text)
print(f"String: '{text}'")
if result:
    print(f"First character that occurs only once: '{result}'")
else:
    print("No unique character found.")
