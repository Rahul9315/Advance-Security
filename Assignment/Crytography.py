# Menu() of the program of Crytogtraphy

def main():
    ## main function starts here
    user_choice = menu() # menu options it return user_choice i.e, 1 , 2 , 3

    if user_choice == 1: ## Caesar Cipher
        print("You selected Caesar Cipher!")
        caesar_cipher()
    elif user_choice == 2: ## Vigenere Cipher
        print("You selected Vigenere Cipher!")
        vigenere_cipher()
    elif user_choice == 3: ## 2x2 Hill Cipher
        print("You selected 2x2 Hill Cipher!")


def vigenere_cipher():
    user_input = input("Do you want to encrypt or decrypt (e/d):  ").lower()

    if user_input == 'e':
        print("Encryption method Selected\n")
        text =  input('Enter the text to be encypted: ')
        key = input('Enter the key:  ')
        ciphertext = vigenere_encrypt(text,key)
        print(f'CIPHERTEXT :  {ciphertext}')
        vigenere_cipher()

    elif user_input == 'd':
        print('Encytion Method selected\n')
        text =  input('Enter the text to be decypted: ')
        key = input('Enter the key:  ')
        plaintext = vigenere_decrypt(text,key)
        print(f'PLAINTEXT :  {plaintext}')
        vigenere_cipher()
        
def caesar_cipher():
    print("Do you want to encrypt or decrpt?")
    user_input = input("e/d :  ").lower()

    if user_input == 'e':
        print('Encytion Method selected\n')
        key = int(input('Enter the key (1 - 26): '))
        text =  input('Enter the text to be encypted: ')
        ciphertext = caesar_cipher_encrypt(text,key)
        print(f'CIPHERTEXT :  {ciphertext}')
        caesar_cipher()

    elif user_input == 'd':
        print('Encytion Method selected\n')
        key = int(input('Enter the key (1 - 26): '))
        text =  input('Enter the text to be decypted: ')
        plaintext = caesar_cipher_decrypt(text,key)
        print(f'PLAINTEXT :  {plaintext}')
        caesar_cipher()


def caesar_cipher_encrypt(plaintext, key):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext = ''
    for letter in plaintext:
        lower_letter = letter.lower() # character to let it remain in lower case  in encrpted text
        if lower_letter in characters:
            index =  characters.find(lower_letter)
            new_index = (index +key) % 26

            if letter.isupper(): # character to let it remain in lupper case in encryted text
                ciphertext = ciphertext + characters[new_index].upper()
            else:
                ciphertext += characters[new_index]
        else: 
            ciphertext += letter # to deal with the special characteres like " , ; @ ! 1 2 3 \ these characyters will remain unchanged
    return ciphertext

def caesar_cipher_decrypt(ciphertext, key):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    plaintext = ''
    
    for letter in ciphertext:
        lower_letter = letter.lower() # character to let it remain in lower case  in encrpted text
        
        if lower_letter in characters:
            index = characters.find(lower_letter)
            new_index = (index - key) % 26
            if letter.isupper():
                plaintext += characters[new_index].upper() #character to let it remain in lupper case in encryted text
            else:
                plaintext += characters[new_index]
        else:
            plaintext += letter # to deal with the special characteres like " , ; @ ! 1 2 3 \ these characters will remain unchanged
    
    return plaintext

def vigenere_encrypt(plaintext, key):
    key = generate_key_vigenere_cipher(plaintext, key)
    ciphertext = []
    
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():  # Only encrypt alphabetic characters
            char = plaintext[i].upper()
            key_char = key[i].upper()
            shift = (ord(char) + ord(key_char)) % 26 ## ord is use to convert in acii no.
            encrypted_char = chr(shift + ord('A'))
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(plaintext[i])  # Non-alphabetic characters remain unchanged
    
    return "".join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    key = generate_key_vigenere_cipher(ciphertext, key)
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

def generate_key_vigenere_cipher(plaintext, key): ## key of the same length as the plain text or ciphertext
    key = list(key)
    if len(plaintext) == len(key):
        return key
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def menu(): # it return user_choice i.e, 1 , 2 , 3

    user_choice = 1

    while True:
        
        print("---------------------------------------------------------")
        print("Welcome to CrytoGraphy World!!")
        print("Select an option below in Integers 1-3 only!!")
        print("1. Caesar Cipher ")
        print("2. Vigenere Cipher ")
        print("3. 2x2 Hill Cipher ")
        print("---------------------------------------------------------")

        try:
            user_choice = int(input("Enter your choice (1-3): "))
            if user_choice in [1, 2, 3]:
                return user_choice
            else:
                print("Invalid input. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def encrytion():
    print("hello world 2!!!!")

if __name__ == "__main__":
    main()


