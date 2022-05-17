import numpy as np

# List Python
a = [1,2,3,4]
b = [6,7,8,9]

# Numpy array
anp = np.array([1,2,3,4])
bnp = np.array([6,7,8,9])

# Penjumlahan
jumlah_list = a + b
jumlah_array = anp + bnp # elemenwise operation

# Pengurangan
kurang_array = anp- bnp

# Perkalian
kali_array = anp * bnp

# Pembagian
bagi_array = anp / bnp

# Kuadrat
kuadrat_array = anp**2

print(kurang_array)
 
# Hal sama juga berlaku untuk matrix
# Semua operasi aritmarika pada matrix di numpy adalah perasi elemenwise