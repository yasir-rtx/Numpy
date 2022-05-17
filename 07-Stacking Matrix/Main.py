import imp
import sys


import numpy as np
import os

os.system("cls")

a = np.array([1,2,3])
b = np.array([4,5,6])

# stacking adalah menggabungkan 2 buah matrix
print("Stacking horizontal : \n", np.hstack((a,b)))
print("Stacking vertikal : \n", np.vstack((a,b)))

# Matrix
aMat = np.zeros((2,2))
bMat = np.ones((2,2))

print("Stacking matrix horiozontal : \n", np.hstack((aMat, bMat)))
print("Stacking matrix vertikal : \n", np.vstack((aMat, bMat)))