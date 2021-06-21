# Feito por: Cacatua
# Criado em: 26/04/2021
# Atualizado em: 21/06/2021
"""
Descrição:
    Script para identificar e clicar nas reações no cellbotinho quando
    tinha evento para adquirir dinheiro através das reações
Como Utilizar:
    Basta deixar rodando o script enquanto deixar o chat do discord 
    aberto.
Obs:
    
"""

# Import das bibliotecas necessárias
import pyautogui as aut

def main():
    i=0
    # print(aut.displayMousePosition())
    # im = aut.screenshot('teste.png', region=(380,650,100,350))
    print("===== Iniciando Cellbotinho Autoclicker =====")
    while True:
        try:
            cellbotinho = aut.locateOnScreen("cellbotinhos.png", region=(380,750,200,250))
            if cellbotinho != None:
                print("Encontrei!!!")
                cellbotinho = aut.center(cellbotinho)
                aut.click(cellbotinho.x, cellbotinho.y)
                i += 1
                print(f"Cliquei {i} vezes!")
                break
            
        except KeyboardInterrupt:
            print("Adeus!")
            break
            
        except:
            print("Não foi possível pegar o cellbotinho")

if __name__ == '__main__':
    main()