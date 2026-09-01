class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_dados(self):
       return f"{self.nome} | R$ {self.preco:.2f} | Estoque: {self.quantidade}

produto1 = Produto("pc gamer 9 portas eletrolux", 20000, 10)
produto1.mostrar_dados()