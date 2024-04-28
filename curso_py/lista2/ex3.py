class Estudante:
    def __init__(self, nome, nota1=0, nota2=0, nota3=0):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3


aluno1 = Estudante("Marco Antônio", 5,6,7)
print(aluno1.__dict__)