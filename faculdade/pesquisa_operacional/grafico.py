# Feito por: Nícolas Castellani Brisque
# Criado em: 19/09/2021
# Atualizado em: 19/09/2021
"""
Descrição:
    Script feito para realizar exercício da matéria de Pesquisa Operacional
Como Utilizar:
    Apenas execute o arquivo python.
Obs:
"""

# Import das bibliotecas necessárias
import matplotlib.pyplot as plt

# Função principal que realizará o exercício
def exercicio():
    y = [i for i in range(0,8)]
    # Etapa 01 # Etapa 01 - Encontrando a reta R1
    plt.plot([0,3], [6,0], 'y', label='R1')
    plt.fill_between([0,3], [6,0],[0,0],color='yellow')
    
    # Etapa 02 - Encontrando a reta R2
    plt.plot([0,6], [5,0], 'b', label='R2')
    plt.fill_between([0,6], [5,0],[0,0],color='blue')
    
    # Etapa 02.5 - Encontrando a área entre as retas
    plt.fill_between([0,0.86,3],[5,4.28,0],[0,0,0],color='green')
    
    # Etapa 03 - Encontrando o ponto de lucro máximo
    plt.plot([0.86], [4.28], 'ro', label='L Max')
    plt.annotate('lucro máximo', xy=(0.86, 4.28), xytext=(1, 5),
                arrowprops=dict(facecolor='black', shrink=0.1),
                )
    
    # Etapa 04 - Encontrando a reta que passa pelo ponto de lucro
    plt.plot([0,2.572], [6.43,0], 'r', label='Lucro')

    # Personalizando o gráfico
    plt.grid(True, linestyle =':')
    plt.xlim([0, 7])
    plt.ylim([0, 7])
    plt.yticks(y)
    plt.title('Gráfico de Lucro')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.legend()

    # Exibindo o gráfico
    plt.draw()
    plt.show()

# Chamando a função do exercício
def main():
    exercicio()

if __name__ == '__main__':
    main()