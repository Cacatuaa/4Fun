###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Pac-Man I
# Nome: Maria Clara
# RA: 
###################################################

# Definição do objeto PacMan
class PacMan:
    def __init__(self, x, y, direcao):
        self.x = x
        self.y = y
        self.direcao = direcao
        self.pontos = 0
        self.bonus = 0
        self.fim = False
        self.temp = 0 # para caso ficar andando em loop, quando chegar a um valor, parar o jogo.
    
    # Função para somar os pontos
    def somaPontos(self):
        self.pontos += 1
    
    # Função para gastar o bonus
    def gastaBonus(self):
        if self.bonus > 0:
            self.bonus -= 1
    
    # Função para somar o temporizador
    def somaTemp(self):
        self.temp += 1

# Leitura da entrada
N = int(input())
T = int(input())

mapa = []
for _ in range(N):
    mapa.append(list(input()))

# Simulação do jogo
# Encontrar a posição inicial do pacman (C)
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        if mapa[i][j] == 'C':
            x, y = i, j
            break

pacman = PacMan(x, y, 'D')

def trataPosicao(x, y, mapa):
    # Tratamento para as linhas
    if x > len(mapa) - 1:
        newX = 0
    elif x < 0:
        newX = len(mapa) - 1
    else:
        newX = x
    
    # Tratamento para as colunas
    if y > len(mapa[0]) - 1:
        newY = 0
    elif y < 0:
        newY = len(mapa[0]) - 1
    else:
        newY = y
    return newX, newY

# Função para movimentar o pacman
def movimentacao(pacman, mapa):
    tempPos = (pacman.x, pacman.y)
    direcoes = {'D': (0, 1), 'E': (0, -1), 'C': (-1, 0), 'B': (1, 0)}
    # Movimentos classificados por sentido sendo 0-Direita 1-Esquerda 2-Contrário
    # Utilizando o sentido da direita como exemplo, a sua direita é para baixo, sua esquerda é para cima e contrário é a esquerda
    movimentos = {'D': ['B', 'C', 'E'], 'E': ['C', 'B', 'D'], 'C': ['D', 'E', 'B'], 'B': ['E', 'D', 'C']}

    # Verifica se a direita do pacman tem uma parede
    x = pacman.x + direcoes[movimentos[pacman.direcao][0]][0]
    y = pacman.y + direcoes[movimentos[pacman.direcao][0]][1]
    x, y = trataPosicao(x, y, mapa)
    if mapa[x][y] == '#':
        # Verifico se em frente não é uma parede
        x = pacman.x + direcoes[pacman.direcao][0]
        y = pacman.y + direcoes[pacman.direcao][1]
        x, y = trataPosicao(x, y, mapa)
        if mapa[x][y] == '#':
            # Verifico se a esquerda não é uma parede
            x = pacman.x + direcoes[movimentos[pacman.direcao][1]][0]
            y = pacman.y + direcoes[movimentos[pacman.direcao][1]][1]
            x, y = trataPosicao(x, y, mapa)
            if mapa[x][y] == '#':
                # Caso tenha parede em todos os lados, troco a direção para onde veio o pacman
                x = pacman.x + direcoes[movimentos[pacman.direcao][2]][0]
                y = pacman.y + direcoes[movimentos[pacman.direcao][2]][1]
                pacman.direcao = movimentos[pacman.direcao][2]
            else:
                pacman.direcao = movimentos[pacman.direcao][1]
    else:
        pacman.direcao = movimentos[pacman.direcao][0]

    tempPos = (x, y)
    
    # Verifica se soma pontos
    celula = mapa[tempPos[0]][tempPos[1]]
    if celula == ' ' or celula == 'C':
        pacman.gastaBonus()
        pacman.somaTemp()
    elif celula == '.':
        pacman.somaPontos()
        pacman.gastaBonus()
        mapa[tempPos[0]][tempPos[1]] = ' '
    elif celula == '*':
        pacman.somaPontos()
        pacman.bonus += T
        mapa[tempPos[0]][tempPos[1]] = ' '
    elif celula == 'C':
        mapa[tempPos[0]][tempPos[1]] = ' '
        pacman.gastaBonus()
    elif celula == 'X' and pacman.bonus > 0:
        pacman.gastaBonus()
        mapa[tempPos[0]][tempPos[1]] = ' '
    else:
        return True
    # Para evitar de ficar em loop
    if pacman.temp > 100:
        return True
    
    pacman.x, pacman.y = tempPos
    return False

while not pacman.fim:
    pacman.fim = movimentacao(pacman, mapa)

# Impressão da saída
print(pacman.pontos)