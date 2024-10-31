matriz = []
navios = {}
conversao = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
resultados = []

# Lendo a entrada da matriz com as posições dos navios
for _ in range(10):
    matriz.append(input().split())

# Verificando a quantidade de navios e armazenando num dicionário
for linha in matriz:
    for item in linha:
        if item != '.':
            if item not in navios:
                navios[item] = 1
            else:
                navios[item] = navios[item] + 1

# Lendo os palpites
for _ in range(int(input())):
    linha, coluna = input().split()
    palpite = matriz[conversao[linha]][int(coluna)-1]
    if palpite == ".":
        resultados.append('agua')
    else:
        navios[palpite] = navios[palpite] - 1
        if navios[palpite] != 0:
            resultados.append(f'atingiu o navio {palpite}')
        else:
            resultados.append(f'afundou o navio {palpite}')

# Exibindo os resultados
for resultado in resultados:
    print(resultado)