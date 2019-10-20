import os
import platform


def encode(key, txt):
    coded = ''
    for i in range(len(txt)):
        coded += chr((ord(txt[i]) + ord(key)) % 256)
    return coded


def decode(key, txt):
    decoded = ''
    for i in range(len(txt)):
        decoded += chr((ord(txt[i]) - key) % 256)
    return decoded


def findKey(coded, decoded):
    key = chr((ord(decoded[0]) - ord(coded[0])) % 256)
    return key


def clearScreen():
    if(platform.system() == 'Windows'):
        os.system('cls')
    elif(platform.system() == 'Linux'):
        os.system('clear')


clearScreen()
key = input('\nKey: ')

with open('sample.txt', 'r') as f:
    txt = f.read()
    f.close()

print(encode(key, txt))

with open('caesar.txt', 'w', encoding="utf-8") as f:
    f.write('Key: ' + str(key))
    f.write('\n\nOriginal: ' + txt)
    f.write('\n\nEncoded: ' + encode(key, txt))
    f.close()
