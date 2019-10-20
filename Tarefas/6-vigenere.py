import os
import platform


def clearScreen():
    if(platform.system() == 'Windows'):
        os.system('cls')
    elif(platform.system() == 'Linux'):
        os.system('clear')


def encode(key, txt):
    coded = ''
    for i in range(len(txt)):
        aux = ord(key[i % len(key)])
        coded += chr((ord(txt[i]) + aux) % 256)
    return coded


def decode(key, txt):
    decoded = ''
    for i in range(len(txt)):
        aux = ord(key[i % len(key)])
        decoded += chr((ord(txt[i]) - aux) % 256)
    return decoded


clearScreen()
key = input('\nKey: ')

with open('sample.txt', 'r') as f:
    txt = f.read()
    f.close()

with open('vigenere.txt', 'w', encoding="utf-8") as f:
    f.write('Key: ' + str(key))
    f.write('\n\nOriginal: ' + txt)
    f.write('\n\nEncoded: ' + encode(key, txt))
    f.write('\n\nDecoded: ' + decode(key, encode(key, txt)))
    f.close()
