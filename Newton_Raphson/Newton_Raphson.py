import sympy as sy
from sympy import ( sin, cos )
from sympy.interactive import init_printing
init_printing(pretty_print=True)

arquivo = open( 'Entrada.txt', 'r' )
dados = arquivo.readlines() 
arquivo.close()

n = 0
func =  dados[3] 
resultado = sy.diff( func )

teste = open( "teste.txt", "w" )
teste.write( str(resultado) )
teste.close()

teste = open( "teste.txt", "r" )
resultado = teste.readlines()
teste.close

a = float( dados[0] )
e = float( dados[2] )

while True:

    x = a
    Resultderivada = eval( dados[3] )
    ResultFuncao = eval( resultado[0] ) 

    print("a: ",a,"Result Derivada: ",Resultderivada, "Result Função: ", ResultFuncao )

    a = a - ( Resultderivada / ResultFuncao )

    if abs(a) <= e or n == 10:

        read = open( 'Saida.txt', 'w' )
        read.write( str(a) )
        break

    n = n + 1