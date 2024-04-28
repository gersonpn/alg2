class Pizza:
    def __init__(self, id, nome, ingredientes, tamanho, preco):
        self.id = id
        self.nome = nome
        self.ingredientes = ingredientes
        self.tamanho = tamanho
        self.preco = preco


    def __repr__(self):
        return f"{self.id}. {self.nome} R${self.preco:.2f}"


