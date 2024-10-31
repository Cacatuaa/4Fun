quantidade = int(input()) # Aquisição da quantidade de números que serão inseridos
numeros = [] # Criação da lista para armezenar os números inseridos
for _ in range(0, quantidade): # Estrutura de repetição para passar pela quantidade de números inseridos
    numeros.append(int(input())) # Inserindo na lista o número inputado

for numero in numeros: # Iterando por cada número na lista "numeros"
    valor = numero # Atribuindo o numero para a variavel valor
    pares = 0 # Criação da variável que somará a quantidade de números pares
    impares = 1 # Criação da variável que somará a quantidade de números impares. Considerando que o último número sempre vai ser 1, então já temos confirmado 1 número impar
    maior = 0 # Criação da variável que armazenará o maior valor
    while valor != 1: # Estrututra de repetição para realizar a conjectura até que o valor seja 1
        if valor > maior: # Verificação se o valor atual é o maior da repetição
            maior = valor # Atribuindo o maior valor para a variável "maior"

        if valor % 2 == 0: # Verificação do valor se é par
            valor = valor / 2 # Dividindo o valor por 2 como determinado na conjectura
            pares += 1 # Somando na varíavel pares que foi encontrado um valor par
        else: # Caso o valor não seja par, ele obrigatoriamente será impar
            valor = (3 * valor) + 1 # Multiplicando o valor por 3 e somando 1 como determinado na conjectura
            impares += 1 # Somando na varíavel impares que foi encontrado um valor impar

    # Exibição dos valores para cada número inputado
    print(f"Valor inicial: {numero}") 
    print(f"Numeros Pares: {pares}")
    print(f"Numeros Impares: {impares}")
    print(f"Maior Numero: {maior:.0f}") # Na exibição dessa variável é exibido o valor com casas decimais. Ex: 50.0. O ":.0f" é justamente para tirar essas casas decimais