# Leitura da vida de Jinx e Ekko
hp_jinx = int(input())
hp_ekko = int(input())

for _ in range(int(input(''))):
    hp_jinx = hp_jinx - int(input())

for _ in range(int(input(''))):
    hp_ekko = hp_ekko - int(input())

if hp_jinx < 0:
    hp_jinx = 0
if hp_ekko < 0:
    hp_ekko = 0

print('Vida da Jinx:', hp_jinx)
print('Vida do Ekko:', hp_ekko)

if hp_jinx > hp_ekko:
    print('Jinx foi a vencedora da batalha')
elif hp_jinx == hp_ekko:
    print('A batalha terminou empatada')
else:
    print('Ekko foi o vencedor da batalha')