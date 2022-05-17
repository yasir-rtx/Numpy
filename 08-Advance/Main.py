from audioop import mul
import numpy as np
import os
os.system("cls")

# Membuat matrix dengan tipe data tertentu
a = np.array(([1,2,3],[4,5,6]), dtype=int)
b = np.array(([1,2,3],[4,5,6]), dtype=float)
c = np.array(([1,2,3],[4,5,6]), dtype=bool)
# print(b)

# Membuat matrix dengan function
def kuadrat(baris, kolom):
    return kolom**2

def jumlah(baris, kolom):
    return kolom + baris

# hasil = np.fromfunction(function, size, type)
hasil = np.fromfunction(kuadrat, (1,10), dtype=int)
jumlah = np.fromfunction(jumlah, (4,4), dtype=int)

# Membuat matrix dengan iterable
iterable = (x*x for x in range(5))
iterasi = np.fromiter(iterable, dtype=int)
# print(iterasi)

# multiple array
tipe = [('Nama', 'S255'), ('Height', int)]
data = [ # list
    ('Yelf', 187),
    ('Rvier', 183),
    ('Zacht', 192)
]

multi = np.array(data, dtype=tipe)
print(multi)
print(multi[1])