from sympy import *
import numpy as np
def matriz(f):
    matrix=[]
    for i in range(len(f),0,-1):
        linha=[]
        for j in range(i):
            if j==0:
                linha.append(f[len(f)-i])
            else:
                linha.append(0)
        matrix.append(linha)
    return matrix
    
def calc(f,y):
    for j in range(1,len(f)):
        for i in range(len(f[j])):
            f[i][j]=(float(f[i+1][j-1])-float(f[i][j-1]))/(float(y[i+j])-float(y[i])) 
    return f
def som(y, t, arq):
    a=float(t[0][0])
    for i in range(len(y)-1):
        a=a+c(y,i)*float(t[0][i+1])
    aux=Poly(a,x).coeffs()
    
    for i in range(len(aux)):
        b=pow(x,len(aux)-i-1)
        d=eval(str(b))
        arq.write(str(aux[i])+'*'+str(d)+'\n')
    arq.write('\n')
    #b=np.polyval(aux, x)                                #Utilizado na resolução
    #time=27                                             #De problemas
    #print(eval(str(time).join(str(b).split('x'))))      #Em pontos
def c(y,i):
    a=x-float(y[0])
    if i>0:
        for j in range(1,i+1):
            a=a*(x-float(y[j]))
    return a
x =symbols('x')
arq = open('inicio.txt','r')
final = open('final.txt','w')


n=0
while 1:
    y=[]
    fy=[]
    a = arq.readline()
    if not a:
            break
    while a!='\n':
        y.append(a)
        a = arq.readline()
        n=n+1
    a = arq.readline()
    for i in range(n):
        fy.append(a)
        a = arq.readline()
    n=0
    m=matriz(fy)
    t=calc(m,y)
    som(y, t, final)
    final.write("\n")
arq.close
final.close