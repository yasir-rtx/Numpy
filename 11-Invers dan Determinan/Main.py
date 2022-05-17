import numpy as np
import os
os.system("cls")

a = np.array([(1,-1),(1,1)])

# Inverse
a_inv = np.linalg.inv(a)
# print(a_inv)
# Uji kebenaran inverse
# print("Uji: \n", np.dot(a,a_inv))

# Determinan
a_det = np.linalg.det(a)
print(a_det)