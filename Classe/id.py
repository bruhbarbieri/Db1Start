class Estudante:
    def __init__(self, ID, nome=None, turma=None):
        self.ID = ID
        self.nome = nome
        self.turma = turma

    def imprimir_informacoes(self):
        print(f'ID do aluno: {self.ID}')
        if self.nome is not None:
            print(f'Nome do aluno: {self.nome}')
        if self.turma is not None:
            print(f'Turma do aluno: {self.turma}')

aluno1 = Estudante(1)
aluno1.imprimir_informacoes()

aluno2 = Estudante(2, "João")
aluno2.imprimir_informacoes()

aluno3 = Estudante(3, "Maria", "A")
aluno3.imprimir_informacoes()



