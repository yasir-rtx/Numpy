import numpy as np

a = np.arange(10)**2

# Indexing
print("ELemen pertama dari array : ", a[0])
print("Elemen terakhir dari array : ", a[-1])

# Slicing
print("Elemen dari 1-5 : ", a[0:5])
print("Elemen dari 6 sampai akhir : ", a[5:])
print("ELmen pertama sampai akhir : ", a[:5])

# Iterasi
for i in a:
    print("Nilai = ", i)