class Paciente:
    def __init__(self, nome):
        self.nome = nome 

class Medico:
    def __init__(self, nome):
        self.nome = nome
        
class Consulta:
    def __init__(self, paciente, medico):
        self.paciente = paciente
        self.medico = medico

paciente = Paciente("jui")
medico = Medico("juliois")

consulta = Consulta(
    paciente, 
    medico
)
print(consulta.paciente.nome)
print(consulta.medico.nome)