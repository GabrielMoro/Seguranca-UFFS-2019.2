import os
import platform
import time
import heapq
import json


# Source: https://gist.github.com/bhrigu123/a0e50b1b468cff905346b451ab3a2c39#file-huffmancoding-py
def pad_encoded_text(encoded_text):
		extra_padding = 8 - len(encoded_text) % 8
		for i in range(extra_padding):
			encoded_text += "0"

		padded_info = "{0:08b}".format(extra_padding)
		encoded_text = padded_info + encoded_text
		return encoded_text


# Source: https://gist.github.com/bhrigu123/a0e50b1b468cff905346b451ab3a2c39#file-huffmancoding-py
def remove_padding(padded_encoded_text):
		padded_info = padded_encoded_text[:8]
		extra_padding = int(padded_info, 2)

		padded_encoded_text = padded_encoded_text[8:]
		encoded_text = padded_encoded_text[:-1*extra_padding]

		return encoded_text


# Source: https://gist.github.com/bhrigu123/a0e50b1b468cff905346b451ab3a2c39#file-huffmancoding-py
def get_byte_array(padded_encoded_text):
    if(len(padded_encoded_text) % 8 != 0):
        print("Encoded text not padded properly")
        exit(0)

    b = bytearray()
    for i in range(0, len(padded_encoded_text), 8):
        byte = padded_encoded_text[i:i+8]
        b.append(int(byte, 2))
    return b


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
    heap = {i[0] : i[1] for i in heap}

    # txt = list(txt)
    for i in range(len(txt)):
        c += heap[txt[i]]

    with open('compressed/' + file_name + '.bin', 'wb') as f:
        f.write(get_byte_array(pad_encoded_text(c)))
        f.close()

    heap = {v: k for k, v in heap.items()}
    return heap


def decompress(heap, file_name):
    bin_txt = ''
    dec_txt = ''

    with open('compressed/' + file_name + '.bin', 'rb') as f:
        byte = f.read(1)
        while(byte is not None):
            if(len(byte) != 1):
                break
            # Source: https://gist.github.com/bhrigu123/a0e50b1b468cff905346b451ab3a2c39#file-huffmancoding-py
            byte = ord(byte)
            bits = bin(byte)[2:].rjust(8, '0')
            bin_txt += bits
            byte = f.read(1)
        f.close()

    # Source: Eu
    bin_txt = remove_padding(bin_txt)
    aux = ''
    for i in bin_txt:
        aux += i
        if(aux in heap):
            dec_txt += heap[aux]
            aux = ''

    with open('decompressed/' + file_name + '_dec.txt', 'w', encoding = 'utf8') as f:
        f.write(dec_txt)
        f.close()


def clearScreen():
    if(platform.system() == 'Windows'):
        os.system('cls')
    elif(platform.system() == 'Linux'):
        os.system('clear')


while(True):
    clearScreen()
    print('1 - Compress\n2 - Decompress\n3 - Exit\n')
    opt = int(input('Opt: '))
    if(opt == 1):
        try:
            file = input('File to compress: ')
            file_name = file.split('.')[0]
            with open('files/' + file_name + '.txt', 'r', encoding = "utf8") as f:
                txt = f.read()
                f.close()

            hist = createHist(txt)
            heap = compress(txt, hist)
            with open('heaps/' + file_name + '.json', 'w') as f:
                json.dump(heap, f)
                f.close()
        except:
            print('\nFile not found!\n')
            time.sleep(1)
    elif(opt == 2):
        try:
            file = input('File to decompress: ')
            file_name = file.split('.')[0]
            with open('heaps/' + file_name + '.json', 'r') as f:
                heap = json.load(f)
                f.close()
            decompress(heap, file_name)
        except:
            print('\nFile not found!\n')
            time.sleep(1)
    else:
        clearScreen()
        break
