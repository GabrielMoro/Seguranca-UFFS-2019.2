a = [1, 2, 3, 4, 5]
e = [3, 5, 7]

for i in a:
    for j in e:
        print(f'{i}^({j}-1)mod{j} = {i**(j-1) % j}')
        

