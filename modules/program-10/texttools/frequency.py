"""Word frequency analysis module."""

def word_frequency(tokens):
    freq = {}
    for token in tokens:
        word = token.lower()
        freq[word] = freq.get(word, 0) + 1
    return freq

