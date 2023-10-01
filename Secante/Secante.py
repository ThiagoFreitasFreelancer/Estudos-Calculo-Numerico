from sympy import ( sin, cos, tan )
import math

arquivo = open( "Entrada.txt", "r" )
dados = arquivo.readlines()
read = open( 'Saida.txt', 'w' )

a = float( dados[0] )
b = float( dados[1] )
e = float( dados[2] )
n = 0
result = 0

arquivo.close()

read.write('{:<8s}  {:<12s}  {:<10s}  {:<10s}  {:<10s} \n'.format('a', 'b', 'erro', 'f(a)', 'f(b)'))

while True :
    
    x = a
    FdeA = eval( dados[3] )
    x = b
    FdeB = eval( dados[3] )

    aux = FdeA - FdeB
    aux1 = ( FdeA * b ) - ( FdeB * a )

    result = aux1 / aux

    read.write('{:<10.5f}  {:<10.5f}  {:<10.5f}  {:<10.5f}  {:<10.5f} \n'.format( a, b, aux1, FdeA, FdeB))

    if  abs( aux1 ) < e :

        break    

    a = b
    b = result

    if n > 20 :

        break;

    n = n + 1