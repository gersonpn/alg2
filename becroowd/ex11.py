def vendedor():
  nome = input()
  return nome

def pagamento():
  porcentagem = 15
  salario = float(input())
  vendas = float(input())
  valor = (vendas * porcentagem) / 100
  salario_total = valor + salario
  return salario_total

user = vendedor()
t = pagamento ()

print(f"TOTAL = R$ {t: .2f}")