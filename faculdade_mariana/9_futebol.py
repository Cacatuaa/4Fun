def calculaPontos(indice, jogador):
    # Calculando a pontuação a ser dada para o jogador
    if indice == 0: # Primeiro lugar
        pontos = 6
    elif indice == 1: # Segundo lugar
        pontos = 4
    elif indice == 2: # Terceiro lugar
        pontos = 3
    elif indice == 3: # Quarto lugar
        pontos = 2
    else: # Quinto lugar
        pontos = 1

    # Verificando se o jogador existe no dicionário:
    if jogador not in votacao:
        votacao[jogador] = pontos
    else:
        votacao[jogador] = votacao[jogador] + pontos

def main():
    # Inicialização das variáveis
    global votacao
    votacao = {}
    n = int(input())

    # Iterando sobre a quantidade de vezes inputada
    for _ in range(0,n):
        i = 0
        while i < 5:
            jogador = input()
            calculaPontos(i, jogador)
            i += 1

    # Ordenando o dicionário para pegar o maior valor
    ordenado = {}
    for chave in reversed(sorted(votacao, key=votacao.get)):
        ordenado[chave] = votacao[chave]

    # Exibindo os jogadores com maiores pontos em forma decrescente
    for jogador, pontos in ordenado.items():
        print(f'{jogador}: {pontos}')

if __name__ == '__main__':
    main()