def esfera():
  raio = float(input())
  pi = 3.14159
  volume = (4/3) * pi * (raio ** 3)
  return volume


esfer = esfera()

print(f"VOLUME ={esfer: .3f}")