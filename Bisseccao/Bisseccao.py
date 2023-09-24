from sympy import ( sin, cos )

arquivo = open( 'Entrada.txt', 'r' )
arquivo = arquivo.readlines()
read = open( 'Saida.txt', 'w' )

a = float( arquivo[0] )
b = float( arquivo[1] )
e = float( arquivo[2] )
c = 0.0
n = 0

def isPositivo( n ):

    if n >= 0:
        return True
    else:
        return False

read.write('{:<8s}  {:<12s}  {:<12s}  {:<12s}  {:<12s} \n'.format('a', 'b', 'c', 'f(a)', 'f(c)'))

while True :

    x = a
    FdeA = eval( arquivo[3] )
    x = b
    FdeB = eval( arquivo[3] )

    c = ( a + b ) / 2
    Seila = (b - a) / a
    erro = b - a

    x = c
    FdeC = eval( arquivo[3] )

    read.write('{:<2f}  {:<12.5f}  {:<12.5f}  {:<12.5f}  {:<12.5f} \n'.format( a, b, c, FdeA, FdeC))

    if abs(FdeC) <= e :

        break

    else:        
        
        if isPositivo( FdeC ):

            b = c
        
        else:

            a = c

    n = n + 1