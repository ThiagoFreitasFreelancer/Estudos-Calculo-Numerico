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

    # x = a
    # FdeA = eval( arquivo[3] )

    # x = b
    # FdeB = eval( arquivo[3] )
    FdeA = a
    FdeB = b
    result = FdeA + FdeB / 2

    x = result
    FdeResult = eval( arquivo[3] )

    if FdeResult <= e:

        aux1 = isPositivo( a )
        aux2 = isPositivo( result )

        aux3 = isPositivo( result ) 
        aux4 = isPositivo( b )

        print( "a: ", aux1, "/", " result: ", aux2 )
        print( "result: ", aux3, "/", " b: ", aux4 )

        if aux1 != aux2 :

            b = result
        
        elif aux3 != aux4 :

            a = result

    else:

        read = open( 'Saida.txt', 'w' )
        read.write( str( result ) )
        break