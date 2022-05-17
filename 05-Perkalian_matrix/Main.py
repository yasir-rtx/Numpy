import numpy as np

a = np.array(([1,2,3],
              [4,5,6]))

b = np.ones([3,1])

print("Matrix a : \n", a)
print("Matrix b : \n", b)

# Perkalian matrix 
# print("Perkalian : \n", a * b)

# Perkalian dot product matrix
print("Dot product : \n", np.dot(a,b))
print("Dot product : \n", a.dot(b))