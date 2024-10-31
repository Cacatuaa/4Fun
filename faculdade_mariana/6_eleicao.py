candidatos = []
votos = []
quantidade = int(input("Número de candidatos: "))

# Adquirindo todos os candidatos
for _ in range(0, quantidade):
    candidatos.append(input("Nome do candidato: "))

# Adquirindo todos os votos mais o branco e o nulo
for i in range(0, len(candidatos)+2):
    votos.append(int(input("Quantidade de votos: ")))

# Adquirindo os valores
maior = max(votos)
votos_total = sum(votos)
votos_validos = votos_total - votos[-2] - votos [-1]

# Exibição dos resultados
if maior > votos_validos/2:
    print(f'{candidatos[votos.index(maior)]} foi o vencedor da eleição')
else:
    votos2 = votos.copy() # Copiando a lista para uma nova
    votos2.remove(maior) # Removendo o maior valor
    segundo = max(votos2) # Adquirindo o segundo maior valor 
    print('Haverá segundo turno entre:')
    print(f'{candidatos[votos.index(maior)]}')
    print(f'{candidatos[votos.index(segundo)]}')
print(f'Total de votos: {votos_total}')
print(f'Votos válidos: {votos_validos}')
