class Tartaruga:
    def __init__(self, nome, idade, castrado=False, raça="vira-lata"):
        self.nome = nome
        self.idade = idade
        self.castrado = castrado
        self.raça = raça


    def __str__(self):
        return f"{self.nome} {self.idade}"

    def __repr__(self):
        return str(self.__dict__)


import json
pet1 = Tartaruga("Hulk",1)
pet2 = Tartaruga("Tocha",2)
pet3 = Tartaruga("Bolinha",3)
lista = [pet1, pet2, pet3]
aux = str(lista)
aux = aux.replace("{","\n{")
print(aux)