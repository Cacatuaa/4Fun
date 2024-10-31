###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Quadrados à Obra
# Nome: Maria Clara
# RA:
###################################################

def main():
    # Leitura do número de setores verticais (M) e horizontais (N).
    M, N = map(int, input().split())

    # Inicializa o terreno.
    terreno = []

    # Leitura do mapa do terreno do cliente.
    for i in range(M):
        linha_i = list(input())
        terreno.append(linha_i)

    # Itera sobre cada quadrado vazio no terreno
    maiorQuadrado = [0, 0, 0]
    for i in range(M):
        for j in range(N):
            if terreno[i][j] == ' ':
                temp = buscaQuadrado(i, j, terreno)
                if temp > 0 and temp > maiorQuadrado[0]:
                    maiorQuadrado = [temp, i, j]
    
    # Marca o maior quadrado:
    terrenoMarcado = marcaQuadrado(maiorQuadrado, terreno)

    # Imprime o terreno com o quadrado marcado.
    for linha in terrenoMarcado:
        print(linha)
    # for linha in terrenoMarcado:
    #     print(''.join(linha))

def buscaQuadrado(x, y, terreno):
    tamanho = 1
    while True:
        for i in range(len(terreno)):
            for j in range(len(terreno[i])):
                if calculaDistancia((x, y), (i, j)) == tamanho and terreno[i][j] != ' ':
                    return tamanho - 1
        tamanho += 1

def calculaDistancia(ponto1, ponto2):
    return max(abs(ponto1[0] - ponto2[0]), abs(ponto1[1] - ponto2[1]))

def marcaQuadrado(quadrado, terreno):
    x, y = quadrado[1], quadrado[2]
    tamanho = quadrado[0]
    for i in range(len(terreno)):
        for j in range(len(terreno[i])):
            if calculaDistancia((x, y), (i, j)) == tamanho:
                terreno[i][j] = '*'
    return terreno

if __name__ == "__main__":
    main()