import numpy as np
n = 5
L = 0.1
delx = L/n
Ti = 100
Tf = 20
K = np.zeros(n)
T = np.zeros(n)
T[0] = 100
T[n-1] = 20
j = 0
while j < 100:
    for i in range(0, n, 1):
        K[i] = 1.6 - 0.01*T[i]
    for i in range(1, n-1, 1):
        T[i] = -(T[i+1]*K[i] + T[i-1]*K[i-1])/(K[i] - 2*K[i] - K[i-1])
    j = j + 1
print(type(T))
x = np.linspace(0,0.1,n)
Temp = np.linspace(0,n,n)
for i in range(0, len(x), 1):
    Temp[i] = 160 - np.sqrt(3600 + 160000*x[i])
print(type(Temp))
import matplotlib.pyplot as plt
plt.plot(x, T, linestyle='--', marker='o', color = 'blue', markersize = 4)
plt.plot(x, Temp, linestyle='--', marker='o', color = 'red', markersize = 4)
plt.xlabel('Distânia [m]', fontsize=15)
plt.ylabel('Temperatura °C', fontsize=15)
plt.title('Perfil de temperatura')
plt.legend(['Perfil de temperatura dif. fin.','Perfil de temperatura Exato'], fontsize=14)
axes = plt.gca()
axes.yaxis.grid(b=True, color='black', alpha=0.3, linestyle='-.', linewidth=1)
plt.figure(figsize=(10.5, 9))
plt.show()
