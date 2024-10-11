# Menu() of the program of Crytogtraphy

def main():
    ## main function starts here
    user_choice = menu() # menu options it return user_choice i.e, 1 , 2 , 3

    if user_choice == 1: ## Caesar Cipher
        print("You selected Caesar Cipher!")
        caesar_cipher()
    elif user_choice == 2: ## Vigenere Cipher
        print("You selected Vigenere Cipher!")
    elif user_choice == 3: ## 2x2 Hill Cipher
        print("You selected 2x2 Hill Cipher!")


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
        lower_letter = letter.lower()
        if lower_letter in characters:
            index =  characters.find(lower_letter)
            new_index = (index +key) % 26

            if letter.isupper():
                ciphertext = ciphertext + characters[new_index].upper()
            else:
                ciphertext += characters[new_index]
        else: 
            ciphertext += letter
    return ciphertext
def caesar_cipher_decrypt(ciphertext, key):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    plaintext = ''
    
    for letter in ciphertext:
        lower_letter = letter.lower()
        
        if lower_letter in characters:
            index = characters.find(lower_letter)
            new_index = (index - key) % 26
            if letter.isupper():
                plaintext += characters[new_index].upper()
            else:
                plaintext += characters[new_index]
        else:
            plaintext += letter
    
    return plaintext

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


