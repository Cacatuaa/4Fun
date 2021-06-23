# Feito por: Cacatua
# Criado em: 20/05/2021
# Atualizado em: 21/06/2021
"""
Descrição:
    Script feito para formatar a string de jogos gratuitos pela Epic Games
    para publicar no canal PROMOÇÕES do Discord do Cellbit.
Como Utilizar:
    Digite primeiramente a quantidade de jogos que estão gratuitos e depois
    a url de cada jogo. 
Obs:
    
TODO: 
    - Tentar deixar a busca automática, sem ser necessário o input de url's;
"""

# Import das bibliotecas necessárias
import requests
from bs4 import BeautifulSoup
import datetime

def umJogo():
    # Adqurindo infos do site
    url = input("Digite a URL do jogo: ")
    site = requests.get(url)

    # Usando Beautiful Soup
    soup = BeautifulSoup(site.text, 'html.parser')
    # mensagens = soup.find_all('span', {'data-component':'Message'})
    nome = soup.find('span', {'class' : 'css-1he0b79-NavItemHeading__heading'})

    # Exibindo a string formatada para publicar
    print("="*25)
    print(f'**{nome.text}** está gratuito na **Epic Games**. A promoção termina **{data:%d/%m/%Y}** às **12:00**.')
    print("@LOOTS")
    print(url)
    print("="*25)

def doisJogos():
    # Adquirindo informações do primeiro site
    url1 = input("Digite a URL do primeiro jogo: ")
    url2 = input("Digite a URL do segundo jogo: ")
    site1 = requests.get(url1)
    soup1 = BeautifulSoup(site1.text, 'html.parser')
    nome1 = soup1.find('span', {'class' : 'css-1he0b79-NavItemHeading__heading'})

    # Adquirindo informações do segundo site
    site2 = requests.get(url2)
    soup2 = BeautifulSoup(site2.text, 'html.parser')
    nome2 = soup2.find('span', {'class' : 'css-1he0b79-NavItemHeading__heading'})

    # Exibindo a string formatada para publicar
    print("="*25)
    print(f'**{nome1.text}** e **{nome2.text}** estão gratuitos na **Epic Games**. A promoção termina **{data:%d/%m/%Y}** às **12:00**.')
    print("@LOOTS")
    print(url1)
    print(url2)
    print("="*25)
    
def tresJogos():
    # Adquirindo informações do primeiro site
    url1 = input("Digite a URL do primeiro jogo: ")
    url2 = input("Digite a URL do segundo jogo: ")
    url3 = input("Digite a URL do terceiro jogo: ")
    site1 = requests.get(url1)
    soup1 = BeautifulSoup(site1.text, 'html.parser')
    nome1 = soup1.find('span', {'class' : 'css-1he0b79-NavItemHeading__heading'})

    # Adquirindo informações do segundo site
    site2 = requests.get(url2)
    soup2 = BeautifulSoup(site2.text, 'html.parser')
    nome2 = soup2.find('span', {'class' : 'css-1he0b79-NavItemHeading__heading'})
    
    # Adquirindo informações do terceiro site
    site3 = requests.get(url3)
    soup3 = BeautifulSoup(site3.text, 'html.parser')
    nome3 = soup3.find('span', {'class' : 'css-1he0b79-NavItemHeading__heading'})

    # Exibindo a string formatada para publicar
    print("="*25)
    print(f'**{nome1.text}**, **{nome2.text}** e **{nome3.text}** estão gratuitos na **Epic Games**. A promoção termina **{data:%d/%m/%Y}** às **12:00**.')
    print("@LOOTS")
    print(url1)
    print(url2)
    print(url3)
    print("="*25)

def main():
    # Construindo a data de 1 semana para expirar a promoção
    global data
    day = datetime.date.today()
    data = day + datetime.timedelta(days=7)

    qtd = int(input("Quantidade de jogos grátis: "))
    if qtd == 1:
        umJogo()
    elif qtd == 2:
        doisJogos()
    elif qtd == 3:
        tresJogos()

if __name__ == "__main__":
    main()
