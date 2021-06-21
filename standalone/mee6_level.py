# Feito por: Cacatua
# Criado em: 02/06/2021
# Atualizado em: 21/06/2021
"""
Descrição:
    Cálculo para verificar quantas vezes o nível atual
    da pessoa consegue atingir determinados cargos.
Como Utilizar:
    Siga as instruções do prompt e depois exibirá o resultado.
Obs:
    
"""
# Declaração de variáveis
xp = int(input("Digite seu xp atual para o próximo nível: "))
lvl = int(input("Digite o nível atual: "))
soma = 0
calouros = 1150
exp = 101675
vet = 557700
mestres = 1192550

# Cálculo para adquirir o xp total do nível do input
for i in range(lvl):
    soma = soma + (5 * (i ** 2) + (50 * i) + 100)
soma = soma + xp

# Exibição do resultado
print(f'Seu xp total é {soma}')
print(f'Seu xp total equivale a {soma//calouros}x de Calouros')
print(f'Seu xp total equivale a {soma//exp}x de Experientes')
print(f'Seu xp total equivale a {soma//vet}x de Veteranos')
print(f'Seu xp total equivale a {soma//mestres}x de Mestres')