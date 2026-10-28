class Vendedor:
    def __init__(self, nome):
        self.nome = nome 

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        
class Pedido:
    def __init__(self, cliente, vendedor):
        self.cliente = cliente
        self.vendedor = vendedor

cliente = Cliente("jui")
vendedor = Vendedor("juliois")

pedido = Pedido(
    cliente, 
    vendedor
)
print(pedido.cliente.nome)
print(pedido.vendedor.nome)