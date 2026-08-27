# 15.	Accept a sentence and create a dictionary containing each word and the number of times it occurs.

string = input("Enter a string: ").lower()

words = {}

string_words = string.split(" ")

for word in string_words:
  if word in words:
    words[word] += 1
  else:
    words[word] = 1

for word, freq in words.items():
  print(f"{word}: {freq}")