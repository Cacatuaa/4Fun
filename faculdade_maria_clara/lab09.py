###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Anonimizador de Texto
# Nome: Maria Clara
# RA:
###################################################

# Importação da biblioteca de expressão regular
import re

# Padrões RegEx
padraoNome = r'\b[A-ZÀ-Ú][a-zA-ZÀ-Úá-ú]*\b(?:\s\b[A-ZÀ-Ú][a-zA-ZÀ-Úá-ú]*\b)+'
padraoCpf = r"\d{3}\.\d{3}\.\d{3}-\d{2}|\d{9}-\d{2}"
padraoCartao = r'\b(?:\d{4}\s\d{4}\s\d{4}\s\d{4}|\d{16})\b'
padraoData = r'\b\d{2}/\d{2}/\d{4}\b'
padraoEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
padrao = f"(?P<nome>{padraoNome})|(?P<cpf>{padraoCpf})|(?P<cartao>{padraoCartao})|(?P<data>{padraoData})|(?P<email>{padraoEmail})"

# Leitura do texto
mensagens = ''
while True:
    entrada = input()
    if entrada == '-':
        break
    else:
        mensagens += entrada + '\n'

# Removendo última quebra de linha
mensagens = mensagens.rstrip('\n')

# Adquirindo informações sensíveis
informacoesSensiveis = re.finditer(padrao, mensagens)

# Associando os resultados encontrados com os tipos
informacoesMapeadas = []
for match in informacoesSensiveis:
    for tipo, valor in match.groupdict().items():
        if valor:
            informacoesMapeadas.append((valor, tipo))

# Função para converter o padrão do CPF ou cartão
def convertePadrao(palavra):
    if palavra[1] == 'cpf':
        # Se houver pontos no CPF, retira os pontos
        if '.' in palavra[0]:
            temp = palavra[0].replace('.', '')
        # Caso contrário retorna com os pontos
        else:
            temp = f'{palavra[0][0:3]}.{palavra[0][3:6]}.{palavra[0][6:]}'
    elif palavra[1] == 'cartao':
        # Se houver espaços no cartão, retira os espaços
        if ' ' in palavra[0]:
            temp = palavra[0].replace(' ', '')
        # Caso contrário retorna com os espaços
        else:
            temp = f'{palavra[0][0:4]} {palavra[0][4:8]} {palavra[0][8:12]} {palavra[0][12:]}'
    return (temp, palavra[1])

# Removendo as informações duplicadas sem perder a ordem
informacoesSensiveisUnicas = []
for item in informacoesMapeadas:
    # Validação para verificar dois cpfs/cartões em padrões diferentes
    if item[1] == 'cpf' or item[1] == 'cartao':
        if item not in informacoesSensiveisUnicas and convertePadrao(item) not in informacoesSensiveisUnicas:
            informacoesSensiveisUnicas.append(item)
    else:
        if item not in informacoesSensiveisUnicas:
            informacoesSensiveisUnicas.append(item)

# Anonimização do texto
for indice, palavra in enumerate(informacoesSensiveisUnicas):
    if palavra[1] == 'cpf' or palavra[1] == 'cartao':
        palavraConvertida = convertePadrao(palavra)
        mensagens = mensagens.replace(palavraConvertida[0], f'{palavra[1]}:{indice + 1}')

    mensagens = mensagens.replace(palavra[0], f'{palavra[1]}:{indice + 1}')

# Impressão da saída
print(mensagens)