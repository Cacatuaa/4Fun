class Pessoa:
    def __init__(self, nome, cpf, lista_disciplina):
        self._nome = nome
        self._cpf = cpf
        self._lista_disciplina = lista_disciplina

	# getter
    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def lista_disciplina(self):
        return self._lista_disciplina

    # setter
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf

    @lista_disciplina.setter
    def lista_disciplina(self, novo_lista_disciplina):
        self._lista_disciplina = novo_lista_disciplina

    def pode_inserir_disciplina(self):
        if len(self._lista_disciplina) <= 3:
            return True
        else:
            False

class Aluno(Pessoa):
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        self._lista_disciplina = [""]

    def pode_inserir_disciplina(self):
        if len(self.lista_disciplina) <= 6:
            return True
        else:
            return False

class Professor(Pessoa):
    def __init__(self, nome, cpf, lista_titularidade):
        self._nome = nome
        self._cpf = cpf
        self._lista_titularidade = lista_titularidade

    # getter
    @property
    def lista_titularidade(self):
        return self._lista_titularidade

    # setter
    @lista_titularidade.setter
    def lista_titularidade(self, nova_lista):
        self._lista_disciplina = nova_lista
    
def VerificaDisciplina(aluno):
    if aluno.pode_inserir_disciplina() == False:
        print("O aluno não pode inserir mais disciplina")
    else:
        print("O aluno pode inserir mais disciplinas")
    
def main():
    aluno1 = Aluno("Nícolas Castellani Brisque", "123.456.789-01")
    professor1 = Professor("Santiago Robles", "109.876.543-21", ["Professor de Java", "Professor de Programação"])
    print(f"O nome do aluno é {aluno1.nome}, CPF: {aluno1.cpf} e está cursando {aluno1.lista_disciplina}")
    print(f"O nome do professor é {professor1.nome}, CPF: {professor1.cpf} e está possui as seguintes titularidades {professor1.lista_titularidade}")

    aluno1.lista_disciplina = ["Matemática", "Português", "Ciências", "Programação"]
    VerificaDisciplina(aluno1)

    aluno1.lista_disciplina = ["Matemática", "Português", "Ciências", "Programação", "Geografia", "História", "Inglês"]
    VerificaDisciplina(aluno1)
    

if __name__ == "__main__":
    main()
