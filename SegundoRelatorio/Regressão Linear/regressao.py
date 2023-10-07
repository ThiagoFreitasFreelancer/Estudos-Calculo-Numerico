def regressao(pontos, saida):
    x = list()
    y = list()
    for c in pontos:
        x.append(c[0])
        y.append(c[1])
    n = len(x)
    somx = somy = somqx = somxy = 0
    

    for c in y:
        somy += c

    for c in x:
        somx += c
        somqx += c ** 2

    for c in range(n):
        somxy += x[c] * y[c]

    a1 = (n * somxy - somx * somy) / (n * somqx - somx ** 2)
    a0 = somy / n - a1 * (somx / n)

    saida.write(f'\ny = {a0:.7f} + {a1:.7f}x')

#Abrindo o arquivo para pegar o que precisa e os fechando
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

    regressao(pontos, saida)

saida = open("saida.txt", "w")
exec("entrada1", saida)
exec("entrada2", saida)
exec("entrada3", saida)
saida.close