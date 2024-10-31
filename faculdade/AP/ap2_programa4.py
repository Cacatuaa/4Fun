# Feito por:
# Guilherme Santana Costa Alves     RA:1811514886
# José Pererira Agostinho Júnior    RA:1811515521
# Nícolas Castellani Brisque        RA:1811512361

# Classes
class Usuario:
    def __init__(self, id, nome):
        self._id = id
        self._nome = nome
        self._limite = 0
        self._cargo = ""
        self._idExemplar = []
        usuarios.append(self)

	# Getters
    @property
    def nome(self):
        return self._nome

    @property
    def id(self):
        return self._id

    @property
    def limite(self):
        return self._limite
    
    @property
    def cargo(self):
        return self._cargo
    
    @property
    def idExemplar(self):
        return self._idExemplar

    # Setters
    @idExemplar.setter
    def idExemplar(self, novo_id):
        self._idExemplar = novo_id


class Aluno(Usuario):
    def __init__(self, id, nome):
        Usuario.__init__(self, id, nome)
        self._limite = 1
        self._cargo = "Aluno"

class Professor(Usuario):
    def __init__(self, id, nome):
        Usuario.__init__(self, id, nome)
        self._limite = 3
        self._cargo = "Professor"

        
class Exemplar:
    def __init__(self, id, titulo, tipo, autor, ano):
        self._id = id
        self._titulo = titulo
        self._tipo = tipo
        self._autor = autor
        self._ano = ano
        self._estado = "Disponível"
        exemplares.append(self)

    # Getters
    @property
    def id(self):
        return self._id

    @property
    def titulo(self):
        return self._titulo

    @property
    def tipo(self):
        return self._tipo

    @property
    def autor(self):
        return self._autor
    
    @property
    def estado(self):
        return self._estado

    # Setters
    @estado.setter
    def estado(self, novo_estado):
        self._estado = novo_estado

# Funções
def Destaque(frase):
    print()
    print("="*35)
    print(frase)
    print("="*35)
    print()

# Funções relacionadas ao Usuário
def exibirUsuarios():
    print("\nLista de Usuários Cadastrados: ")
    print("ID".ljust(5) + "Nome".ljust(35) + "Cargo".ljust(15)+ "Limite Disponível".ljust(20))
    for users in usuarios:
        print(f"{str(users.id).ljust(5)}{users.nome.ljust(35)}{users.cargo.ljust(15)}{str(len(users.idExemplar))} de {str(users.limite)}")
    print()

def verificaUsuario(identidade):
    for users in usuarios:
        if users.id == identidade:
            return True
    return False

def buscaUsuario(identidade):
    for index, users in enumerate(usuarios):
        if users.id == identidade:
            usuario_escolhido = usuarios[index]
            break
    return usuario_escolhido

def cadastroUsuario(tipo):
    print("\nVocê escolheu cadastrar USUÁRIO!")
    try:
        exibirUsuarios()
        print("Digite as seguintes informações para cadastrar o usuário: ")
        identidade = int(input("ID: "))
        nome = input("Nome: ")

    except ValueError:
        print("Houve um erro tentando cadastrar, verifique se as informações foram digitas corretamente!")

    else:
        if verificaUsuario(identidade):
            print("Já existe um usuário com este ID, cadastre outro ID!")
            cadastroUsuario(tipo)
        else:
            if tipo == 0:
                Aluno(identidade, nome)
                print(f"Aluno {nome} cadastrado com sucesso!")
            else:
                Professor(identidade, nome)
                print(f"Professor {nome} cadastrado com sucesso!")

# Funções relacionadas ao Exemplar
def exibirExemplares():
    print("\nLista de Exemplares Cadastrados: ")
    print("ID".ljust(5) + "Estado".ljust(15) + "Tipo".ljust(15) + "Autor".ljust(80)+ "Título".ljust(40))
    for exemplar in exemplares:
        print(f"{str(exemplar.id).ljust(5)}{exemplar.estado.ljust(15)}{exemplar.tipo.ljust(15)}{exemplar.autor.ljust(80)}{exemplar.titulo.ljust(40)}")
    print()

def verificaExemplar(identidade):
    for exemp in exemplares:
        if exemp.id == identidade:
            return True
    return False

def buscaExemplar(identidade):
    for index, exemp in enumerate(exemplares):
        if exemp.id == identidade:
            exemplar_escolhido = exemplares[index]
            break
    return exemplar_escolhido

def cadastroExemplar():
    print("\nVocê escolheu cadastrar EXEMPLAR!")
    try:
        exibirExemplares()
        print("Digite as seguintes informações para cadastrar o exemplar: ")
        identidade = int(input("ID: "))
        tipo = input("Livro ou Periódico: ") 
        titulo = input("Título: ") 
        autor = input("Autor: ")
        ano = int(input("Ano: "))

    except:
        print("Houve um erro tentando cadastrar, verifique se as informações foram digitas corretamente!")

    else:
        if verificaExemplar(identidade):
            print("Já existe um exemplar com este ID, cadastre outro ID!")
            cadastroExemplar()
        else:
            Exemplar(identidade, titulo, tipo, autor, ano)
            print("Cadastro realizado com sucesso!")

# Funções relacionadas às operações do programa
def emprestar():
    try:
        exibirUsuarios()
        identidade = int(input("Digite o id do usuário que deseja pegar emprestado: "))

    except ValueError:
        print("Você digitou um valor inválido!")
        emprestar()

    else:
        try:
            if verificaUsuario(identidade):
                usuario_escolhido = buscaUsuario(identidade)
                print(f"Você escolheu o {usuario_escolhido.cargo} {usuario_escolhido.nome}!")

                if len(usuario_escolhido.idExemplar) == usuario_escolhido.limite:
                    print("O usuário ja atingiu o limite de empréstimos! Devolva algum exemplar e tente novamente!\n")

                else:
                    exibirExemplares()
                    id_exemplar = int(input("Digite o ID do exemplar que deseja pegar emprestado: "))

                    if verificaExemplar(id_exemplar):
                        exemplar_escolhido = buscaExemplar(id_exemplar)
                        print(f"Você escolheu o {exemplar_escolhido.tipo} {exemplar_escolhido.titulo} de {exemplar_escolhido.autor}!")

                        if exemplar_escolhido.estado == "Ocupado":
                            print(f"O estado do exemplar está {exemplar_escolhido.estado}, tente outra operação!")

                        else:
                            usuario_escolhido.idExemplar.append(exemplar_escolhido.id)
                            print(f"O estado do exemplar está {exemplar_escolhido.estado}, empréstimo realizado com sucesso!\n")
                            exemplar_escolhido.estado = "Ocupado"

                    else:
                        print("Você digitou uma opção inválida! Tente uma nova operação.")        
            else:
                print("Você digitou uma opção inválida! Tente uma nova operação.")
        except UnboundLocalError:
            print("Você digitou uma opção inválida! Tente uma nova operação.")
            
def devolver():
    try:
        exibirUsuarios()
        identidade = int(input("Digite o id do usuário que deseja devolver um exemplar: "))

    except ValueError:
        print("Você digitou um valor inválido!")
        devolver()

    else:
        try:
            if verificaUsuario(identidade):
                usuario_escolhido = buscaUsuario(identidade)
                print(f"Você escolheu o {usuario_escolhido.cargo} {usuario_escolhido.nome}!")

                if len(usuario_escolhido.idExemplar) == 0:
                    print(f"O {usuario_escolhido.cargo} {usuario_escolhido.nome} não possui nenhum exemplar em posse! Tente uma nova operação!")

                else:
                    print(f"O {usuario_escolhido.cargo} {usuario_escolhido.nome} possui o(s) seguinte(s) exemplar(es) em posse: ")
                    print("ID".ljust(5) + "Tipo".ljust(15) + "Autor".ljust(80)+ "Título".ljust(40))

                    for item in usuario_escolhido.idExemplar:
                        exemplar_emprestado = buscaExemplar(item)
                        print(f"{str(exemplar_emprestado.id).ljust(5)}{exemplar_emprestado.tipo.ljust(15)}{exemplar_emprestado.autor.ljust(80)}{exemplar_emprestado.titulo.ljust(40)}")
                    
                    try:
                        escolha = int(input("Digite o id do exemplar que deseja devolver (digite 0 se deseja sair da operação de devolução): "))

                    except ValueError:
                        print("Você digitou um valor inválido! Saindo da operação.")

                    else:
                        if escolha == 0:
                            print("Você decidiu sair da operação de devolução!")

                        elif verificaExemplar(escolha):
                            exemplar_escolhido = buscaExemplar(escolha)
                            print(f"O {usuario_escolhido.cargo} {usuario_escolhido.nome} devolveu o {exemplar_escolhido.tipo} {exemplar_escolhido.titulo}!")
                            usuario_escolhido.idExemplar.remove(exemplar_escolhido.id)
                            exemplar_escolhido.estado = "Disponível"

                        else:
                            print("Você digitou uma opção inválida! Tente uma nova operação.")

            else:
                print("Você digitou uma opção inválida!")
                devolver()
        except UnboundLocalError:
            print("Você digitou uma opção inválida! Tente uma nova operação.")

def cadastrar():
    try:
        print("Digite 0 para cadastrar ALUNO, 1 para cadastrar PROFESSOR e 2 para cadastrar EXEMPLAR")
        escolha = int(input("Sua escolha: "))
    except ValueError:
        print("Você digitou uma opção inválida!")
        cadastrar()
    else:
        if escolha > 2 or escolha < 0:
            print("Você digitou uma opção inválida!")
            cadastrar()
        else:
            if escolha == 2:
                cadastroExemplar()
            else:
                cadastroUsuario(escolha)

def main():
    global usuarios
    global exemplares
    usuarios = []
    exemplares = []

    # Cadastramento de usuários e exemplares
    Professor(1, "Santiago Robles")
    Professor(2, "Oswaldo Fuji")
    Aluno(3, "Nícolas C Brisque")
    Aluno(4, "Pedro Álvares Cabral")
    Exemplar(1, "Hamlet", "Livro", "William Shakespeare", 1603)
    Exemplar(2, "Dom Casmurro", "Livro", "Machado de Assis", 1899)
    Exemplar(3, "Sherlock Holmes", "Livro", "Arthur Conan Doyle", 2007)
    Exemplar(4, "Inference by Exclusion in Goffin Cockatoos (Cacatua goffini)", "Periódico", "Mark O'Hara, Alice M I Auersperg, Thomas Bugnyar, Ludwig Huber", 2015)
    Exemplar(5, "Megabacteriose em Calopsita (Nymphicus hollandicus)", "Periódico", "Laurien A C F, Júlio Cézar S N, Marleyne J A A L A, Mercia R B, Roseana T D M", 2017)

    repeticao = True
    Destaque("Bem vindo ao sistema da biblioteca!")

    while repeticao:
        try:
            print()
            print("Digite uma das opções a seguir ")
            print("1 - Emprestar")
            print("2 - Devolver")
            print("3 - Cadastrar")
            print("4 - Sair")
            escolha = int(input("Sua escolha: "))

        except ValueError:
            print("Você digitou um valor inválido!")

        except KeyboardInterrupt:
            print("Você decidiu sair. Até mais!")
            repeticao = False

        else:
            if escolha == 1:
                Destaque("Você escolheu a opção EMPRESTAR!")
                emprestar()

            elif escolha == 2:
                Destaque("Você escolheu a opção DEVOLVER!")
                devolver()

            elif escolha == 3:
                Destaque("Você escolheu a opção CADASTRAR!")
                cadastrar()
            
            elif escolha == 4:
                Destaque("Você escolheu a opção SAIR!")
                repeticao = False

            else:
                print("Você digitou uma opção inválida, tente novamente!\n")

if __name__ == "__main__":
    main()