def lista_nome():
  nome = []
  for i in range(3):
    n = input()
    nome.append(n)

  return nome

b = lista_nome()

for user in enumerate(b):
  indice,user = user
  print(indice,user)