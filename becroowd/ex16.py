def calcular_dist():
  km = int(input())
  litros = float(input())
  distancia = km / litros
  return distancia


n = calcular_dist()

print(f"{n:.3f} km/l")
