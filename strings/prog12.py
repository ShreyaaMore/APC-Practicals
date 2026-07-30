# Find the longest word in a given sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()

if words:
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    print(f"Longest word: {longest}")
else:
    print("No words entered.")