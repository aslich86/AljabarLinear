#Perkalian dua matriks
X = [[12, 7, 3],
     [4, 5, 6],
     [7,8, 9]]
print('matriks x ukuran 3 x 3 =', X)
Y = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]
print('matriks ukuran 3 x Y =', Y)
#Cara Nested Loops
print('Hasil perkalian matriks X dan Y dengan nested loops')
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
print('XY =', result)
#Cara List Comprehension
print('Hasil perkalian X dan Y menggunakan list comprehension')
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
XY = result
print('XY =', XY)

