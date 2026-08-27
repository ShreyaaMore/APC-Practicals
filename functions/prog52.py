words = ["python", "data", "science", "ai", "machine", "learning", "code"]

def get_word_lengths(w_list):
    return list(map(lambda w: len(w), w_list))

lengths = get_word_lengths(words)
print("Lengths of words:", lengths)

long_words = list(filter(lambda w: len(w) > 5, words))
print("Words with > 5 characters:", long_words)

sorted_words = sorted(words, key=lambda w: len(w))
print("Words sorted by length:", sorted_words)
