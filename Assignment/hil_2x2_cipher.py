# *********
# -*- Made by VoxelPixel
# -*- For YouTube Tutorial
# -*- https://github.com/VoxelPixel
# -*- Support me on Patreon: https://www.patreon.com/voxelpixel
# *********

import sys
import math
import numpy as np


def cipher_encryption():
    plaintext = input("Enter message: ").upper()
    plaintext = plaintext.replace(" ", "")

    # if message length is odd number, append 0 at the end
    len_chk = 0
    if len(plaintext) % 2 != 0:
        plaintext += "0"
        len_chk = 1

    # plaintext to matrices
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

    key = input("Enter 4 letter Key String: ").upper()
    key = key.replace(" ", "")

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

    print("Encrypted Text: {}".format(encryp_text))


def cipher_decryption():
    plaintext = input("Enter message: ").upper()
    plaintext = plaintext.replace(" ", "")

    # if message length is odd number, append 0 at the end
    len_chk = 0
    if len(plaintext) % 2 != 0:
        plaintext += "0"
        len_chk = 1

    # plaintext to matrices
    row = 2
    col = int(len(plaintext) / 2)
    plaintext2d = np.zeros((row, col), dtype=int)

    itr1 = 0
    itr2 = 0
    for i in range(len(plaintext)):
        if i % 2 == 0:
            plaintext2d[0][itr1] = int(ord(plaintext[i]) - 65)
            itr1 += 1
        else:
            plaintext2d[1][itr2] = int(ord(plaintext[i]) - 65)
            itr2 += 1
    # for

    key = input("Enter 4 letter Key String: ").upper()
    key = key.replace(" ", "")

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
    itr_count = int(len(plaintext) / 2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = plaintext2d[0][i] * key2d[0][0] + plaintext2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = plaintext2d[0][i] * key2d[1][0] + plaintext2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
            # for
    else:
        for i in range(itr_count - 1):
            temp1 = plaintext2d[0][i] * key2d[0][0] + plaintext2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = plaintext2d[0][i] * key2d[1][0] + plaintext2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
            # for
    # if else

    print("Decrypted Text: {}".format(decryp_text))


def main():
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        print("---Encryption---")
        cipher_encryption()
    elif choice == 2:
        print("---Decryption---")
        cipher_decryption()
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()