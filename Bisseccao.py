arquivo = open( 'Entrada.txt', 'r' )
arquivo = arquivo.readlines() 

a = float( arquivo[0] )
b = float( arquivo[1] )
e = float( arquivo[2] )
result = 0.0

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

    result = FdeA + FdeB / 2

    if result <= e:

        if  isPositivo( a ) != isPositivo( result ) :

            b = result
        
        elif isPositivo( result ) != isPositivo( b ):

            a = result

    else:

        read = open( 'Saida.txt', 'w' )
        read.write( str(result) )
        break