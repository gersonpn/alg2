lista = []


for fruta in range (2):
    fruta = {}
    fruta["nome"] = input("nome: ")
    fruta["cor"] = input("cor: ")
    fruta["preco"] = eval(input("preco: "))
    fruta["quantidade"] = eval(input("quantidade: "))
    fruta["organico"] = input("organico (Sim ou Não): ").lower() == "sim"
    n = fruta["quantidade"] * fruta["preco"]
    n += n
    lista.append(fruta)

print(f"total R${n:.2f}")
