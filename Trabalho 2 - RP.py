import numpy as np
import pandas as pd

k = 200
rho = 7000
cp = 500
a = 1
b = 1
n = 100
n_tempo = 10
delx = a/n
dely = b/n
delz = 1

T_superior = 100
T_inferior = 20
T_direita = 20
T_esquerda = 20
T = np.zeros([n,n])
for i in range(0, n, 1):
    for k in range(0, n, 1):
        T[i][k] = 20
err = 10
Erro = []
while err > 0.0001:
    A = T[0][0]
    for i in range(0, n, 1):

        for j in range(0, n, 1):

            if i == 0 and j == 0:
                T_e = T_esquerda
                T_n = T_superior
                T_s = T[i + 1][j]
                T_w = T[i][j + 1]
                T[i][j] = (T_w + T_e + T_n + T_s)/4

            if i == 0 and n - 1 > j > 0:
                T_e = T[i][j - 1]
                T_n = T_superior
                T_s = T[i + 1][j]
                T_w = T[i][j + 1]
                T[i][j] = (T_w + T_e + T_n + T_s)/4

            if i == 0 and j == n - 1:
                T_e = T[i][j - 1]
                T_n = T_superior
                T_s = T[i + 1][j]
                T_w = T_direita
                T[i][j] = (T_w + T_e + T_n + T_s)/4

            if n - 1 > i > 0 and j == 0:
                T_e = T_esquerda
                T_n = T[i - 1][j]
                T_s = T[i + 1][j]
                T_w = T[i][j + 1]
                T[i][j] = (T_w + T_e + T_n + T_s)/4

            if n - 1 > i > 0 and n - 1 > j > 0:
                T_e = T[i][j - 1]
                T_n = T[i - 1][j]
                T_s = T[i + 1][j]
                T_w = T[i][j + 1]
                T[i][j] = (T_w + T_e + T_n + T_s)/4

            if n - 1 > i > 0 and j == n - 1:
                T_e = T[i][j - 1]
                T_n = T[i - 1][j]
                T_s = T[i + 1][j]
                T_w = T_direita
                T[i][j] = (T_w + T_e + T_n + T_s)/4

            if i == n - 1 and j == 0:
                T_e = T_esquerda
                T_n = T[i - 1][j]
                T_s = T_inferior
                T_w = T[i][j + 1]
                T[i][j] = (T_w + T_e + T_n + T_s)/4

            if i == n - 1 and n - 1 > j > 0:
                T_e = T[i][j - 1]
                T_n = T[i - 1][j]
                T_s = T_inferior
                T_w = T[i][j + 1]
                T[i][j] = (T_w + T_e + T_n + T_s)/4

            if i == n - 1 and j == n - 1:
                T_e = T[i][j - 1]
                T_n = T[i - 1][j]
                T_s = T_inferior
                T_w = T_direita
                T[i][j] = (T_w + T_e + T_n + T_s)/4
    err = np.sqrt((A-T[0][0])**2)
    Erro.append(err)

# balanco de energia
Q_ver = []
Q_hor = []
for i in range(0, n-1, 1):
    for k in range(0, n-1, 1):
        q_inVert = k*abs(T[i][k] - T[i][k+1])
        q_inHori = k*abs(T[i][k] - T[i+1][k])
        Q_ver.append(q_inVert)
        Q_hor.append(q_inHori)
print(sum(Q_ver) + sum(Q_hor))

import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(6, 5))
plt.imshow(T, cmap='viridis', interpolation='nearest')
plt.xlabel('x [m]', fontsize=15)
plt.ylabel('y [m]', fontsize=15)
plt.title('Mapa de Calor')
plt.colorbar()
plt.show()

plt.figure(figsize=(6, 5))
plt.plot(Erro, linestyle='--', marker='o', color = 'blue', markersize = 4)
plt.xlabel('Iteração', fontsize=15)
plt.ylabel('Erro', fontsize=15)
plt.title('Erro Máximo')
plt.show()