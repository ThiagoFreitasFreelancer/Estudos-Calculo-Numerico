from sympy import ( sin )

arquivo = open( 'Entrada.txt', 'r' )
read = open( 'Saida.txt', 'w' )
arquivo = arquivo.readlines() 

a = float( arquivo[0] )
b = float( arquivo[1] )
e = float( arquivo[2] )
c = 0.0
n = 0

read.write('{:<9s}  {:<12s}  {:<12s}  {:<12s}  {:<12s} {:<12s} \n'.format('a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'))

def isPositivo( n ):

    if n >= 0:
        return True
    else:
        return False

while True :

    x = a
    FdeA = eval( arquivo[3] )
    x = b
    FdeB = eval( arquivo[3] )

    c = ( (a * FdeB) - (b * FdeA) ) / ( FdeB - FdeA )
    erro = b - a

    x = c
    FdeC = eval( arquivo[3] )

    read.write('{:<12f} {:<12f} {:<12f} {:<12f} {:<12f} {:<12f} \n'.format( a, b, c, FdeA, FdeB, FdeC ))

    if abs(FdeC) <= e or n == 10:

        break

    else:        
        
        if isPositivo( FdeC ):

            b = c
        
        else:

            a = c

    n = n + 1