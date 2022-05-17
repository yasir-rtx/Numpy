import numpy as np

# Membuat vector 
a = np.array([1,2,3,4,5])

# Membuat vector dengan range
b = np.arange(1,10,0.5) # np.arange(batas_bawah, batas_atas, step)

# Membuat linear space
c = np.linspace(1,10,4)

# Membuat array multidimensi/matrix
d = np.array([ (1,2,3), (4,5,6)])

# vector dengan nilai 0
e = np.zeros(5)

# matrix dengan nilai 0
f = np.zeros((3,3))

# membuat vector bernilai 1
g = np.ones((3,3))

# matrix identitas
h = np.identity(5) #atau np.eye(x)

# Display array
print(c)