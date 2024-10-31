def marcaLocal(matriz, linha, coluna):
    if matriz[linha][coluna] != "#":
        matriz[linha][coluna] = "+"


def main():
    matriz = [['.' for _ in range(20)] for _ in range(20)] # Criação da matriz
    linha, coluna = map(int, input().split()) # Definindo o ponto inicial
    matriz[linha][coluna] = "+"

    while True:
        entrada = input()
        if len(entrada) > 2:
            direcao = entrada.split()[0]
            passos = int(entrada.split()[1])
            if direcao == "N":
                for _ in range(0, passos):
                    linha -= 1
                    marcaLocal(matriz, linha, coluna)
            elif direcao == "S":
                for _ in range(0, passos):
                    linha += 1
                    marcaLocal(matriz, linha, coluna)
            elif direcao == "O":
                for _ in range(0, passos):
                    coluna -= 1
                    marcaLocal(matriz, linha, coluna)
            else:
                for _ in range(0, passos):
                    coluna += 1
                    marcaLocal(matriz, linha, coluna)

        else:
            if entrada == "F":
                break
            else:
                matriz[linha][coluna] = "#"

    # Exibição da matriz
    for ponto in matriz:
        print(" ".join(ponto))

if __name__ == '__main__':
    main()