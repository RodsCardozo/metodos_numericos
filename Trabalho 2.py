
import numpy as np

k = 20
rho = 7000
cp = 500
a = 1
b = 1
n = 50

delx = a/n
dely = b/n
delz = 1

delt = rho*cp*delx**2/(2*k*n*0.5)
print(delt)
Tempo = 0
T_old = np.zeros([n,n])
T = np.zeros([n,n])
for i in range(0, n, 1):
    for k in range(0, n, 1):
        T_old[i][k] = 20
T_superior = 100
T_inferior = 20
T_direita = 20
T_esquerda = 20
err = 10
cont = 1
Erro = []
while err > 0.0001:
    apx = (k*delt)/(rho*cp*delx**2)
    apy = (k*delt)/(rho*cp*delx**2)
    A = T[0][0]
    for i in range(0, n, 1):

        for j in range(0, n, 1):

            if i == 0 and j == 0:
                T_e = T_esquerda
                T_n = T_superior
                T_s = T_old[i+1][j]
                T_w = T_old[i][j+1]
                T[i][j] = T_old[i][j] + apx*(T_w + T_e - 2*T_old[i][j]) + apy*(T_n + T_s - 2*T_old[i][j])

            if i == 0 and n-1 > j > 0:
                T_e = T_old[i][j-1]
                T_n = T_superior
                T_s = T_old[i+1][j]
                T_w = T_old[i][j+1]
                T[i][j] = T_old[i][j] + apx*(T_w + T_e - 2*T_old[i][j]) + apy*(T_n + T_s - 2*T_old[i][j])

            if i == 0 and j == n-1:
                T_e = T_old[i][j-1]
                T_n = T_superior
                T_s = T_old[i+1][j]
                T_w = T_direita
                T[i][j] = T_old[i][j] + apx*(T_w + T_e - 2*T_old[i][j]) + apy*(T_n + T_s - 2*T_old[i][j])

            if n-1 > i > 0 and j == 0:
                T_e = T_esquerda
                T_n = T_old[i-1][j]
                T_s = T_old[i+1][j]
                T_w = T_old[i][j+1]
                T[i][j] = T_old[i][j] + apx*(T_w + T_e - 2*T_old[i][j]) + apy*(T_n + T_s - 2*T_old[i][j])

            if n-1 > i > 0 and n-1> j > 0:
                T_e = T_old[i][j-1]
                T_n = T_old[i-1][j]
                T_s = T_old[i+1][j]
                T_w = T_old[i][j+1]
                T[i][j] = T_old[i][j] + apx*(T_w + T_e - 2*T_old[i][j]) + apy*(T_n + T_s - 2*T_old[i][j])

            if n-1 > i > 0 and j == n-1:
                T_e = T_old[i][j-1]
                T_n = T_old[i-1][j]
                T_s = T_old[i+1][j]
                T_w = T_direita
                T[i][j] = T_old[i][j] + apx*(T_w + T_e - 2*T_old[i][j]) + apy*(T_n + T_s - 2*T_old[i][j])

            if i == n-1 and j == 0:
                T_e = T_esquerda
                T_n = T_old[i-1][j]
                T_s = T_inferior
                T_w = T_old[i][j+1]
                T[i][j] = T_old[i][j] + apx*(T_w + T_e - 2*T_old[i][j]) + apy*(T_n + T_s - 2*T_old[i][j])

            if i == n-1 and n-1 > j > 0:
                T_e = T_old[i][j-1]
                T_n = T_old[i-1][j]
                T_s = T_inferior
                T_w = T_old[i][j+1]
                T[i][j] = T_old[i][j] + apx*(T_w + T_e - 2*T_old[i][j]) + apy*(T_n + T_s - 2*T_old[i][j])

            if i == n-1 and j == n-1:
                T_e = T_old[i][j-1]
                T_n = T_old[i-1][j]
                T_s = T_inferior
                T_w = T_direita
                T[i][j] = T_old[i][j] + apx*(T_w + T_e - 2*T_old[i][j]) + apy*(T_n + T_s - 2*T_old[i][j])

    err = np.sqrt((A-T[0][0])**2)
    Erro.append(err)
    T_old = T
    cont += 1
    Tempo = Tempo + delt
print(cont)
print(Tempo)
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(5, 5))
plt.imshow(T, cmap='viridis', interpolation='nearest')
plt.xlabel('x [m]', fontsize=15)
plt.ylabel('y [m]', fontsize=15)
plt.title('Mapa de Calor')
plt.show()

plt.figure(figsize=(5, 5))
plt.plot(Erro, linestyle='--', marker='o', color = 'blue', markersize = 4)
plt.xlabel('Iteração', fontsize=15)
plt.ylabel('Erro', fontsize=15)
plt.title('Erro Máximo')
plt.show()














