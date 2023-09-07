from __future__ import division 

arquivo = open( 'Entrada.txt', 'r' )
arquivo = arquivo.readlines()

a = float( arquivo[0] )
b = float( arquivo[1] )
TOL = float( arquivo[2] )

def bissecao( f, a, b, TOL, N ): 

    i = 1 
    x = a  
    fa = eval( f )  
    while (i <= N):  

        #iteracao da bissecao  
        p = a + (b-a) / 2
        x = p 
        fp = eval( f )  

        #condicao de parada  
        if ((fp == 0) or ((b-a)/2 < TOL)):
            read = open( 'Saida.txt', 'w' )
            read.write( str( p ) )
            read.close()
            return p  
        
        #bissecta o intervalo  
        #i = i+1  
        if (fa * fp > 0):  
            a = p  
            fa = fp  
        else: 
            b = p

    raise NameError('Num. max. de iter. excedido!')

print( bissecao( arquivo[3], a, b, TOL, 100 ) )