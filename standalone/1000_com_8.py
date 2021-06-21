# Feito por: Cacatua
# Criado em: 20/05/2021
# Atualizado em: 21/06/2021
"""
Descrição: 
    Script para gerar inúmeras vezes combinações aleatórias utilizando as
    funções de soma, subtração, multiplicação e divisão para encontrar uma combinação específica 
    que o resultado seja 1000 utilizando apenas o número 8.
    
Como Utilizar:
    Basta rodar o script e ele exibirá os resultados encontrados.
Obs:
"""

# Import das bibliotecas necessárias
import random

def main():
    # Declaração das variáveis
    operadores = ['+', '-', '*', "/"]
    resultados = []
    contador = 0
    
    while True:
        total = 8
        try:
            resultado = ''
            for _ in range(8):
                i = random.randint(0, 3)
                resultado = resultado + f'{total}{operadores[i]}8= '
                if operadores[i] == '+':
                    total += 8
                elif operadores[i] == '-':
                    total -= 8
                elif operadores[i] == '*':
                    total = total * 8
                elif operadores[i] == '/':
                    total = total / 8
                if total < 0 or total > 100000:
                    break
            contador += 1
            print(f'{contador} - {resultado}')
            if total == 1000:
                resultado = resultado + str(total)
                resultados.append(resultado)
                if len(resultados) > 5:
                    break
        except:
            continue
    
    # Exibição do resultado
    print("="*30)
    print("Estas foram as combinações encontradas:")
    for item in resultados:
        print(item)

if __name__ == '__main__':
    main()