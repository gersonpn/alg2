def funcionario():
    nome = int(input())
    return nome

def pagamento():
    valor_hora = float(input())
    horas = float(input())
    pagamento = horas * valor_hora
    return pagamento


# Chama as funções para obter os valores
numero_funcionario = funcionario()
salario = pagamento()

print(f"NUMBER = {numero_funcionario}\nSALARY = U${salario:.2f}")