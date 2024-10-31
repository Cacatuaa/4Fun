import requests
import json

# cellbit : 261289646065975296
# emotes do cacatua : 626049475068166165
def buscaMembro(id, pagina):
    jason = requests.get(pagina)
    site = jason.json()
    for pessoa in site['players']:
        if id == pessoa['id']:
            nome = pessoa["username"]
            print(f'Nome: {nome}')
            print(f'Nível: {pessoa["level"]}')
            resetarMembro(id, nome)
            
def resetarMembro(id, nome):
    resposta = (input(f'Deseja resetar o "{nome}"(s/n): ')).lower()
    if resposta == 's':
        url = 'https://mee6.xyz/api/plugins/levels/do-reset/261289646065975296/player/'
        site = url + id
        auth = input("Digite o token de autorização: ")
        try:
            requests.post(site, headers={'authorization' : auth})
        except:
            print("Algo deu errado!")
        else:
            print(f'{nome} resetado com sucesso!')

    elif resposta == 'n':
        print("Reset cancelado, voltando para o início!")
        print()
        main()

    else:
        print("Resposta inválida, voltando para o início!")
        print()
        main()
    
def main():
    # Pegando info da pessoa
    
    id = input("Digite o ID da pessoa: ")
    pagina = input("Digite a página que a pessoa se encontra: ")
    if pagina == '0':
        url = 'https://mee6.xyz/api/plugins/levels/leaderboard/261289646065975296'
        site = url
    else:
        url = 'https://mee6.xyz/api/plugins/levels/leaderboard/261289646065975296?page='
        site = url + pagina
    buscaMembro(id, site)

if __name__ == "__main__":
    main()