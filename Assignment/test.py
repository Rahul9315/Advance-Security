def generate_key(plaintext, key):
    key = list(key)
    if len(plaintext) == len(key):
        return key
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(plaintext, key):
    key = generate_key(plaintext, key)
    ciphertext = []
    
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():  # Only encrypt alphabetic characters
            char = plaintext[i].upper()
            key_char = key[i].upper()
            shift = (ord(char) + ord(key_char)) % 26
            encrypted_char = chr(shift + ord('A'))
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(plaintext[i])  # Non-alphabetic characters remain unchanged
    
    return "".join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    key = generate_key(ciphertext, key)
    plaintext = []
    
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():  # Only decrypt alphabetic characters
            char = ciphertext[i].upper()
            key_char = key[i].upper()
            shift = (ord(char) - ord(key_char) + 26) % 26
            decrypted_char = chr(shift + ord('A'))
            plaintext.append(decrypted_char)
        else:
            plaintext.append(ciphertext[i])  # Non-alphabetic characters remain unchanged
    
    return "".join(plaintext)

# Example usage
plaintext = "Hello,@ ""World!"
key = "KeY"
encrypted_text = vigenere_encrypt(plaintext, key)
decrypted_text = vigenere_decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
