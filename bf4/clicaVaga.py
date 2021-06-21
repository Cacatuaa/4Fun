# Feito por: Cacatua
# Criado em: 04/06/2021
# Atualizado em: 21/06/2021
"""
Descrição:
    Script para identificar quando um servidor no Battlefield 4 estiver com uma vaga 
    utilizando captura de tela e OCR. O mesmo clica no botão de entrar automaticamente 
    quando estiver disponível.
Como Utilizar:
    Após configurar as coordenadas do print, basta deixar o jogo na tela principal.
    o servidor que deseja entrar aberto e rodar o script.
Obs:
    Alterar o local do tesseract para a execução do mesmo.
"""

# Import das bibliotecas necessárias
import pytesseract
import pyautogui as aut
import time

def main():
    # print(aut.displayMousePosition())
    # 1508, 151 -> posição de refresh
    # 1183, 252 -> posição para entrar
    
    while True:
        aut.click(1508, 151)
        aut.screenshot('lobby.png', region=(863, 196, 120, 80))
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        lobby = pytesseract.image_to_string('lobby.png')
        lobby = lobby[19:-3]
        print(lobby)
        total = int(lobby)
        if total < 20:
            print("ENTRANDO CARAIO!!!!!!")
            aut.click(1183, 252)
            break
        time.sleep(2)

if __name__ == '__main__':
    main()