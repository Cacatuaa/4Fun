###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Níveis de Radiação
# Nome: Maria Clara
# RA: 
###################################################

# Leitura de dados
linhas = int(input())
area = []
for _ in range(linhas):
    area.append(list(input()))

# Processamento
# Função para calcular a distância entre os pontos
def calcula_distancia(ponto1, ponto2):
    return max(abs(ponto1[0] - ponto2[0]), abs(ponto1[1] - ponto2[1]))

# Função para calcular o nivel de radiação ao redor do ponto inicial
def calcula_niveis(ponto):
    # Definição das variáveis
    linha, coluna = ponto
    valorInicial = int(area[linha][coluna])
    temp = [[0] * len(area[0]) for _ in range(linhas)]
    temp[linha][coluna] = valorInicial
    k = 1
    
    # Iterando quantas vezes necessárias até zerar o nivel de radiação
    while k < valorInicial:
        # print('Para K = ', k)
        for i in range(linhas):
            for j in range(len(area[i])):
                if calcula_distancia(ponto, (i, j)) == k:
                    temp[i][j] = valorInicial - k
        k += 1
    return temp

# Pontos de radiação a serem calculados
somas = []
for linha in range(linhas):
    for coluna in range(len(area[linha])):
        if area[linha][coluna] != '0':
            somas.append(calcula_niveis((linha, coluna)))

# Niveis de radiação
niveis = [[0] * len(area[0]) for _ in range(linhas)]

# Tratamento para somar todas as matrizes
for soma in somas:
    for i in range(linhas):
        for j in range(len(area[i])):
            if niveis[i][j] == '+':
                pass
            elif niveis[i][j] + soma[i][j] > 9:
                niveis[i][j] = '+'
            else:
                niveis[i][j] += soma[i][j]

# Impressão da saída
for linha in niveis:
  print(''.join(map(str, linha)))