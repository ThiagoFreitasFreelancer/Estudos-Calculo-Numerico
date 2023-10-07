import numpy as np
from numpy.polynomial import Polynomial as P
from sympy import zeros, symbols, integrate


def f(x):
    return #inserir função aqui


def mmqc(a, b):
    base = [1, x]
    tamBase = len(base)
    matrizAux = zeros(tamBase)

    vetorF = zeros(tamBase, 1)
    cont = 0

    for i in range(tamBase):
        aux = base[i] * f(x)
        vetorF[i, 0] = integrate(aux, (x, a, b))
        for j in range(tamBase):
            aux = base[i] * base[j]
            matrizAux[i, j] = aux
            cont += 1

            if (cont == tamBase):
                for cont in range(tamBase):
                    matrizAux[i, cont] = integrate(
                        matrizAux[i, cont], (x, a, b))
                cont = 0

    resultado = matrizAux.LUsolve(vetorF)
    simb = 1
    result = 0
    for i in range(tamBase):
        result += round(resultado[i, 0], 3) * simb
        simb *= x

    saida.write(result)


def exec(file_name, saida):
    fo = open(f"{file_name}.txt", "r")
    line = fo.readlines()
    for c in range(len(line)):
        line[c] = line[c].rstrip()
    fo.close()

    lis = list()
    pontos = list()

    # Tratamento dos valores X e Y
    for c in line:
        c = c.split()
        if len(c) == 1:
            break
        for n in range(2):
            lis.append(float(c[n]))
        pontos.append(lis[:])
        lis.clear()

    mmqc(pontos, saida)


saida = open("saida.txt", "w")
exec("entrada1", saida)
exec("entrada2", saida)
exec("entrada3", saida)
saida.close
