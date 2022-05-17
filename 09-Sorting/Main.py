import numpy as np
import os
os.system("cls")

a = np.floor(np.random.randn(1,6)*10) #floor untuk membulatkan, lalu fungsi random

print(a)

#mencari nilai max dan min
print("nilai maksimumnya adalah", a.max()) #mencari nilai maksimum
print("posisi maksimumnya adalah", a.argmax()) #mencari posisi nilai maksimum
print("nilai minimumnya adalah", a.min()) #mencari nilai minimum
print("posisi minimumnya adalah", a.argmin()) #mencari nilai minimum

print("mengurutkan nilai a:")
print(np.sort(a)) 	 
print(np.argsort(a)) #posisi

#multiple
dtipe = [("nama", "S255"), ("tinggi", int)]
data = [("ucup",170), ("otong", 160), ("mario",180)]

e = np.array(data,dtype = dtipe)
print(e)

print(np.sort(e, order="tinggi"))