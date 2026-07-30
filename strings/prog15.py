# Print all duplicate characters in a string.

s = input("Enter a string: ").lower()

counts = {}
for char in s:
    counts[char] = counts.get(char, 0) + 1

duplicates = [char for char, count in counts.items() if count > 1]

if duplicates:
    print(f"Duplicate characters: {', '.join(repr(c) for c in duplicates)}")
else:
    print("No duplicate characters found.")