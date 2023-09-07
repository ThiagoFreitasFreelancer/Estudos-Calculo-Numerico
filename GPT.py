arquivo = open( 'Entrada.txt', 'r' )
arquivo = arquivo.readlines()

a = float( arquivo[0] )
b = float( arquivo[1] )
E = float( arquivo[2] )


def bissecao(funcao, a, b, E):
    x = a
    aux = eval( funcao )

    x = b
    aux1 = eval( funcao )

    if aux * aux1 >= 0:
        raise ValueError("A função deve ter sinais opostos em 'a' e 'b' para aplicar o método da bissecção.")
    
    while (b - a) >= E:
        # Encontre o ponto médio
        c = (a + b) / 2

        # Avalie a função no ponto médio
        x = c
        fc = eval( funcao )

        # Verifique se o valor absoluto da função no ponto médio é menor que E
        if abs(fc) < E:
            arquivo =  open("resultado_bissecao.txt", "w")
            arquivo.write( "Raiz encontrada: ", c )
            arquivo.write( "Valor da função na raiz: ", fc)
            break

        # Atualize 'a' e 'b' com base no sinal de 'fc'
        x = a
        if fc * eval( funcao ) < 0:
            b = c
        else:
            a = c

    # Abra um arquivo para escrever o resultado
    

# # Exemplo de uso:
# def funcao_exemplo(x):
#     return x**3 - x**2 + 2

# a = 0
# b = -2
# E = 0.001

raiz = bissecao( arquivo[3], a, b, E)
#print(f"Raiz encontrada: {raiz}")
