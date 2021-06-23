# Feito por Cacatua - 22/10/2020
# Baseado no seguinte projeto: https://gabrielf9.github.io/enigma_do_medo/
# Caso não tenha requests instalado, utilize: "pip install requests" e "pip install matplotlib"
# Atualizado em: 23/06/2021
"""
Descrição:
    Script feito para adquirir a quantidade do projeto do Engima do Medo da Ordem Paranormal e
    elaborar um gráfico se baseando nas quantidades de cada produto vendido e aguardando aprovação.
Como Utilizar:
    Basta executar o script que será gerado o gráfico onde você pode salvá-lo se quiser.
Obs:
    
"""

# Import das bibliotecas necessárias
import requests
import matplotlib.pyplot as plt 
import numpy as np

class Itens:
    def __init__(self, identidade, titulo, preco, pago, pendente, total_pago, total_pendente, total):
        self._identidade = identidade
        self._titulo = titulo
        self._pago = pago
        self._preco = preco
        self._pendente = pendente
        self._total_pago = total_pago
        self._total_pendente = total_pendente
        self._total = total

    # Getters
    @property
    def identidade(self):
        return self._identidade
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def preco(self):
        return self._preco

    @property
    def pago(self):
        return self._pago

    @property
    def pendente(self):
        return self._pendente
    
    @property
    def total_pago(self):
        return self._total_pago

    @property
    def total_pendente(self):
        return self._total_pendente

    @property
    def total(self):
        return self._total

    # Setter
    @identidade.setter
    def identidade(self, novo_identidade):
        self._identidade = novo_identidade

def organizaLista(lista):
    organizado = sorted(lista, key = lambda x: x.preco)
    i = 0
    for item in organizado:
        item.identidade = str(i)
        i += 1
    return organizado

def mostraGrafico(recompensas): 
    labels = []
    listaPagos = []
    listaPendentes = []
    tick_label = []
    width = 0.35

    for elem in recompensas:
        labels.append(elem.identidade)
        listaPagos.append(int(elem.pago))
        listaPendentes.append(int(elem.pendente))
        tick_label.append('R$' + str(elem.preco))

    x = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(14, 7))
    rects1 = ax.bar(x - width/2, listaPagos, width, label='Pagos', color='purple', edgecolor='black')
    rects2 = ax.bar(x + width/2, listaPendentes, width, label='Pendentes', color='orange', edgecolor='black')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Quantidade')
    ax.set_title('Quantidade de Recompensas Pagas e Pendentes')
    ax.set_xticks(x)
    ax.set_xticklabels(tick_label)
    ax.legend()


    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    fig.canvas.set_window_title('Gráfico Enigma do Medo')
    fig.tight_layout()
    plt.show()

    # plt.bar(left, height, tick_label = tick_label, 
    #         width = 0.5, color = ['green', 'blue']) 
    

def main():
    i = 0
    recompensas = []

    site = requests.get('https://api.catarse.me/reward_details?project_id=eq.122021')
    novo_site = site.json()

    for item in novo_site:
        recompensa = Itens(i, item['title'], int(item['minimum_value']), item['paid_count'], item['waiting_payment_count'], (float(item['minimum_value']) * float(item['paid_count'])), (float(item['minimum_value']) * float(item['waiting_payment_count'])), (int(item['paid_count']) * int(item['minimum_value']) + int(item['waiting_payment_count']) * int(item['minimum_value'])))
        recompensas.append(recompensa)
        i += 1

    organizado = organizaLista(recompensas)
    mostraGrafico(organizado)
    """
    while True:
        print("=" * 35)
        print("Menu de Operações")
        print("1 - Ver o título")
        print("2 - Ver o preço")
        print("3 - Ver a quantidade paga")
        print("4 - Ver o total pago")
        print("5 - Ver a quantidade pendente")
        print("6 - Ver o total pendente")
        print("7 - Ver o total pago e pendente")
        print("8 - Ver o total arrecadado")
        print("9 - Sair do programa")
        opcoes = input("Selecione quais opções deseja ver colocando o dígito da operação separando por espaços: ") 

        if opcoes == '9':
            print("Você decidiu sair, até mais!")
            break

        else:
            print()
            mostraOperacoes(opcoes.split(), recompensas)
"""
if __name__ == "__main__":
    main()