# 22. Create a dictionary containing numbers from 1 to 20 as keys and their squares as values, but include only even numbers.

even_squares = {i: i ** 2 for i in range(2, 21, 2)}

print("Dictionary of even squares (1 to 20):")
print(even_squares)
