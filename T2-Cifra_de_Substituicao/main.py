import random
import string


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


key = createKey()
# print(key, end = '\n\n')
print(encrypt('random test phrase of a random test', key))
