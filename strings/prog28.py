# Count the frequency of every word in a paragraph.

paragraph = input("Enter a paragraph: ")

clean_text = paragraph.lower()

clean_text = clean_text.replace(".", "").replace(",", "").replace("!", "").replace("?", "")

words = clean_text.split()

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print("\nWord Frequencies:")
for word, count in word_counts.items():
    print(f"'{word}': {count}")