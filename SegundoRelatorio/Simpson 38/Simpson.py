import math

def largura(intervalo,divisoes):
    h=(float(eval(intervalo[1]))-float(eval(intervalo[0])))/float(divisoes[0])
    return h
def result(fx,intervalo):
    a=fx.split('x')
    a=('('+str(intervalo)+')').join(a)
    return eval(a)
def som(fx,intervalo,h,divisoes):
    a=0
    b=divisoes/3
    for i in range(1,int(b)*2):
        c=i/3
        a=result(fx,float(eval(intervalo[0]))+(int(c)+i)*h)+a
    return a
def som1(fx,intervalo,h,divisoes):
    a=0
    b=divisoes/3
    for i in range(1,int(b)+1):
        a=result(fx,float(intervalo[0])+(3*i*h))+a
    return a
def trapezio(h,fx,intervalo,divisoes):
    r=((3*h)/8)*(result(fx[0],intervalo[0])+result(fx[0],intervalo[1])+3*som(fx[0],intervalo,h,int(divisoes[0]))+2*som1(fx[0],intervalo,h,int(divisoes[0])))
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