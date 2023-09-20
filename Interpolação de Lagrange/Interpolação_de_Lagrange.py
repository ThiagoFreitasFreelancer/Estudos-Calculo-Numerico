from sympy import *

def som(y):
    aux=[]
    for i in range(len(y)):
        a=c(y,i,x)/c(y,i,float(y[i]))
        aux.append(a)
    return aux
def c(y,i,a):
    z=1
    for j in range(len(y)):
        if j!=i:
            z=z*(a-float(y[j]))
    return z

def prod(fy,aux,arq):
    result=0
    for i in range(len(fy)):
        result=result+float(fy[i])*aux[i]
    a=Poly(result,x).coeffs()
    for i in range(len(a)):
        b=pow(x,len(a)-i-1)
        c=eval(str(b))
        arq.write(str(a[i])+'*'+str(c)+'\n')
    arq.write('\n')
    
x =symbols('x')
arq = open('Entrada.txt','r')
final = open('Saida.txt','w')


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
    ax=som(y)
    prod(fy,ax,final)
    final.write("\n")
arq.close
final.close