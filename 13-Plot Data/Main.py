import numpy as np
import matplotlib.pyplot as plt
import os
os.system("cls")

# Persamaan garis y = 2x + 3
x = np.arange(0,11,1)
y = 2*x + 3
print(x)
print(y)

plt.figure(1)
plt.plot(x,y)

# Lingkaran
r = 5
angle = np.arange(0,2*np.pi,0.01)
x2 = r * np.cos(angle)
y2 = r * np.sin(angle)

plt.figure(2)
plt.plot(x2,y2)
plt.show()