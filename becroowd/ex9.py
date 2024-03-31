valores = []

for _ in range(4):
    valor = int(input())
    valores.append(valor)

produto_AB = valores[0] * valores[1]
produto_CD = valores[2] * valores[3]
diferenca = produto_AB - produto_CD

print("DIFERENCA =", diferenca)
