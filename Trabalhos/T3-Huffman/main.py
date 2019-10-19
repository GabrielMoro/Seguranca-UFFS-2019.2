import heapq


class HeapNode:
    def __init__(self, values = (), left = None, right = None):
        if not isinstance(values, tuple):
            raise TypeError("Values must be a tuple")
        self.values = values
        self.left = left
        self.right = right

def createHist(txt):
    h = {}
    for c in txt:
        if(c not in h):
            h[c] = 1
        else:
            h[c] += 1
    h = {k: v for k, v in sorted(h.items(), key=lambda x: x[1])}
    return h


def compression(hist):
    compressed = ''

    return compressed


with open('.txt', 'r', encoding="utf8") as f:
    txt = f.read()
    txt = txt.lower()
    f.close()

hist = createHist(txt)
