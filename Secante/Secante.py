from sympy import ( sin )

arquivo = open( "Entrada.txt", "r" )
dados = arquivo.readlines() 

a = float( dados[0] )
b = float( dados[1] )
e = float( dados[2] )
n = 0
result = 0

arquivo.close()


while True :
    
    x = a
    FdeA = eval( dados[3] )
    x = b
    FdeB = eval( dados[3] )

    aux = FdeA - FdeB
    aux1 = ( FdeA * b ) - ( FdeB * a )

    result = aux1 / aux

    if  abs( aux1 ) < e :
        read = open( 'Saida.txt', 'w' )
        read.write( str( result ) )
        break    

    a = b
    b = result

    if n > 10 :
        break;

    n = n + 1