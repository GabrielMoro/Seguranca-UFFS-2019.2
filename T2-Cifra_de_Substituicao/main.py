import random
import string
import json


def createKey():
    x = list(string.ascii_letters)
    y = x.copy()
    random.shuffle(y)

    return dict(zip(x, y))


def encrypt(msg, key):
    aux = list(msg)
    for i in range(len(msg)):
        if(aux[i] not in key):
            continue
        aux[i] = key[aux[i]]
    return ''.join(aux)


def decryptWithKey(msg, key):
    key = dict(map(reversed, key.items()))
    aux = list(msg)
    for i in range(len(msg)):
        if(aux[i] not in key):
            continue
        aux[i] = key[aux[i]]
    return ''.join(aux)


def createHist(txt):
    h = {}
    for c in txt:
        if(c not in string.ascii_letters):
            continue
        if(c not in h):
            h[c] = 1
        else:
            h[c] += 1
    h = {k: v for k, v in sorted(h.items(), key=lambda x: x[1], reverse=True)}
    return h


key = createKey()
# print(key, end = '\n\n')
with open('txt.txt', 'r') as f:
    msg = f.read()
    f.close()

encrypted = encrypt(msg, key)
print(encrypted)
encryptedHist = createHist(encrypted)
# print(encryptedHist, len(encryptedHist))

print(decryptWithKey(encrypted, key))

with open('letter_frequency.json', 'r') as f:
    letters = json.load(f)
    f.close()

