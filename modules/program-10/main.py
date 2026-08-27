# 10.	Create a package texttools containing:
# a)	cleaning.py – remove punctuation and extra spaces 
# b)	tokenization.py – tokenize text 
# c)	frequency.py – word-frequency analysis
# Create a main program to use the package.

from texttools.cleaning import remove_punctuation, remove_extra_spaces
from texttools.tokenization import tokenize_words, tokenize_sentences
from texttools.frequency import word_frequency

sample_text = """
    Python is a popular programming language! Python is used for web development,
    software development, and data analysis. Is Python easy to learn? Yes, Python is great!
"""

print("Original Text:")
print(sample_text)

cleaned_text = remove_punctuation(sample_text)
cleaned_text = remove_extra_spaces(cleaned_text)
print("Cleaned Text (Punctuation and extra spaces removed):")
print(cleaned_text)

words = tokenize_words(cleaned_text)
print(f"\nWords Tokenized ({len(words)} words):")
print(words)

sentences = tokenize_sentences(sample_text)
print(f"\nSentences Tokenized ({len(sentences)} sentences):")
for s in sentences:
    print(f"- {s}")

freq = word_frequency(words)
print("\nWord Frequency Analysis:")
for word, count in sorted(freq.items(), key=lambda item: item[1], reverse=True):
    print(f"'{word}': {count}")

