class Círculo:
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.141592653589793

    def perímetro(self):
        return 2 * self.pi * self.raio

    def área(self):
        return self.pi * self.raio ** 2


c = Círculo(2)
print(f"raio={c.raio}")
print(f"p={c.perímetro():.2f}")
print(f"a={c.área():.2f}")