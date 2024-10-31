mapa = []
caminho = []
portais = {}
naoPortais = ['N', 'S', 'L', 'O', '#', '*']
L = int(input())
# Leitura do mapa que Jayce tentará seguir
for _ in range(L):
    mapa.append(input().split())

# Leitura da posição inicial do Jayce
linha, coluna = (int(i) for i in input().split())

# Identificando os portais no mapa
for i in range(len(mapa)): # Iterando pelas linhas
    for j in range(len(mapa[i])): # Iterando pelas colunas
        conteudo = mapa[i][j]
        if conteudo not in naoPortais: # Verificando se o valor lido é um portal ou não
            if conteudo not in portais: # Vericando se já tem o portal registrado no portais
                portais[conteudo] = [] # Definindo que o conteúdo daquele dicionário será um array
            portais[conteudo].append([i,j]) # Adicionando a posição do portal no dicionário

# Seguindo o caminho do mapa
while True:
    posicao = mapa[linha][coluna]
    if posicao == "#":
        print("Jayce nao conseguiu chegar em Piltover")
        break
    elif posicao == '*':
        print("Jayce conseguiu chegar em Piltover")
        break
    else:
        # Verificando se entrou no portal ou não
        if posicao not in naoPortais:
            for portal in portais[posicao]:
                if linha != portal[0] and coluna != portal[1]:
                    linha = portal[0]
                    coluna = portal[1]
                    break
            posicao = ultimo

        if posicao == "N":
            linha = linha - 1
        elif posicao == "S":
            linha = linha + 1
        elif posicao == "O":
            coluna = coluna - 1
        elif posicao == "L":
            coluna = coluna + 1

        ultimo = posicao # Variável auxiliar para caso pegue portal, considerar a última casa andada
        if [linha, coluna] not in caminho:
            caminho.append([linha, coluna])
        else:
            print("Jayce nao conseguiu chegar em Piltover")
            break