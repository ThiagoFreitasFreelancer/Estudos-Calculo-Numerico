from sympy import ( sin, cos, tan )
import math

arquivo = open( 'Entrada.txt', 'r' )
arquivos = arquivo.readlines()
arquivo.close()

read = open( 'Saida.txt', 'w' )

a = float( arquivos[0] )
b = float( arquivos[1] )
e = float( arquivos[2] )
c = 0.0
n = 0

read.write('{:<8s}  {:<12s}  {:<12s}  {:<12s}  {:<12s} {:<12s} \n'.format('a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'))

while True :

    x = a
    FdeA = eval( arquivos[3] )
    x = b
    FdeB = eval( arquivos[3] )

    c = ( a + b ) / 2

    x = c
    FdeC = eval( arquivos[3] )

    read.write('{:<2f}  {:<12.5f}  {:<12.5f}  {:<12.5f}  {:<12.5f} {:<12.5f} \n'.format( a, b, c, FdeA, FdeB, FdeC))

    if abs(FdeC) <= e or n > 20 :

        break

    else:        
        
        if FdeC > 0:

            b = c
        
        else:

            a = c
    n = n + 1