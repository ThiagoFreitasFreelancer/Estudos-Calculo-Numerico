from __future__ import division
import numpy as np
from numpy import linalg

with open('Entrada.txt', 'r') as f:
    N = int(f.readline())
    b = list(map(float, f.readline().split()))
    A = []
    for i in range(N):
        row = list(map(float, f.readline().split()))
        A.append(row)
    A = np.array(A)
vetFinal = []

for i in range(len(b)):
    vetFinal.append(0)


def main():
    global A, b, N

    aux = []
    ite = 0

    for i in range(len(vetFinal)):
        aux.append(0)

    arq = open("Saida.txt", "w")
    arq.write("Contador:\n")

    while N:
        for i in range(len(A)):
            x = b[i]
            for j in range(len(A)):
                if i != j:
                    x -= A[i][j] * aux[j]
            x /= A[i][i]
            aux[i] = round(x, 5)
        N -= 1
        ite += 1

        for i in range(len(aux)):
            vetFinal[i] = aux[i]

        arq.write("%d     " % ite)
        arq.write(str(vetFinal))
        arq.write("\n")

    arq.write(
        "\nResultado para comparacao da funcao np.linalg.solve")
    arq.write(str(np.linalg.solve(A, b)))
    arq.close()


main()




