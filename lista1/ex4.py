lista = []


for fruta in range(1):
  fruta = {}
  fruta["nome"] = input("nome: ")
  fruta["cor"] = input("cor: ")
  fruta["preco"] = eval(input("preco: "))
  fruta["quantidade"] = eval(input("quantidade: "))
  fruta["organico"] = input("organico (Sim ou Não): ").lower() == "sim"
  lista.append(fruta)

print(" ".join(fruta.keys()))

print(" ".join(map(str, fruta.values())))