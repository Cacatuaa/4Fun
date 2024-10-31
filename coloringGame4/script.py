# Feito por: Cacatua
# Criado em: 
# Atualizado em: 
"""
Descrição:
    Script para clicar automaticamente nos botões do jogo Coloring Game 4.
Como Utilizar:
    Defina a quantidade de números que tem na imagem, posicione a tela com um pouco de zoom
    e execute o script
"""

import pyautogui as aut
import time

def main():
    for i in range(1,17):
        ultimo = (750, 530)
        total = 0
        while True:
            item = aut.locateCenterOnScreen(str(i) + '.PNG', confidence=0.98, region=(101,63,1202,966))
            if item == ultimo:
                print('==== Trocando de Número ====')
                aut.rightClick(item.x, item.y)
                aut.leftClick(item.x, item.y)
            elif item != None:
                aut.click(item.x, item.y)
                total += 1
                ultimo = item
            else:
                if total != 0:
                    print(f'Cliquei {total} vezes no número {i}.')
                break

if __name__ == '__main__':
    main()