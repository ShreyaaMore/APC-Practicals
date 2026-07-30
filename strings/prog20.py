# Count how many times a specific word appears in a sentence.

sentence = input("Enter a sentence: ").lower()
target = input("Enter the word to count: ").lower()

words = sentence.split()
count = 0

for word in words:
    if word == target:
        count += 1

print(f"The word '{target}' appears {count} times.")