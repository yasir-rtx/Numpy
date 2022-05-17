import numpy as np
import os
os.system("cls")

A = np.array([(2,3),(1,2)])
Y = np.array([23,14])
# print(A)
# print(Y)

# Y = A.X
# X = A**-1.Y

# Mencari nilai X
A_inv = np.linalg.inv(A)
X1 = np.dot(A_inv,Y)
# print(X)

# cara lain
X2 = np.linalg.solve(A,Y)
print(X2)