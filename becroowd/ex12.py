def peca1():
  codigo,quantidade,valor = map(float, input().split())
  preco = quantidade * valor
  return preco

def peca2():
  codigo, quantidade, valor = map(float, input().split())
  preco = quantidade * valor
  return preco


p1 = peca1()
p2 = peca2()

total = p1 + p2

print(f"VALOR A PAGAR: R${total: .2f}")
