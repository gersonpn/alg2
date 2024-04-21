frase = "Carro azul, preto e verde passando pela rua"

texto = frase.split(", ")

for i, frase in enumerate(texto):
  print(texto[i].strip(","))

print(texto)