# Penjumlahan Matriks
X = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]
# Penjumlahan nested loop
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(len(X[0])):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
        Z1 = result

# Penjumlahan dengan list comprehension
result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
Z2 = result

print('X = ', X)
print('Y =', Y)
print('Hasil penjumlahan dengan cara nested loop')
print('X + Y =', Z1)
print('Hasil penjumlahan dengan cara list comprehension')
print('X + Y =', Z2)