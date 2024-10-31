# Adaptado por: Cacatua
# Criado em: 
# Atualizado em: 
"""
Descrição:
    Script para verificar se houveram mudanças em algum site
Como Utilizar:
    Alterar a variável site
"""

# Importing libraries
import time
import hashlib
from urllib.request import urlopen, Request
import datetime
  
# setting the URL you want to monitor
site = 'https://www.eventbrite.com/e/iem-rio-major-championship-tickets-72676745101'

url = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
  
# to perform a GET request and load the 
# content of the website and store it in a var
response = urlopen(url).read()
  
# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
while True:
    print(f'[{time.strftime("%H:%M:%S", time.localtime())}] - Executando...')
    try:
        # perform the get request and store it in a var
        response = urlopen(url).read()
          
        # create a hash
        currentHash = hashlib.sha224(response).hexdigest()
          
        # wait for 30 seconds
        time.sleep(30)
          
        # perform the get request
        response = urlopen(url).read()
          
        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()
  
        # check if new hash is same as the previous hash
        if newHash == currentHash:
            continue
  
        # if something changed in the hashes
        else:
            # notify
            print(f'[{time.strftime("%H:%M:%S", time.localtime())}] - Alguma coisa mudou')
  
            # again read the website
            response = urlopen(url).read()
  
            # create a hash
            currentHash = hashlib.sha224(response).hexdigest()
  
            # wait for 30 seconds
            time.sleep(10)
            continue
              
    # To handle exceptions
    except Exception as e:
        print(f"Erro: {e}")