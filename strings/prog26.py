# Encrypt and decrypt a message using the Caesar Cipher algorithm.

text = input("Enter your message: ")
shift = int(input("Enter the shift number (e.g., 3): "))
mode = input("Type 'encrypt' or 'decrypt': ").lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""

for char in text:
    if char.lower() in alphabet:
        # Find its current position (0 to 25)
        current_position = alphabet.find(char.lower())
        
        if mode == "encrypt":
            new_position = (current_position + shift) % 26
        elif mode == "decrypt":
            new_position = (current_position - shift) % 26
            
        new_letter = alphabet[new_position]
        
        if char.isupper():
            result += new_letter.upper()
        else:
            result += new_letter
            
    else:
        result += char

print(f"Result: {result}")