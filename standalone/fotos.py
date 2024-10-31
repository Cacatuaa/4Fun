import requests
from bs4 import BeautifulSoup
import os

url = 'https://fotop.com.br/fotos/eventos/busca/id/6564/evento/26210/busca/numero'
site = requests.get(url)
soup = BeautifulSoup(site.text, 'html.parser')
lista = soup.find_all('img')
fotos = []
for item in lista:
    #print(item['src'])
    if "https://fotopbr.s3.amazonaws.com/fotos/arquivo" in item['src'] and item['src'] not in fotos:
        fotos.append(item['src'])

caminho = 'C:/Users/Cacatua/Desktop/fotos'
pasta = os.path.realpath(caminho)
i = 0
for item in fotos:
    img_data = requests.get(item).content
    with open(pasta + os.sep + str(i) + item[-4:], 'wb') as handler:
        handler.write(img_data)
    print(f'Baixando imagem: {i}')
    i += 1
    
print('\nFotos baixadas com sucesso')