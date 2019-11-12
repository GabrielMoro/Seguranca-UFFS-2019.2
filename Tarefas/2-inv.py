n = 21
inv = []

for i in range(2, n):
    for j in range(2, n):
        if((j * i) % n == 1):
            inv.append((i, j))
        
print(inv)
