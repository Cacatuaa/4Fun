# Feito por 
# Nícolas Castellani Brisque        RA: 1811512361
# José Agostinho Pereira Júnior     RA: 1811515521

# Função para receber valores até o usuário parar
def ReceberValores():
    validador = input("Deseja digitar um novo valor (s/n)? ")
    if (validador == "s"):
        return True
    else:
        return False

# Função para somar os valores do input
def SomarValores(lista):
    soma = 0
    for valor in lista:
        soma = soma + valor
    return soma

# Função para somar os valores pares do input
def SomarValoresPares(lista):
    somaPar = 0
    for valor in lista:
        if (valor % 2) == 0:
            somaPar = somaPar + valor
    return somaPar

# Função para somar os valores impares do input
def SomarValoresImpares(lista):
    somaImpar = 0
    for valor in lista:
        if (valor % 2) != 0:
            somaImpar = somaImpar + valor
    return somaImpar

# Função para ordenar os valores em forma crescente
def OrdenarCrescente(lista):
    ListaCrescente = sorted(lista)
    return ListaCrescente

# Função para ordenar os valores em forma descrescente
def OrdenarDescrescente(lista):
    ListaDescrescente = sorted(lista, reverse=True)
    return ListaDescrescente


# Variáveis Globais
Numeros = []

# Código Principal
while(ReceberValores()):
    Numeros.append(int(input("Digite um número: ")))

# Print da Lista e das Funções
print(Numeros)
print(OrdenarCrescente(Numeros))
print(OrdenarDescrescente(Numeros))
print(SomarValores(Numeros))
print(SomarValoresPares(Numeros))
print(SomarValoresImpares(Numeros))