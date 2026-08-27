# 35. Accept a paragraph and create a dictionary where:
# • Key = word length • Value = number of words having that length.

paragraph = input("Enter a paragraph: ")

words = paragraph.replace(".", "").split()

length_counts = {}
for word in words:
    length = len(word)
    length_counts[length] = length_counts.get(length, 0) + 1

print(f"Paragraph: '{paragraph}'")
print("\nWord length frequencies:")
for length, count in sorted(length_counts.items()):
    print(f"Length {length}: {count} word(s)")
