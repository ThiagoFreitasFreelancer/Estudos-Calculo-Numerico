from sympy import ( sin )

arquivo = open( 'Entrada.txt', 'r' )
arquivo = arquivo.readlines() 

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

    if abs(FdeC) <= e or n == 10:

        read = open( 'Saida.txt', 'w' )
        read.write( str( c ) )
        break

    else:        
        
        if isPositivo( FdeC ):

            b = c
        
        else:

            a = c

    n = n + 1