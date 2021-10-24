#Matriks Acak
from numpy import empty
a = empty([3,3])
print(a)
#Matriks Segitiga
from numpy import array
from numpy import tril
from numpy import triu
M = array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]])
print(M)
#Segitiga Bawah
lower = tril(M)
print(lower)
#Segitiga Atas
upper = triu(M)
print(upper)
#Matriks 0
from numpy import zeros
a = zeros([3,5])
print(a)
#Matriks satuan
from numpy import ones
a = ones([5])
print(a)
#Matriks Diagonal
from numpy import array
from numpy import diag
#Buatlah Matriks
M = array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]])
print(M)
#Vektor Diagonal
d = diag(M)
print(d)
D = diag(d)
print(D)
