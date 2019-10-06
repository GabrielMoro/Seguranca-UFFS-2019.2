import json

def createHist(filename):
    hist = {}

    with open(filename, 'r') as f:
        for word in f.read():
            for c in word:
                if(c == '\n'):
                    continue
                if(c not in hist):
                    hist[c] = 1
                else:
                    hist[c] += 1
        f.close()

    hist = {k : v for k, v in sorted(hist.items(), key = lambda x: x[1], reverse = True)}
    return hist


def saveHist(hist):
    with open('letter_frequency.json', 'w') as f:
        json.dump(hist, f)
        f.close()


hist = createHist('words.txt')
# hist = createHist('sample.txt')
saveHist(hist)
