import numpy as np
import os
os.system("cls")

a = np.array([1,2,0])
b = np.array([3,4,0])

#perkalian dot
c1 = np.dot(a,b)
print(c1)

#perkalian cross
c2 = np.cross(a,b)
c3 = np.cross(b,a)
print(c2)
print(c3)