class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

c = Retangulo(2, 5)
print(f"p={c.perimetro():.2f}")
print(f"a={c.area():.2f}")
