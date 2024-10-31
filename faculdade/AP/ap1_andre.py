# Enunciado do Exercíco AP1 P1 Linguagem Programação
"""
Usando python3, crie um programa que permita ao usuário entrar com uma lista de valores inteiros
( quantos valores o usuário desejar ).
Quando o usuário optar por não inserir mais valores o programa deverá:
• imprimir no console a lista de todos os valores digitados
• imprimir no console a lista de todos os valores digitados em ordem crescente
• imprimir no console a lista de todos os valores digitados em ordem decrescente
• imprimir no console a soma de todos os valores digitados
• imprimir no console a soma de todos os valores pares digitados
• imprimir no console a soma de todos os valores ímpares digitados
O programa deve obrigatóriamente conter uma funćão que retorne a soma dos valores em uma lista.

Exemplo:
input = 1, 5, 3, 2, 4 , 10 ,6, 8, 7, 9 ou 1 5 3 2 4 10 6 8 7 9
ouput = 
[ 1, 5, 3, 2, 4 , 10 ,6, 8, 7, 9 ]
[ 1, 2, 3, 4 ,5 ,6, 7, 8, 9,10 ]
[ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
55
30
25
"""

# Métodos para adicionar valores pela quantidade que o usuário digitar

# Método 1 
# Usuário digitando N valores ele vai desejar adicionar e uma estrutura de repetição que de N inputs para o usuário
"""
Entrada_Valores = int(input("Digite quantos valores você queira adicionar = "))
i = 1
while(i <= Entrada_Valores):
    Lista_De_Valores.append(input(f"Digite o valor {i} = "))
    i = i + 1
print(Lista_De_Valores)
""" 

# Método 2 (Método Utilizado no Programa AP1 P1 Linguagem Programação)
# Separar os valores num input só pelo espaço " "
"""
Lista_De_Valores = list((input("Digite os valores utilizando espaço para separá-los = ").split()))
print(Lista_De_Valores)
"""

# Método 3
# Utilizando pergunta para adicionar cada valor
"""
validador = True
while(validador == True):
    Lista_De_Valores.append(input(f"Digite o valor = "))
    if (input("Deseja digitar um novo valor? (y/n)")) == "n":
        validador = False
print(Lista_De_Valores)
"""
# Funções
def Transformar_Em_Inteiro(Lista_Para_Transformar):
    Nova_Lista = []
    for elemento in Lista_Para_Transformar:
        Nova_Lista.append(int(elemento))
    return Nova_Lista

def Organizacao_Ordem_Crescente(Lista_Para_Ordem_Crescente):
    Lista_Para_Ordem_Crescente.sort()
    return Lista_Para_Ordem_Crescente

def Organizacao_Ordem_Decrescente(Lista_Para_Ordem_Decrescente):
    Lista_Para_Ordem_Decrescente.sort(reverse=True)
    return Lista_Para_Ordem_Decrescente

def Soma(Lista_Para_Soma):
    return sum(Lista_Para_Soma)

def Soma_Numeros_Pares(Lista_Para_Soma_Pares):
    soma_par = 0
    for elemento in Lista_Para_Soma_Pares:
        if (elemento % 2) == 0:
            soma_par = soma_par + elemento
    return soma_par

def Soma_Numeros_Impares(Lista_Para_Soma_Impares):
    soma_impar = 0
    for elemento in Lista_Para_Soma_Impares:
        if (elemento % 2) != 0:
            soma_impar = soma_impar + elemento
    return soma_impar


# Código Principal
Lista_De_Valores = []

Lista_De_Valores = list((input("Digite os valores utilizando ESPAÇO para separá-los = ").split()))

Lista_De_Valores_Inteiro = Transformar_Em_Inteiro(Lista_De_Valores)

print(Lista_De_Valores_Inteiro)
print(Organizacao_Ordem_Crescente(Lista_De_Valores_Inteiro))
print(Organizacao_Ordem_Decrescente(Lista_De_Valores_Inteiro))
print(Soma(Lista_De_Valores_Inteiro))
print(Soma_Numeros_Pares(Lista_De_Valores_Inteiro))
print(Soma_Numeros_Impares(Lista_De_Valores_Inteiro))