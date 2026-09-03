# 11.	Read a text file and find the longest word present in the file.

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as f:
        words = f.read().split()
        cleaned_words = [w.strip(".,!?;:\"'()[]{}") for w in words]
        cleaned_words = [w for w in cleaned_words if w]

        if cleaned_words:
            longest_word = max(cleaned_words, key=len)
            print(f"Longest word: {longest_word}")
            print(f"Length: {len(longest_word)}")
        else:
            print("No words found in the file.")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

