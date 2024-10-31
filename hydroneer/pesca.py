# Feito por: Cacatua
# Criado em: 
# Atualizado em: 
"""
Descrição:
    Script para pescar automaticamente no jogo Hydroneer
Como Utilizar:
    Deixa executando o script e vá para uma área de pesca 
"""

import pyautogui as aut
import time

# aut.displayMousePosition()
# aut.screenshot('teste.png', region=(750,400,250,250))
i = 0
while True:
    try:
        img = aut.locateCenterOnScreen('boia3.png', confidence=0.65, region=(650,350,650,350))
        if img != None:
            #print(f"Localizei nas coordenadas: {img.x} {img.y}")
            aut.leftClick()
            aut.leftClick()
            time.sleep(1)
            i += 1
        
    except:
        print(f"Peguei {i} peixes")
        break
