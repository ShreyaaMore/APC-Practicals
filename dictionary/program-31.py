# 31. Take a list of words, create a dictionary where the key is the word length and the value is a list of words having that length.

words = ["apple", "bat", "cat", "banana", "dog", "elephant", "fox"]

length_dict = {}
for word in words:
    length = len(word)
    if length not in length_dict:
        length_dict[length] = []
    length_dict[length].append(word)

print("List of words:", words)
print("\nGrouped by length:")
print(length_dict)
