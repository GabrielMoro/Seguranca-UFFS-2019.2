import random
import string
import json


def createKey():
    x = list(string.printable)
    y = x.copy()
    random.shuffle(y)

    return dict(zip(x, y))


def saveKey(key):
    with open('key.json', 'w') as f:
        json.dump(key, f)
        f.close()


# Key as "key = dict(map(reversed, key.items()))" to decrypt
def encrypt(msg, key):
    aux = list(msg)
    for i in range(len(msg)):
        if(aux[i] not in key):
            continue
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


op = input('Create new key? (Y|N)\n')
if(op.lower == 'y'):
    key = createKey()
    saveKey(key)
else:
    with open('key.json', 'r') as f:
        key = json.load(f)
        f.close()

# print(key, end = '\n\n')
with open('txt.txt', 'r') as f:
    msg = f.read()
    f.close()

encrypted = encrypt(msg, key)
with open('encrypted.txt', 'w+') as f:
    f.write(encrypted)
    f.close()

encryptedHist = createHist(encrypted)

with open('frequency.json', 'r') as f:
    letters = json.load(f)
    f.close()

