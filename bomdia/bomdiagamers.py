# Feito por: Cacatua
# Criado em: 19/05/2021
# Atualizado em: 21/06/2021
"""
Descrição:
    Script para ver a quantidade de membros no servidor e mandar uma
    mensagem de bom dia dizendo esta quantidade com o horário.
Como Utilizar:
    Deixe o Discord aberto no chat e ele pegará e digitará a mesnagem
    automaticamente.
Obs:
    
TODO: 
    - Fazer com que pegue apenas um número ao invés de separar a string;
"""
# Import das bibliotecas necessárias
import pytesseract
import pyautogui
from datetime import datetime


def main():
    # print(pyautogui.displayMousePosition())
    pyautogui.screenshot('membros.png', region=(1690, 85, 90, 25))
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    amigosGamersOnline = pytesseract.image_to_string('membros.png')
    # print(amigosGamersOnline)
    amigosGamersOnline = amigosGamersOnline[8:]
    numero = amigosGamersOnline.split()
    data = datetime.now()
    atual = data.strftime("%H:%M %d/%m")

    pyautogui.click(x=395, y=995)
    pyautogui.write(atual)
    pyautogui.hotkey('shift', 'enter')
    pyautogui.write(f"{numero[0]} amigos gamers online")


if __name__ == '__main__':
    main()
