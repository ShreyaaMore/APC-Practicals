# 12.	Read a text file and count how many times each word occurs. Display the result using a dictionary.

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as f:
        words = f.read().split()
        word_freq = {}
        for word in words:
            cleaned_word = word.strip(".,!?;:\"'()[]{}").lower()
            if cleaned_word:
                word_freq[cleaned_word] = word_freq.get(cleaned_word, 0) + 1

    print("\nWord Occurrences (Dictionary):")
    for word, count in word_freq.items():
        print(f"'{word}': {count}")
    print("\nFull Dictionary:", word_freq)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

