import heapq


def createHist(txt):
    h = {}
    for c in txt:
        if(c not in h):
            h[c] = 1
        else:
            h[c] += 1
    h = {k: v for k, v in sorted(h.items(), key=lambda x: x[1])}
    return h


def createHeap(hist):
    heap = [[weight, [symbol, '']] for symbol, weight in hist.items()]
    heapq.heapify(heap)
    while(len(heap) > 1):
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            for i in left[1:]:
                i[1] = '0' + i[1]
            for i in right[1:]:
                i[1] = '1' + i[1]
            heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def compress(txt, hist):
    c = ''

    heap = createHeap(hist)
    aux = {i[0] : i[1] for i in heap}

    # txt = list(txt)
    for i in range(len(txt)):
        c += aux[txt[i]]


with open('.txt', 'r', encoding="utf8") as f:
    txt = f.read()
    # txt = txt.lower()
    f.close()

hist = createHist(txt)

compress(txt, hist)
