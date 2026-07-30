# Display the frequency of every character in a string.

s = input("Enter a string: ")

freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1

print("Character Frequency:")
for char, count in freq.items():
    print(f"'{char}': {count}")