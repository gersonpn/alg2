class Cachorro:
    def __init__(self, nome, idade, castrado=False, raça="SRD"):
        self.nome = nome
        self.idade = idade
        self.castrado = castrado
        self.raça = raça


    def __str__(self):
        return f"{self.nome} {self.idade}"

    def __repr__(self):
      return vars(self)

pet = Cachorro("Montana",1,raça="ET+")
print(pet)
print(vars(pet))