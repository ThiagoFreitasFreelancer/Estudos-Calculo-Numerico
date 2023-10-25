import math
def largura(intervalo,divisoes):
    h=(float(eval(intervalo[1]))-float(eval(intervalo[0])))/float(divisoes[0])
    return h
def result(fx,intervalo):
    a=fx.split('x')
    a=('('+str(intervalo)+')').join(a)
    return eval(a)
def som(fx,h,intervalo,divisoes):
    a=0
    for i in range(1,int(divisoes)):
        a=result(fx,float(eval(intervalo[0]))+i*h)+a
    return a
def trapezio(h,fx,intervalo,divisoes):
    r=(h/2)*(result(fx[0],intervalo[0])+result(fx[0],intervalo[1])+2*som(fx[0],h,intervalo,divisoes[0]))
    return r

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
            h=largura(intervalo, divisoes)
            g=trapezio(h,fx,intervalo,divisoes)
            final.write(str(g)+'\n\n')
            b=1
            break
        fx.append(a)
        a = arq.readline()
    if(b==1):
        break
    h=largura(intervalo, divisoes)
    g=trapezio(h,fx,intervalo,divisoes)
    final.write(str(g)+'\n\n')
    
    
arq.close
final.close