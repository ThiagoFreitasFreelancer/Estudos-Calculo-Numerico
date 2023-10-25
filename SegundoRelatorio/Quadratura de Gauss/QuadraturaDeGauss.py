from sympy import *
import math
def quadgauss(fy,i):
    g=((float(i[1])-float(i[0]))/2)*(f(i,fy))
    return eval(str(g))

def f(i,fy):
    a=(float(i[0])+float(i[1]))/2
    b=(float(i[1])-float(i[0]))/(2*math.sqrt(3))
    f=fy.split('x')
    c=a-b
    g1=('('+str(c)+')').join(f)
    c=a+b
    g2=('('+str(c)+')').join(f)
    return eval(g1)+eval(g2)

arq = open('inicio.txt','r')
final = open('final.txt','w')

while 1:
    intervalo=[]
    a = arq.readline()
    if not a:
            break
    while a!='\n':
        intervalo.append(a)       
        a = arq.readline()
    a=arq.readline()
    fy=a
    a=arq.readline()
    final.write(str(quadgauss(fy,intervalo))+'\n\n')
arq.close
final.close