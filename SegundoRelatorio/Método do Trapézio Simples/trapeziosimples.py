import math


def largura(intervalo):
    h = (float(eval(intervalo[1]))-float(eval(intervalo[0])))/1
    return h


def result(fx, intervalo):
    a = fx.split('x')
    b = ('('+str(intervalo)+')').join(a)
    return eval(str(b))


def trapezio(h, fx, intervalo):
    r = (h/2)*(result(fx[0], intervalo[0])+result(fx[0], intervalo[1]))
    return r


arq = open('inicio.txt', 'r')
final = open('final.txt', 'w')
b = 0
while 1:
    intervalo = []
    fx = []
    a = arq.readline()
    if not a:
        break
    while a != '\n':
        intervalo.append(a)
        a = arq.readline()
    a = arq.readline()
    while a != '\n':
        if not a:
            h = largura(intervalo)
            g = trapezio(h, fx, intervalo)
            final.write(str(g)+'\n\n')
            b = 1
            break
        fx.append(a)
        a = arq.readline()
    if(b == 1):
        break
    h = largura(intervalo)
    g = trapezio(h, fx, intervalo)
    final.write(str(g)+'\n\n')


arq.close
final.close
