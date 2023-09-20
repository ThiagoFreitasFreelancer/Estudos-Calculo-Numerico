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

# Abrindo arquivo de saída
with open("Saida.txt", "w") as arquivo:
    arquivo.write("Resultado da biblioteca NP Python:\n ")
    arquivo.write(str(np.linalg.solve(A, b)))
    arquivo.write("\nResultado do Metodo da Eliminacao de Gaus implementação:\n ")

    # Executando método da eliminação de Gauss
    A = np.column_stack((A, b)).astype(float)

    for i in range(N):
        aux = np.argmax(np.abs(A[i:, i]))

        if aux > 0:
            A[i + aux] = np.copy(A[i])
            A[i] = np.copy(A[i + aux])

        mult = A[i, i:] / A[i, i]

        for j in range(i + 1, N):
            A[j, i:] -= A[j, i] * mult
            A[j, :i] = 0.

    for i in range(N - 1, -1, -1):
        for j in range(N - 1, i, -1):
            A[i, -1] -= A[i, j] * A[j, -1]
        A[i, -1] /= A[i, i]

    # Escrevendo resultado no arquivo de saída
    arquivo.write(str(A[:, -1]))