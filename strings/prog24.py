# Find the character with the highest frequency.

s = input("Enter a string: ")

if not s:
    print("Empty string.")
else:
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    max_char = max(freq, key=freq.get)
    print(f"Most frequent character: '{max_char}' (Appears {freq[max_char]} times)")