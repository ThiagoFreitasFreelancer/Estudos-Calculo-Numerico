def passos(h,intervalo):
    aux=(float(intervalo[1])-float(intervalo[0]))/h
    return round(aux,0)

def calc2(f,x,y):
    aux=f.split('x')
    aux=str(x).join(aux)
    aux=aux.split('y')
    aux=str(y).join(aux)
    return eval(aux)

def heun(x,y0,f,h,intervalo):
    y=[]
    for i in range(int(passos(h,intervalo))):
        y01=y0+calc2(f,x,y0)*h
        yh=y0+((calc2(f,x,y0)+calc2(f,x+h,y01))/2)*h
        y0=yh
        x=x+h
        y.append(str(i)+': '+str(round(yh,3)))
    return y


arq = open('heun.txt','r')
final = open('heunf.txt','w')
while 1:
    intervalo=[]
    a = arq.readline()
    if not a:  
        break
    while a!='\n':
        intervalo.append(a)
        a = arq.readline()
    a=arq.readline()
    while a!='\n':
        if not a:
            break        
        y0=a
        a = arq.readline()
        f=a
        a = arq.readline()
        h=a
        a = arq.readline()
    
    g=heun(0,float(y0),f,float(h), intervalo)
    
    final.write(str(g)+'\n\n') 
arq.close
final.close