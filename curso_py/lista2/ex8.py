class Círculo:
  def __init__(self, x, y, raio, cor = "transparente"):
    self.x = x
    self.y = y
    self.raio = raio
    self.cor = cor

  def perímetro(self):
    return 2 * (3.141592653589793 * self.raio)

  def área(self):
    return 3.141592653589793 * (self.raio * self.raio)

  def moveXY(self, a, b):
        self.x += a
        self.y += b


c = Círculo(0,0,1)
print(f"raio={c.raio}")
print(f"p={c.perímetro():.2f}")
print(f"a={c.área():.2f}")