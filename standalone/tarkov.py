# Feito por: Cacatua
# Criado em: 11/03/2021
# Atualizado em: 23/06/2021
"""
Descrição:
    Script para calcular qual o item para ser craftado que possui
    mais profit no jogo Escape From Tarkov.
Como Utilizar:
    O script automaticamente irá buscar pelos valores e trazer os
    valores dos itens no prompt.
Obs:
    Necessário verificar por mudanças na composição dos itens.
TODO:
    - Deixar dinâmico a forma de horas utilizadas para fabricar o item;
"""

# Import das bibliotecas necessárias
import requests
from bs4 import BeautifulSoup

def buscaValor(url):
    print("Carregando dados...")
    site = requests.get(url)
    soup = BeautifulSoup(site.text, 'html.parser')
    item = soup.find('span', {'class' : 'price alt'})
    item = item.text[:-1]
    item = int(item.replace(',', ''))
    print("Dados carregados.")
    print("="*30)
    return item

def profitVPX(ram, ssd, bgphone, vpx, horas):
    # 3 RAM + 1 SSD + 1 broken gphone = 2 VPX
    custo = 3 * ram + ssd + bgphone
    lucro = vpx * 2 - custo
    lucro_hora = lucro / horas
    print(f"O lucro de VPX será de: {lucro}")
    print(f"O lucro por hora será de: {lucro_hora:.2f}")
    
def profitGPU(circuit, cpu, cpufan, vpx, gpu, horas):
    # 8 Circuit Board + 4 CPU + 2 CPU Fan = 1 Graphics Card
    custo = 8 * circuit + 4 * cpu + 2 * cpufan + vpx
    lucro = gpu - custo
    lucro_hora = lucro / horas
    print(f"O lucro de GPU será de: {lucro}")
    print(f"O lucro por hora será de: {lucro_hora:.2f}")
    
def profitFolder(pendrive, paper, folder, horas):
    # 3 Flash Drive + 1 Paper = 1 Folder
    custo = 3 * pendrive + paper
    lucro = folder - custo
    lucro_hora = lucro / horas
    print(f"O lucro de Folder w/ Intelligence será de: {lucro}")
    print(f"O lucro por hora será de: {lucro_hora:.2f}")

def profitUHF(bluekeycard, jammer, uhf, horas):
    # 1 Blue KeyCard + 2 Jammer = 1 UHF RFID
    custo = bluekeycard + 2 * jammer
    lucro = uhf - custo
    lucro_hora = lucro / horas
    print(f"O lucro de UHF será de: {lucro}")
    print(f"O lucro por hora será de: {lucro_hora:.2f}")
    
def main():
    vpx = buscaValor('https://tarkov-market.com/item/VPX_Flash_Storage_Module')
    ram = buscaValor('https://tarkov-market.com/item/RAM')
    ssd = buscaValor('https://tarkov-market.com/item/ssd_drive')
    broken_gphone = buscaValor('https://tarkov-market.com/item/Broken_GPhone')
    circuit = buscaValor('https://tarkov-market.com/item/Printed_circuit_board')
    cpu = buscaValor('https://tarkov-market.com/item/PC_CPU')
    cpufan = buscaValor('https://tarkov-market.com/item/CPU_Fan')
    gpu = buscaValor('https://tarkov-market.com/item/graphics_card')
    pendrive = buscaValor('https://tarkov-market.com/item/secure_flash_drive')
    paper = buscaValor('https://tarkov-market.com/item/Printer_paper')
    bluekeycard = buscaValor('https://tarkov-market.com/item/terragroup_labs_access_keycard')
    jammer = buscaValor('https://tarkov-market.com/item/signal_jammer')
    folder = buscaValor('https://tarkov-market.com/item/folder_with_intelligence')
    uhf = buscaValor('https://tarkov-market.com/item/UHF_RFID_Reader')
    
    # Exibição do resultado
    print("="*45)
    profitVPX(ram, ssd, broken_gphone, vpx, 44)
    print("="*45)
    profitGPU(circuit, cpu, cpufan, vpx, gpu, 66)
    print("="*45)
    profitFolder(pendrive, paper, folder, 31)
    print("="*45)
    profitUHF(bluekeycard, jammer, uhf, 53)
    
if __name__ == '__main__':
    main()