class Contador:
    def __init__(self, atual, maximo):
        self.maximo = maximo
        self.atual = atual
        self.inicio = atual

    def __iter__(self):
        self.atual = self.inicio
        return self

    def __next__(self):
        if self.atual < self.maximo:
            valor = self.atual
            self.atual += 1
            return valor
        else:
            raise StopIteration
