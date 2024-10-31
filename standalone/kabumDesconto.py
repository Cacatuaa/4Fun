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

url = 'https://b2lq2jmc06.execute-api.us-east-1.amazonaws.com/PROD/ofertas?campanha=natal&app=1&limite=15000&pagina=1'
site = requests.get(url)
arquivoJson = site.json()
print(arquivoJson)
produtos = arquivoJson['produtos']
desconto = int(input('Quantos % de desconto?! '))
lista = []
print(f'===== Exibindo produtos com {desconto}% de desconto =====')
while True:
    for item in produtos:
        if item['desconto'] >= desconto and item['codigo'] not in lista:
            print(f'Produto: {item["produto"]}')
            print(f'Quantidade: {item["quantidade"]}')
            print(f'Desconto: {item["desconto"]}%')
            print(f'Preço: de R${item["vlr_normal"]} por R${item["vlr_oferta"]:.2f}')
            print(f'Link do produto: https://www.kabum.com.br/produto/{item["codigo"]}')
            print()
            lista.append(item["codigo"])
    time.sleep(25)