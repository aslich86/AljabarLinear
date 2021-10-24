#Transpose, menukar entri baris dan kolom
X = [[12,7],
     [4,5],
     [3,8]]
print('matriks X=', X)
print()
#transpose dengan nested loop
result = [[0,0,0],
          [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[j][i] = X[i][j]
print('Transpose menggunakan nested loop')
print('Transpose X=', result)
print()
#transpose dengan list comprehensive
print('Transpose menggunakan list comprehensive')
result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
print('Transpose X =', result)


