
import numpy as np

k = 200
rho = 7000
cp = 500
a = 1
b = 1
n = 10
n_tempo = 1000
delx = a/n
dely = b/n
delz = 1

tempo_total = 2000
delt = tempo_total/n_tempo
Tempo = np.linspace(delt, tempo_total, n_tempo )
T_old = np.zeros([n,n])
T = np.zeros([n,n])
for i in range(0, n, 1):
    for k in range(0, n, 1):
        T_old[i][k] = 20
T_superior = 100
T_inferior = 20
T_direita = 20
T_esquerda = 20

for t in range(0, len(Tempo), 1):

    apx = (k*Tempo[t])/(rho*cp*delx**2)
    apy = (k*Tempo[t])/(rho*cp*delx**2)

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
    T_old = T
print(T)