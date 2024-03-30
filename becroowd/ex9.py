lista = []

while len(lista) < 4:
  n = int(input())
  lista.append(n)

diferencas = []
for i in range(len(lista) - 2):  # Ajuste para iterar até o penúltimo elemento
    produto_anterior = lista[i] * lista[i + 1]
    produto_atual = lista[i + 1] * lista[i + 2]
    diferenca = produto_atual - produto_anterior
    diferencas.append(diferenca)

print(diferencas)