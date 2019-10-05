import random
import string
import json


def createKey():
    x = list(string.printable)
    y = x.copy()
    random.shuffle(y)

    return dict(zip(x, y))


def encrypt(msg, key):
    aux = list(msg)
    for i in range(len(msg)):
        aux[i] = key[aux[i]]
    return ''.join(aux)


def createHist(txt):
    h = {}
    for c in txt:
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

with open('hist.json', 'r') as f:
    hist = json.load(f)
    f.close()

