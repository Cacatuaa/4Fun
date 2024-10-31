# Feito por:
# Guilherme Santana Costa Alves     RA:1811514886
# José Pererira Agostinho Júnior    RA:1811515521
# Nícolas Castellani Brisque        RA:1811512361

def Converter(lista):
    Dicionario = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    Lista_Convertida = []

    try:
        for elemento in lista:
            Lista_Convertida.append(Dicionario[elemento])

    except KeyError:
        print("Você digitou um número romano inexistente!\n")

    else:
        print(f"O número romano convertido é {Somar(Lista_Convertida)}")


def Somar(lista):
    soma = 0
    for i in range(0, len(lista)):
        if i < len(lista)-1:
            if lista[i] < lista[i+1]:
                soma = soma - lista[i]
            else:
                soma = soma + lista[i]
        else:
            soma = soma + lista[i]      
    return soma

def main():
    repeticao = True
    while repeticao:
        try:
            resposta = input("Deseja digitar um novo número romano?! (s/n)").lower()

            if resposta == "s":
                    Lista_Romano = list(input("Digite o número romano: ").upper())
                    Converter(Lista_Romano)

            elif resposta == "n":
                print("Você decidiu sair. Até mais!")
                repeticao = False
            else:
                print("Por favor, selecione uma opção valida!\n")

        except KeyboardInterrupt:
            print("\nExecução Interrompida!")
            repeticao = False

if __name__ == "__main__":
    main()