import sys
import numpy as np

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
        hill_cipher()


def hill_cipher():
    user_input = input("Do you want to encrypt or decrypt (e/d):  ").lower()

    if user_input == 'e':
        print("Encryption method Selected\n")
        text =  input('Enter the text to be encypted: ').upper()
        key = input('Enter the 4 letter Key:  ').upper()
        ciphertext = hill_cipher_encryption(text,key)
        print(f'CIPHERTEXT :  {ciphertext}')
        hill_cipher()

    elif user_input == 'd':
        print('Decrytion Method selected\n')
        text =  input('Enter the text to be decypted: ').upper()
        key = input('Enter the 4 letter key:  ').upper()
        plaintext = hill_cipher_decryption(text,key)
        print(f'PLAINTEXT :  {plaintext}')
        hill_cipher()

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
        print('Decrytion Method selected\n')
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
        print('Decytion Method selected\n')
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


def hill_cipher_encryption(plaintext ,key):
    plaintext = plaintext.replace(" ", "") # removing space
    key = key.replace(" ", "") #removing space

    # if message length is odd number, append 0 at the end
    len_chk = 0
    if len(plaintext) % 2 != 0:
        plaintext += "0"
        len_chk = 1

    # msg to matrices
    row = 2
    col = int(len(plaintext)/2)
    plaintext2d = np.zeros((row, col), dtype=int)

    itr1 = 0
    itr2 = 0
    for i in range(len(plaintext)):
        if i % 2 == 0:
            plaintext2d[0][itr1] = int(ord(plaintext[i])-65)
            itr1 += 1
        else:
            plaintext2d[1][itr2] = int(ord(plaintext[i])-65)
            itr2 += 1
    # for
    # key to 2x2
    key2d = np.zeros((2, 2), dtype=int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr3])-65
            itr3 += 1

    # checking validity of the key
    # finding determinant
    deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
    deter = deter % 26

    # finding multiplicative inverse
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue
    # for

    if mul_inv == -1:
        print("Invalid key")
        sys.exit()
    # if

    encryp_text = ""
    itr_count = int(len(plaintext)/2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = plaintext2d[0][i] * key2d[0][0] + plaintext2d[1][i] * key2d[0][1]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = plaintext2d[0][i] * key2d[1][0] + plaintext2d[1][i] * key2d[1][1]
            encryp_text += chr((temp2 % 26) + 65)
        # for
    else:
        for i in range(itr_count-1):
            temp1 = plaintext2d[0][i] * key2d[0][0] + plaintext2d[1][i] * key2d[0][1]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = plaintext2d[0][i] * key2d[1][0] + plaintext2d[1][i] * key2d[1][1]
            encryp_text += chr((temp2 % 26) + 65)
        # for
    # if else
    return encryp_text

def hill_cipher_decryption(ciphertext,key):
    key = key.replace(" ", "")
    ciphertext = ciphertext.replace(" ", "")

    # if message length is odd number, append 0 at the end
    len_chk = 0
    if len(ciphertext) % 2 != 0:
        ciphertext += "0"
        len_chk = 1

    # ciphertext to matrices
    row = 2
    col = int(len(ciphertext) / 2)
    ciphertext2d = np.zeros((row, col), dtype=int)

    itr1 = 0
    itr2 = 0
    for i in range(len(ciphertext)):
        if i % 2 == 0:
            ciphertext2d[0][itr1] = int(ord(ciphertext[i]) - 65)
            itr1 += 1
        else:
            ciphertext2d[1][itr2] = int(ord(ciphertext[i]) - 65)
            itr2 += 1
    # for

    # key to 2x2
    key2d = np.zeros((2, 2), dtype=int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr3]) - 65
            itr3 += 1
    # for

    # finding determinant
    deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
    deter = deter % 26

    # finding multiplicative inverse
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue
    # for

    # adjugate matrix
    # swapping
    key2d[0][0], key2d[1][1] = key2d[1][1], key2d[0][0]

    # changing signs
    key2d[0][1] *= -1
    key2d[1][0] *= -1

    key2d[0][1] = key2d[0][1] % 26
    key2d[1][0] = key2d[1][0] % 26

    # multiplying multiplicative inverse with adjugate matrix
    for i in range(2):
        for j in range(2):
            key2d[i][j] *= mul_inv

    # modulo
    for i in range(2):
        for j in range(2):
            key2d[i][j] = key2d[i][j] % 26

    # cipher to plain
    decryp_text = ""
    itr_count = int(len(ciphertext) / 2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = ciphertext2d[0][i] * key2d[0][0] + ciphertext2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = ciphertext2d[0][i] * key2d[1][0] + ciphertext2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
            # for
    else:
        for i in range(itr_count - 1):
            temp1 = ciphertext2d[0][i] * key2d[0][0] + ciphertext2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = ciphertext2d[0][i] * key2d[1][0] + ciphertext2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
            # for
    # if else

    return decryp_text


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

if __name__ == "__main__":
    main()


