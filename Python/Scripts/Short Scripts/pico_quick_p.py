convert = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
alpha = '0abcdefghijklmnopqrstuvwxyz'
big = ''

for i in convert:
    big += alpha[i]
print(big.upper())
