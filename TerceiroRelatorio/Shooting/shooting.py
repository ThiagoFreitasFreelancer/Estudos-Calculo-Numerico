def passos(h,intervalo):
    aux=(float(intervalo[1])-float(intervalo[0]))/h
    return round(aux,0)

def calc3(f,x,y,z):
    aux=f.split('x')
    aux=str(x).join(aux)
    aux=aux.split('y')
    aux=str(y).join(aux)
    aux=aux.split('z')
    aux=str(z).join(aux)
    return eval(aux)

def rungekutta(intervalo,y0,z0,f,g,h):
    y=[]
    y.append(y0)
    x=float(intervalo[0])
    for i in range(int(passos(h,intervalo))):
        k1=h*calc3(f,x,y0,z0)
        l1=h*calc3(g,x,y0,z0)
        k2=h*calc3(f,x+(1/2)*h,y0+(1/2)*k1, z0+(1/2)*l1)
        l2=h*calc3(g,x+(1/2)*h,y0+(1/2)*k1, z0+(1/2)*l1)
        k3=h*calc3(f,x+(1/2)*h,y0+(1/2)*k2,z0+(1/2)*l2)
        l3=h*calc3(g,x+(1/2)*h,y0+(1/2)*k2,z0+(1/2)*l2)
        k4=h*calc3(f,x+h,y0+k3,z0+l3)
        l4=h*calc3(g,x+h,y0+k3,z0+l3)
        yh=y0+(1/6)*(k1+2*k2+2*k3+k4)
        zh=z0+(1/6)*(l1+2*l2+2*l3+l4)
        x=x+h
        y0=yh
        z0=zh
        y.append(yh)
    
    return y

def shooting(y1,y2,b,intervalo,h):
    y=[]
    a=int(passos(h,intervalo))
    for i in range(a):
        y.append(str(i)+': '+str(round((y1[i]+((b-y1[a-1])/y2[a-1])*y2[i]),3)))
    return y


arq = open('shooting.txt','r')
final = open('shootingf.txt','w')
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
        y1=a
        a = arq.readline()
        y=a
        a = arq.readline()
        z=a
        a = arq.readline()
        h=a
        a = arq.readline()
    yh1=rungekutta(intervalo,float(y0),0,y,z,float(h))
    yh2=rungekutta(intervalo,0,1,y,z,float(h))
    g=shooting(yh1,yh2,float(y1),intervalo,float(h))
    final.write(str(g)+'\n\n') 
arq.close
final.close