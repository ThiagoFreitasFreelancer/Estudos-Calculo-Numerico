import math
def largura(intervalo,divisoes):
    h=(float(intervalo[1])-float(intervalo[0]))/float(divisoes)
    return h
def result(fx,intervalo):
    a=fx.split('x')
    a=('('+str(intervalo)+')').join(a)
    return eval(a)
def som(fx,h,intervalo,divisoes):
    a=0
    for i in range(1,int(divisoes)):
        a=result(fx,float(intervalo[0])+i*h)+a
    return a
def trapezio(h,fx,intervalo,divisoes):
    r=(h/2)*(result(fx[0],intervalo[0])+result(fx[0],intervalo[1])+2*som(fx[0],h,intervalo,divisoes[0]))
    return r

def richards(intervalo, divisoes,fx):
    h1=largura(intervalo, divisoes[0])
    h2=largura(intervalo, divisoes[1])
    i1=trapezio(h1,fx,intervalo,divisoes[0])
    i2=trapezio(h2,fx,intervalo,divisoes[1])
    i=i1+pow(float(divisoes[0]),2)/(pow(float(divisoes[1]),2)-pow(float(divisoes[0]),2))*(i2-i1)
    return i
    
arq = open('inicio.txt','r')
final = open('final.txt','w')
b=0
while 1:
    intervalo=[]
    divisoes=[]
    fx=[]
    a = arq.readline()
    if not a:    
            break
    while a!='\n':
        intervalo.append(a)
        a = arq.readline()
    a = arq.readline()
    while a!='\n':
        divisoes.append(a)
        a = arq.readline()
    a=arq.readline()
    while a!='\n':
        if not a:
            print(a)
            g=richards(intervalo,divisoes,fx)
            final.write(str(g)+'\n\n')
            b=1
            break
        fx.append(a)
        a = arq.readline()
    if(b==1):
        break
    g=richards(intervalo,divisoes,fx)
    final.write(str(g)+'\n\n')
    
    
arq.close
final.close