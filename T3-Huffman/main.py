def createHist(txt):
    h = {}
    for c in txt:
        if(c not in h):
            h[c] = 1
        else:
            h[c] += 1
    h = {k: v for k, v in sorted(h.items(), key=lambda x: x[1], reverse=True)}
    return h


with open('.txt', 'r') as f:
    txt = f.read()
    txt = txt.lower()
    f.close()

hist = createHist(txt)
print(hist)
