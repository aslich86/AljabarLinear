# Cara 2
import numpy as numpy
import numpy.linalg as m
from numpy.linalg import det

A= numpy.array([[2, -1, 4, 1],[1, 2, -3, 6],[-1, 1, -1, -3],[3, 0, 5, 2]])
print('A=',A)
print('det(A) =',det(A))
B=numpy.identity(4)
#reduksi baris
for i in range(0,len(B)):
    B[0][i]=A[0][i]
    B[1][i]=A[1][i]+2*A[0][i]
    B[2][i]=A[2][i]+A[0][i]
    B[3][i]=A[3][i]
    print('setelah reduksi baris kedua dan ketiga')
    print('A_reduksi =',B)
    print('det(A_reduksi)=',det(B))
