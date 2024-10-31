# Feito por:
# Guilherme Santana Costa Alves     RA:1811514886
# José Pererira Agostinho Júnior    RA:1811515521
# Nícolas Castellani Brisque        RA:1811512361

# Fonte para criar as verificações: https://www.toppr.com/guides/maths/knowing-our-numbers/roman-numerals/

def Converter(lista_para_conversao):
    msg_erro = "Você digitou um número romano inválido!\n"

    Dicionario = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    lista = []

    try:
        for elemento in lista_para_conversao:
            lista.append(Dicionario[elemento])

    except KeyError:
        print(msg_erro)

    else:
        # Verificações
        # Verificação da repetição de V(5), L(50) e D(500)
        if lista.count(5) > 1 or lista.count(50) > 1 or lista.count(500) > 1:
            print(msg_erro)

        # Verificação de I(1) subtraindo algo diferente de V(5) ou X(10)
        elif lista.count(1) >= 1 and lista.index(1) != len(lista)-1 and lista[lista.index(1)+1] > 10:
            print(msg_erro)
        
        # Verificação de X(10) subtraindo algo diferente de L(50), C(100) ou M(1000), ou seja, subtraindo de 500
        elif lista.count(10) >= 1 and lista.index(10) != len(lista)-1 and lista[lista.index(10)+1] == 500:
            print(msg_erro)

        # Verificação de V(5) com função de subtração
        elif lista.count(5) == 1 and lista.index(5) != len(lista)-1 and lista[lista.index(5)+1] > 5:
            print(msg_erro)
        
        # Verificação de L(50) com função de subtração
        elif lista.count(50) == 1 and lista.index(50) != len(lista)-1 and lista[lista.index(50)+1] > 50:
            print(msg_erro)
        
        # Verificação de D(500) com função de subtração
        elif lista.count(500) == 1 and lista.index(500) != len(lista)-1 and lista[lista.index(500)+1] > 500:
            print(msg_erro)
        
        else:
            # Verificação de repetição sucessiva maior que 3
            soma = 1
            for i in range(0, len(lista)-1):
                if lista[i] == lista[i+1]:
                    soma += 1
                    if soma > 3:
                        break
                else:
                    soma = 1
                    
            if soma > 3:
                print(msg_erro)
            else:
                print(f"O número romano convertido é {Somar(lista)}")

def Somar(lista):
    soma = 0
    for i in range(0, len(lista)):
        if i < len(lista)-1:
            if lista[i] < lista[i+1]:
                soma -= lista[i]
            else:
                soma += lista[i]
        else:
            soma += lista[i]      
    return soma

def main():
    repeticao = True
    while repeticao:
        try:
            resposta = input("Deseja digitar um novo número romano?! (s/n) ").lower()

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