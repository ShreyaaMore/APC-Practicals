# 14.	Accept a string from the user and create a dictionary containing each character and its frequency.

string = input("Enter a string: ").lower()

words = {}

for char in string:
  if char in words:
    words[char] += 1
  else:
    words[char] = 1

for ch, freq in words.items():
  print(f"{ch}: {freq}")