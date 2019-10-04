import random
import string


def createKey():
    x = list(string.printable)
    y = x.copy()
    random.shuffle(y)

    return dict(zip(x, y))


def encrypt(str, key):
    for a, b in key.items():
        str = str.replace(a, b)
    return str



