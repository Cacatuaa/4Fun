# Feito por: Cacatua
# Criado em: 12/06/2021
# Atualizado em: 21/06/2021
"""
Descrição:
    Script para passar pelos arquivos de conversas .csv do Discord e buscar qualquer
    tipo de anexo que contenha https://cdn.discordapp.com/attachments/ na mensagem e 
    baixar na mesma pasta os arquivos.
Como Utilizar:
    Coloque o script dentro da pasta package > messages e basta só executar.
Obs:
    
TODO:
    - Fazer alguma forma deste pegar de quem é as mensagens e colocar no nome do arquivo;
    - Tratar demais erros que podem acontecer. Por exemplo: o mesmo quebra quando tem mais 
    algum outro texto na mensagem e consequentemente não consegue pegar a imagem pelo link;
"""

# Import das bibliotecas necessárias
import os
import requests

print('='*30)
print(f'Diretório atual: {os.getcwd()}')
print('='*30)

anexos = []
listaArquivos = []
teste = os.getcwd()
print(teste.split('\\'))
for subdir, dirs, files in os.walk(os.getcwd()):
    for filename in files:
        anexos = []
        filepath = subdir + os.sep + filename
        if filepath.endswith(".csv"):
            # print(filepath)
            listaArquivos.append(filepath)
            csv = open(filepath, "r", encoding="utf8")
            for line in csv:
                line = line.split(",")
                # print(line)
                for item in line:
                    if "https://cdn.discordapp.com/attachments/" in item:
                        # print(f'Esse é o item anexado {item} ==')
                        anexos.append(item[:-1])
            csv.close()
            i = 0
            for item in anexos:
                print(f'{i} - {item}')
                pasta = subdir.split('\\')
                img_data = requests.get(item).content
                with open(pasta[-1] + os.sep + str(i) + item[-4:], 'wb') as handler:
                    handler.write(img_data)
                i += 1