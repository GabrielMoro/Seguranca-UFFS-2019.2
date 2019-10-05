import string
import json


hist = {}

with open('words_alpha.txt', 'r') as f:
    for word in f.readlines():
        for c in word:
            if(c == '\n'):
                continue
            if(c not in hist):
                hist[c] = 1
            else:
                hist[c] += 1
    f.close()

hist = {k : v for k, v in sorted(hist.items(), key = lambda x: x[1], reverse = True)}

with open('hist.json', 'w') as f:
    json.dump(hist, f)
    f.close()
