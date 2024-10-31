# Feito por 
# Nícolas Castellani Brisque        RA: 1811512361
# José Agostinho Pereira Júnior     RA: 1811515521

# Funções
# Função para destacar uma mensagem
def Destaque(frase):
    print()
    print("="*35)
    print(frase)
    print("="*35)

# Função 1 - Abrir o arquivo de configuração
def AbrirArquivo():
    print(f'\nVocê escolheu a opção {opc1}')

    # Verificação para saber se um arquivo já está aberto
    if Arquivo_Esta_Aberto == False:

        global Arquivo_Configuracao
        Nome_Arquivo = input("Digite o nome do arquivo de configuração para abrir: ")

        try: 
            Arquivo_Configuracao = open(Nome_Arquivo + ".csv", "r+")
            
        except FileNotFoundError:
            Criar_Arquivo = input("\nAparentemente este arquivo não existe, deseja criá-lo agora?! (s/n) ")

            if Criar_Arquivo == "s":
                print('\nDigite todo o caminho do arquivo que deseja criar incluindo o próprio arquivo.\nCaso queira criar no mesmo diretório que este programa, basta digitar apenas o nome do arquivo!')
                Nome_Arquivo = input('Arquivo: ')

                # Criar o arquivo
                Arquivo_Configuracao = open(Nome_Arquivo + ".csv", "w")
                Arquivo_Configuracao.close()

                # Abrir em modo de leitura e escrita
                Arquivo_Configuracao = open(Nome_Arquivo + ".csv", "r+")
                print()
                Destaque("Arquivo foi aberto com sucesso!")
                # Retornará que o arquivo está aberto
                return True
            else:
                # Retornará que o arquivo não está aberto
                return False
            
        else:
            Destaque("Arquivo foi aberto com sucesso!")
            # Retornará que o arquivo está aberto
            return True

    # Caso já tenha um arquivo aberto, o programa dará a opção de fechar
    else:
        resposta = input("Um arquivo ja está aberto! Deseja finalizar este?! (s/n) ")

        if resposta == "s":
            Arquivo_Configuracao.close()
            Destaque("Arquivo finalizado com sucesso!")
            return False

        else:
            Destaque("Arquivo se manteve aberto, escolha uma nova opção!")
    
# Função 2 - Adicionar servidor ao arquivo de configuração
def InserirDados():
    print(f'\nVocê escolheu a opção {opc2}:')
    if Arquivo_Esta_Aberto == False:
        print("Houve um erro tentando ler o arquivo. Abra o arquivo através da opção 1 e tente novamente!")

    else:
        validaLoop = True
        while validaLoop == True:
            mensagem = input("Deseja inserir um novo servidor?! (s/n) ")

            if mensagem == "n":
                Destaque("Você decidiu não inserir nenhum novo servidor! Retornando para a opção de nova escolha.")
                validaLoop = False

            elif mensagem == "s":
                Nome = input("Digite o Nome: ")
                IP = input("Digite o IP: ")
                Dominio = input("Digite o Dominio: ")

                confirmacao = input(f'\nVocê digitou: \"{Nome}\", \"{IP}\" e \"{Dominio}\"! Deseja inserir o servidor no arquivo de configuração?! (s/n) ')
                if confirmacao == "s":
                    Arquivo_Configuracao.write(f'{Nome},{IP},{Dominio}\n')
                    Destaque("Servidor inserido no arquivo de configuração com sucesso!")

                else:
                    Destaque("Servidor não inserido no arquivo de configuração!")

            else:
                print("Por favor insira uma opção válida!")
                
# Função 3 - Exibir os itens do arquivo de configuração
def LerArquivo():
    print(f'\nVocê escolheu a opção {opc3}:')
    if Arquivo_Esta_Aberto == False:
        print("Houve um erro tentando ler o arquivo. Abra o arquivo através da opção 1 e tente novamente!")

    else:
        print()
        print("="*90)
        Arquivo_Configuracao.seek(0)
        print("Nome                                               IP                             Hostname")

        for linha in Arquivo_Configuracao:
            dados = linha.split(",")
            try:
                print(f'{dados[0].ljust(50)} {dados[1].ljust(30)} {dados[2].ljust(30)}')
            except IndexError:
                continue
            
        print("="*90)

# Função para exibir o menu de opções
def Menu():
    print()
    print("="*30)
    print("Escolha uma das opções abaixo: ")
    print(opc1)
    print(opc2)
    print(opc3)
    print(opc4)

# Variáveis Globais
validador = True
Arquivo_Esta_Aberto = False
opc1 = "1 - Abrir/fechar arquivo de configuração"
opc2 = "2 - Adicionar servidor ao arquivo de configuração"
opc3 = "3 - Visualizar arquivo de configuração"
opc4 = "4 - Sair do programa do arquivo de configuração"


# Código Principal
print("="*15, "Programa de Configuração em CSV", "="*15)

# Loop para digitar e verificar a escolha do usuário
while validador == True:
    try:
        Menu()
        Escolha = int(input("\nDigite sua escolha: "))

    # Exceção para caso o usuário digite algum valor diferente de um número
    except ValueError:
        print('Por favor, digite um número inteiro!\n')

    # Exceção para caso o usuário interrompa o programa utilizando o comando Crtl+C
    except KeyboardInterrupt:
        Destaque('Você decidiu sair. Até mais!')
        validador = False

    # Caso o passe pelo try
    else:
        # Opção 1
        if Escolha == 1:
            Arquivo_Esta_Aberto = AbrirArquivo()
        
        # Opção 2
        elif Escolha == 2:
            InserirDados()
        
        # Opção 3
        elif Escolha == 3:
            LerArquivo()

        # Opção 4
        elif Escolha == 4:
            validador = False
            if Arquivo_Esta_Aberto == True:
                Arquivo_Configuracao.close()
                Destaque("Fechando arquivo de configuração e saindo do programa!")
            else:
                Destaque('Saindo do programa, até logo!')
            exit()
        else:
            print('Por favor, insira um número válido!\n')