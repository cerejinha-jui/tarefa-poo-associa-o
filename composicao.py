class Itempedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Pedido:
    def __init__(self, numero):
        self.numero = numero
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        item = Itempedido(produto, quantidade)
        self.itens.append(item)
        

item1 = Itempedido("jotabook", 2)
item2 = Itempedido("jotageladeira", 3)
pedido1 = Pedido(1)

pedido1.adicionar_item(item1, 2)
pedido1.adicionar_item(item2, 1)

for item in pedido1.itens:
   print(f"item: {item.produto} qnt: {item.quantidade} ")