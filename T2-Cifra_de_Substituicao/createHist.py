import string
import json

hist = {}

f = open('words_alpha.txt', 'r')

for word in f.readlines():
    for c in word:
        if(c not in hist):
            hist[c] = 1
        else:
            hist[c] += 1

del hist['\n']
hist = {k: v for k, v in sorted(hist.items(), key = lambda x: x[1], reverse = True)}

with open('hist.json', 'w') as f:
    json.dump(hist, f)
