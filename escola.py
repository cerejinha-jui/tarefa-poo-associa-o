class Professor:
    def __init__(self, nome):
        self.nome = nome 

class Turma:
    def __init__(self, nome):
        self.nome = nome
        
class Disciplina:
    def __init__(self, professor, turma):
        self.professor = professor
        self.turma = turma

professor1 = Professor("josemeira")
turma2 =Turma("2 tds")

disciplina = Disciplina(
    professor1, 
    turma2
)
print(disciplina.professor.nome)
print(disciplina.turma.nome)