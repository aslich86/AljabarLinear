#Latihan numpy as np
import numpy as np
A = np.array([[1, 4, 5, 12],
              [-5, 8, 9, 0],
              [-6, 7, 11, 19]])
print('A =', A)
print()
print('Menampilkan entri matriks pada sebuah baris')
print("A[0] =", A[0]) #Baris Pertama
print("A=[2] =", A[2]) #Baris Ketiga
print('entri matriks pada baris terakhir')
print("A[-1] =",A[-1])
print()
print('Menampilkan entri matriks pada sebuah kolom')
print("A[:,0]=",A[:,0]) #Kolom Pertama
print("A[:,3]=",A[:,3]) #Kolom Keempat
print('entri matriks pada kolom terakhir')
print("A[:,-1]=", A[:,-1]) #Kolom Terakhir
print()
print('Menampilkan entri matriks pada sebuah baris ke-i kolom ke-j')
#Kolom ketiga Baris pertama
print("A[0][0]=", A[0][0])
#Kolom ketiga baris kedua
print("A[1][2]=", A[1][2])
print('entri pada baris terakhir kolom terakhir')
#Kolom terakhir baris terakhir
print("A[-1][-1]=", A[-1][-1])
#Cara Lain Membuat Matriks
import numpy as np
a = np.matrix('1 2; 3 4')
print(a)
#Transpose
import numpy as np
X = np.array([[12,7],[4,5],[3,8]])
print('matriks X=', X)
XT = X.transpose()
print('transpose matriks X =')
print(XT)