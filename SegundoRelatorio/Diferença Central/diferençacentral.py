import math
def calc(fy,x):
    a=fy.split('x')
    a=str(x).join(a)
    return eval(a)

def difcentral(fy,ponto,h):
    a=(calc(fy,float(ponto)+float(h))-calc(fy,float(ponto)-float(h)))/(2*float(h))
    return a

    

arq = open('inicio.txt','r')
final = open('final.txt','w')
b=0
while 1:
    a = arq.readline()
    if not a:     
            break
    fy=a
    a=arq.readline()
    ponto=a
    a=arq.readline()
    h=a
    if a=='\n':
        final.write(str(difcentral(fy,ponto,h))+'\n\n')
        a=arq.readline()
    a=arq.readline()
    final.write(str(difcentral(fy,ponto,h))+'\n\n')
arq.close
final.close