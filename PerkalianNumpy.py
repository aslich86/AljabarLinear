#Perkalian dengan bantuan Numpy
from numpy import array
A = array ([
    [1, 2],
    [3, 4],
    [5, 6]])
print(A)
B = array ([
    [1, 2],
    [3, 4]])
print(B)
#Perkalian 1
C = A .dot(B)
#Perkalian 2
D = A @ B
print(D)
