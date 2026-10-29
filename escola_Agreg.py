class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
    
    def adicionar_alunos(self, aluno):
        self.alunos.append(aluno)


A1 = Aluno("juiu")
A2 = Aluno("jui")

turma = Turma("2° ano tds")

turma.adicionar_alunos(A1)
turma.adicionar_alunos(A2)

print(f"turma: {turma.nome}")
print("alunos: ")

for aluno in turma.alunos:
    print(f"- {aluno.nome}")
