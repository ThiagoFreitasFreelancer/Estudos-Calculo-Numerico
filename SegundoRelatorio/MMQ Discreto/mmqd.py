import numpy as np
from sympy import symbols


def AjusteReta(T):  # Função auxiliar do MMQ Discreto
    Npontos = len(T)
    X = np.array([p[0] for p in T])
    Y = np.array([p[1] for p in T])
    a = (Npontos*sum(Y*X)-sum(X)*sum(Y))/(sum(X*X)*Npontos-(sum(X))**2)
    b = (sum(X*X)*sum(Y)-sum(X*Y)*sum(X))/(sum(X*X)*Npontos-(sum(X))**2)
    return a, b


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

    mmqd(pontos, saida)


def mmqd(pontos, saida):
    T = pontos
    a, b = AjusteReta(T)
    saida.write(f'\n{a:.5}*x + {b:.5}')


x = symbols('x')

saida = open("saida.txt", "w")
exec("entrada1", saida)
exec("entrada2", saida)
exec("entrada3", saida)
saida.close
