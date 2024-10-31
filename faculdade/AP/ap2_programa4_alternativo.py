# Feito por:
# Guilherme Santana Costa Alves     RA:1811514886
# José Pererira Agostinho Júnior    RA:1811515521
# Nícolas Castellani Brisque        RA:1811512361

class Usuario:
    def __init__(self, id, nome):
        self._id = id
        self._nome = nome
        self._limite = 0
        self._emprestimo = 0

	# Getters
    @property
    def limite(self):
        return self._limite

    @property
    def emprestimo(self):
        return self._emprestimo

    # Setters
    @emprestimo.setter
    def emprestimo(self, novo_valor):
        self._emprestimo = novo_valor

class Aluno(Usuario):
    def __init__(self, id, nome):
        Usuario.__init__(self, id, nome)
        self._limite = 1
    
class Professor(Usuario):
    def __init__(self, id, nome):
        Usuario.__init__(self, id, nome)
        self._limite = 3
        
class Exemplar:
    def __init__(self, id, titulo, tipo, autor, ano):
        self._id = id
        self._titulo = titulo
        self._tipo = tipo
        self._autor = autor
        self._ano = ano
        self._estado = "Disponível"

    # Getters
    @property
    def estado(self):
        return self._estado

    # Setters
    @estado.setter
    def estado(self, novo_estado):
        self._estado = novo_estado

# Funções
def emprestar(usuario, exemplar):
    if usuario.emprestimo == usuario.limite:
        print("Erro! Usuário ja atingiu o limite de empréstimos!")
    elif exemplar.estado == "Ocupado":
        print("Erro! Exemplar ja emprestado.")
    else:
        usuario.emprestimo += 1
        exemplar.estado = "Ocupado"
        print("Empréstimo realizado com sucesso!")

def devolver(usuario, exemplar):
    if usuario.emprestimo == 0:
        print("Não há nada para devolver!")
    elif exemplar.estado == "Disponível":
        print("O exemplar não está em posse deste usuário!")
    else:
        usuario.emprestimo -= 1
        exemplar.estado = "Disponível"
        print("Devolução realizada com sucesso!")


def main():
    print(" 1) cadastrar 3 livros e 2 periodicos")
    livro1 = Exemplar(1, "Hamlet", "Livro", "William Shakespeare", 1603)
    livro2 = Exemplar(2, "Dom Casmurro", "Livro", "Machado de Assis", 1899)
    livro3 = Exemplar(3, "Sherlock Holmes", "Livro", "J. K. Rowling", 2007)
    periodico1 = Exemplar(4, "Inference by Exclusion in Goffin Cockatoos (Cacatua goffini)", "Periódico", "Mark O'Hara, Alice M I Auersperg, Thomas Bugnyar, Ludwig Huber", 2015)
    periodico2 = Exemplar(5, "Megabacteriose em Calopsita (Nymphicus hollandicus)", "Periódico", "Laurien A C Filho, Júlio Cézar S Nascimento, Marleyne J A A L Amorim, Mercia R Barros, Roseana T D Moura", 2017)

    print(" 2) cadastrar 2 alunos e 2 professores")
    professor1 = Professor(1, "Joaquim da Costa")
    professor2 = Professor(2, "Roberto Pereira")
    aluno1 = Aluno(3, "Nícolas C Brisque")
    aluno2 = Aluno(4, "Daniel Alexsander")

    print(" 3) aluno1 empresta livro 1")
    emprestar(aluno1, livro1)
    print(" 4) aluno2 empresta livro 2")
    emprestar(aluno2, livro2)
    print(" 5) professor1 empresta livro1 ( erro, exemplar emprestado )")
    emprestar(professor1, livro1)
    print(" 6) professor1 empresta livro2 ( erro, exemplar emprestado )")
    emprestar(professor1, livro2)
    print(" 7) aluno1 empresta periodico1 ( erro, aluno1 já atingiu o limite )")
    emprestar(aluno1, periodico1)
    print(" 8) aluno1 devolve livro1")
    devolver(aluno1, livro1)
    print(" 9) aluno1 empresta periodico1")
    emprestar(aluno1, periodico1)
    print(" 10) professor2 empresta livro1")
    emprestar(professor2, livro1)
    print(" 11) professor2 empresta periodico1 (erro, exemplar emprestado )")
    emprestar(professor2, periodico1)
    print(" 12) professot2 empresta periodico2")
    emprestar(professor2, periodico2)
    print(" 13) aluno1 empresta livro3 ( erro, aluno1 atingiu limite de empréstimos )")
    emprestar(aluno1,livro3)

if __name__ == "__main__":
    main()