import numpy as np

# Lendo dados do arquivo de entrada
with open('Entrada.txt', 'r') as f:
    N = int(f.readline())
    b = list(map(float, f.readline().split()))
    A = []
    for i in range(N):
        row = list(map(float, f.readline().split()))
        A.append(row)
    A = np.array(A)

# Calculando a fatoração LU
L = np.eye(N)
U = np.copy(A)

for i in range(N):
    # Pivotear se necessário
    max_index = np.argmax(np.abs(U[i:, i]))
    if max_index != 0:
        temp = np.copy(U[i, :])
        U[i, :] = U[max_index + i, :]
        U[max_index + i, :] = temp
        temp = np.copy(L[i, :i])
        L[i, :i] = L[max_index + i, :i]
        L[max_index + i, :i] = temp
        temp = b[i]
        b[i] = b[max_index + i]
        b[max_index + i] = temp

    # Eliminar abaixo da diagonal
    for j in range(i + 1, N):
        L[j, i] = U[j, i] / U[i, i]
        U[j, :] = U[j, :] - L[j, i] * U[i, :]

# Resolvendo Ly = b por substituição progressiva
y = np.zeros(N)
for i in range(N):
    y[i] = b[i] - np.dot(L[i, :i], y[:i])

# Resolvendo Ux = y por substituição regressiva
x = np.zeros(N)
for i in range(N - 1, -1, -1):
    x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

# Abrindo arquivo de saída
with open("Saida.txt", "w") as arquivo:
    # Escrevendo resultado no arquivo de saída
    arquivo.write("Solucao encontrada pela fatoracao LU: ")
    arquivo.write("\n")
    arquivo.write(str(x))