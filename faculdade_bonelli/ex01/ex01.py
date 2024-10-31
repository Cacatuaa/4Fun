"""
Escrever um programa para ler os valores diários da radiação solar, temperatura máxima e 
chuva do arquivo Pira_013.met (fornecido), que contém dados meteorológicos de Piracicaba 
do ano de 2013. Acrescentar o cálculo da média da radiação e da temperatura máxima nos 
dias em que a chuva for igual ou superior a 10 mm, e nos dias que a chuva for menor que 10 mm. 
Comentar o resultado.
"""

def main():
    # Obtenção dos dados do arquivo
    with open('C:/Users/Cacatua/Desktop/Programacao/python/bonelli/Pira013.txt', 'r') as f:
        lines = f.read().splitlines(); 

    # Remoção das primeiras 4 linhas
    lines = lines[4:]

    # Variáveis necessárias
    # chuva for igual ou superior a 10 mm
    radMaior10 = [] 
    tempMaxMaior10 = [] 
    # chuva for menor que 10 mm
    radMenor10 = [] 
    tempMaxMenor10 = []

    # Tratamento dos dados
    for line in lines:
        # Separação dos dados
        info = line.split()
        # Verificação da chuva
        chuva = float(info[8])
        if chuva >= 10:
            radMaior10.append(float(info[3]))
            tempMaxMaior10.append(float(info[5]))
        else:
            radMenor10.append(float(info[3]))
            tempMaxMenor10.append(float(info[5]))
    
    # Impressão dos resultados
    print(f'Dias com chuva >= 10mm: {len(radMaior10)}')
    print(f'Média da radiação: {sum(radMaior10) / len(radMaior10):.2f} kJ/m2')
    print(f'Média da temperatura: {sum(tempMaxMaior10) / len(tempMaxMaior10):.2f} °C')
    print('='*30)
    print(f'Dias com chuva < 10mm: {len(radMenor10)}')
    print(f'Média da radiação: {sum(radMenor10) / len(radMenor10):.2f} kJ/m2')
    print(f'Média da temperatura: {sum(tempMaxMenor10) / len(tempMaxMenor10):.2f} °C')

    """
    Comentário: 
    """

if __name__ == '__main__':
    main()