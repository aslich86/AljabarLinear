import numpy as numpy
import numpy.linalg as m
from numpy.linalg import det

A= numpy.array([[2, -1, 4, 1],[1, 2, -3, 6],[-1, 1, -1, -3],[3, 0, 5, 2]])
print('A =',A)
#minor entri a14, menghapus baris ke-1 dan kolom ke-4
M14=numpy.identity(3)
for i in range(0,len(M14)) :
    for j in range(0,len(M14)):
        M14[i][j]=A[i+1][j]


print('Submatriks entri a14 =',M14)
print('Minor entri a14 =',det(M14))
print('Kofaktor entri a14 =',-det(M14))



