# 13.	Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears.

filename = input("Enter the file name: ")
target_word = input("Enter the word to search for: ")

try:
    with open(filename, "r") as f:
        total_occurrences = 0
        matching_lines = []

        for line_no, line in enumerate(f, start=1):
            words = [w.strip(".,!?;:\"'()[]{}").lower() for w in line.split()]
            count = words.count(target_word.lower())
            if count > 0:
                total_occurrences += count
                matching_lines.append(line_no)

    print(f"\nSearch results for '{target_word}':")
    print(f"Total occurrences: {total_occurrences}")
    if matching_lines:
        print(f"Appears on line(s): {matching_lines}")
    else:
        print("Word not found in the file.")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

