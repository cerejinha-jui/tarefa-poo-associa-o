class Jogador:
    def __init__(self, nome):
        self.nome = nome

class Equipe:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []
    
    def adicionar_jogadores(self, jogador):
        self.jogadores.append(jogador)
        

j1 = Jogador("Juiu")
j2 = Jogador("Juliao")

equipe = Equipe("tech team")

equipe.adicionar_jogadores(j1)
equipe.adicionar_jogadores(j2)

print(f"equipe: {equipe.nome}")
print("jogadores: ")

for jogador in equipe.jogadores:
    print(f"- {jogador.nome}")
