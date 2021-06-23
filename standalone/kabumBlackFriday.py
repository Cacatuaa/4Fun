# Feito por: Cacatua
# Criado em: 22/12/2020
# Atualizado em: 23/06/2021
"""
Descrição:
    Script para informar quando que um produto da kabum está disponível
    durante a black friday e exibir uma mensagem na tela.
Como Utilizar:
    Basta deixar executando o código que o mesmo informará quando determinado
    produto estará disponível.
Obs:
    Script foi realizado para um uso imediato então não foram tomadas medidas
    para deixar o código com uma boa redibilidade assim como provável que o 
    mesmo não funcione mais.
"""

# Import das bibliotecas necessárias
import requests
import json
import time
from datetime import datetime
import ctypes  # An included library with Python install.   

url = 'https://blackfriday.kabum.com.br/data_update.json?campanha=blackfriday'
while True:
    site = requests.get(url)
    jason = site.json()
    print(f'===== Update as {datetime.now()} =====')
    # 1660
    try:
        qtd1660 = jason['p']['197134']
    except:
        print(f'1660 = Não disponível')
    else:
        print(f'1660 = {qtd1660}')
        if qtd1660 > 0:
            ctypes.windll.user32.MessageBoxW(0, f"1660 Super Disponível!", "Black Friday Kabum", 1)

    # 2070
    try:
        qtd2070 = jason['p']['197436']
    except:
        print(f'2070 = Não disponível')
    else:
        print(f'2070 = {qtd2070}')
        if qtd2070 > 0:
            ctypes.windll.user32.MessageBoxW(0, f"2070 Disponível", "Black Friday Kabum", 1)

    time.sleep(60)