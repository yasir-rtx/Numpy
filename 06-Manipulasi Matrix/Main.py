import numpy as np

a = np.array(([1,2,3],[4,5,6]))
print("Matrix a dengan ukuan : ", a.shape)

# Transpose
print("Transpose matrix a : \n", np.transpose(a))
print("Transpose matrix a : \n", a.transpose())
print("Transpose matrix a : \n", a.T)

# Flattem
print("Flatten matrix a : ", np.ravel(a))
print("Flatten matrix a : ", a.ravel())

# Reshape
print("Reshape matrix a : \n", a.reshape(6,1)) # Reshape mengebalikan nilai a yang telah dirubah

# Resize 
print("Resize matrix a : \n", a.resize(3,2)) # Resize mengubah nilai dari a