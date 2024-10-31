"""
Algumas definições:
Matriz nula: todos os elementos da matriz = 0
Matriz linha: toda matriz do tipo A = (aij)1xn
Matriz coluna: toda matriz do tipo A = (aij)mx1
Matriz quadrada: toda matriz onde o número de linhas é igual ao número de colunas (m = n),
    também chamada de matriz quadrada de ordem n
Matriz identidade: toda matriz na qual os elementos da diagonal principal são iguais a 1.
Notação: In para indicar a matriz identidade de ordem n.

Cálculo:
Adição e subtração: apenas do mesmo tamanho
Multiplicação: só pode multiplicar matrizes se o número de colunas da primeira matriz é 
    igual ao número de linhas da segunda matriz.

TODO:soma/subtração de matriz
    multiplicação de matriz
"""
def exibeMatriz(matriz):
    for linha in matriz:
        print('|   ', end='')
        for item in linha:
            print(f'{item:<4}  ', end='')
        print('|')

def montaMatriz():
    linha = 0
    i = 1
    matriz = []
    print('\nDigite os valores de cada linha separados por espaço:')
    while True:
        linha = list(map(int, input(f'Linha {i}: ').split()))
        if linha[0] == 0 and len(linha) == 1:
            break
        else:
            matriz.append(linha)
            i += 1

    print('\n===== Matriz =====')
    exibeMatriz(matriz)
    return matriz

def somaMatriz(matriz, matriz2):
    print('\n===== Matrizes Somadas =====')
    for i in range(len(matriz)):
        print('|  ', end='')
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:<3} + {matriz2[i][j]:<3}', end='  ')
            matriz[i][j] = matriz[i][j] + matriz2[i][j] 
        print('|')
    
    print('\n===== Matrizes Resultante =====')
    exibeMatriz(matriz)
    
def subtraiMatriz(matriz, matriz2):
    print('\n===== Matrizes Substraidas =====')
    for i in range(len(matriz)):
        print('|  ', end='')
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:<3} - {matriz2[i][j]:<3}', end='  ')
            matriz[i][j] = matriz[i][j] - matriz2[i][j] 
        print('|')
    
    print('\n===== Matrizes Resultante =====')
    exibeMatriz(matriz)
    
def multiplicacaoEscalar(matriz):
    numero = int(input('\nDigite o número para multiplicar a matriz: '))
    # Multiplica uma matriz por um número apenas.
    print('\n===== Cálculo de Multiplicação Escalar =====')
    for i in range(len(matriz)):
        print('|  ', end='')
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:<3} * {numero:<3}', end='  ')
            matriz[i][j] = matriz[i][j] * numero 
        print('|')
    
    print('\n===== Matriz Multiplicada =====')
    exibeMatriz(matriz)
    
def determinante(matriz):
    if len(matriz[0]) == 2:
        print('Calculando determinante de matriz 2x2:')
        print(f'= ({matriz[0][0]} * {matriz[1][1]}) - ({matriz[0][1]} * {matriz[1][0]})')
        print(f'= {matriz[0][0] * matriz[1][1]} - {matriz[0][1] * matriz[1][0]}')
        print(f'= {(matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])}')
        
    elif len(matriz[0]) == 3:
        print('Calculando determinante de matriz 3x3:')
        print(f'= ({matriz[0][0]} * {matriz[1][1]} * {matriz[2][2]}) + ({matriz[0][1]} * {matriz[1][2]} * {matriz[2][0]}) + ({matriz[0][2]} * {matriz[1][0]} * {matriz[2][1]})')
        print(f'= {matriz[0][0] * matriz[1][1] * matriz[2][2]} + {matriz[0][1] * matriz[1][2] * matriz[2][0]} + {matriz[0][2] * matriz[1][0] * matriz[2][1]}')
        ladoPositivo =(matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][0]) + (matriz[0][2] * matriz[1][0] * matriz[2][1])
        print(f'= {ladoPositivo}')
        print('Calculando com o lado negativo:')
        print(f'=  ({matriz[0][2]} * {matriz[1][1]} * {matriz[2][0]})*-1 + ({matriz[0][0]} * {matriz[1][2]} * {matriz[2][1]})*-1 + ({matriz[0][1]} * {matriz[1][0]} * {matriz[2][2]})*-1')
        print(f'=  {matriz[0][2] * matriz[1][1] * matriz[2][0] * -1} + {matriz[0][0] * matriz[1][2] * matriz[2][1] * -1} + {matriz[0][1] * matriz[1][0] * matriz[2][2] * -1}')
        ladoNegativo = (matriz[0][2] * matriz[1][1] * matriz[2][0] * -1) + (matriz[0][0] * matriz[1][2] * matriz[2][1] * -1) + (matriz[0][1] * matriz[1][0] * matriz[2][2] * -1)
        print(f'= {ladoNegativo}')
        print('Calculando o resultado final:')
        print(f'= {ladoPositivo} + {ladoNegativo}')
        print(f'= {ladoPositivo + ladoNegativo}')

def main():
    while True:
        print()
        print('===== Escolha de Opções =====')
        print('1 - Multiplicação Escalar')
        print('2 - Soma de matrizes')
        print('3 - Subtração de matrizes')
        print('4 - Determinante da matriz')
        print('0 - Sair do programa')
        escolha = int(input("O que deseja escolher?! "))
        
        if escolha == 0:
            print('Saindo do programa...')
            break
        elif escolha == 1:
            matriz = montaMatriz()
            multiplicacaoEscalar(matriz)
        elif escolha == 2:
            matriz = montaMatriz()
            matriz2 = montaMatriz()
            somaMatriz(matriz, matriz2)
        elif escolha == 3:
            matriz = montaMatriz()
            matriz2 = montaMatriz()
            subtraiMatriz(matriz, matriz2)
        elif escolha == 4:
            matriz = montaMatriz()
            determinante(matriz)
        else:
            print('Digite uma escolha válida!')
    
if __name__ == '__main__':
    main()