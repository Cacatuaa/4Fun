def bike():
    # Leitura de dados
    sexo = input()              # masculino ou feminino
    peso = int(input())         # quilogramas (kg)
    altura = int(input())       # centímetros (cm)

    # Seleção do modelo recomendado (masculino)
    if sexo == "M":
        if peso <= 70 and altura <= 165:
            print ("LX-39")
        if peso <= 80 and 165 < altura <= 190:
            print ("BW-02")
        if (80 < peso <= 100 and 165 < altura <= 190) or (peso <= 100 and altura > 190):
            print ("MM-107")
        if 70 < peso <= 100 and altura <= 165:
            print ("LX-40")
        if peso > 100:
            print ("CX-102")

    # Seleção do modelo recomendado (feminino)
    if sexo =="F":
        if altura <= 140:
            print ("LX-38")
        if (peso <= 90 and 140 < altura <= 155) or (peso <= 70 and 155 < altura <= 170):
            print ("BW-03")
        if (peso > 90 and 140 < altura <= 155) or (peso > 70 and 155 < altura <= 170):
            print ("CX-101")
        if peso <= 90 and altura > 170:
            print ("BW-02")
        if peso > 90 and altura > 170:
            print ("CX-102")

def main():
    while True:
        bike()

if __name__ == '__main__':
    main()