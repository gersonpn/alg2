alunos = {
    "111.222.333-44": {"nome": "João", "idade": 20},
    "222.333.444-55": {"nome": "Maria", "idade": 22},
    "333.444.555-66": {"nome": "Pedro", "idade": 21},
    "444.555.666-77": {"nome": "Ana", "idade": 19},
    "555.666.777-88": {"nome": "Lucas", "idade": 23}
}

def busca(dicionario, cpf):
    return dicionario.get(cpf)

cpf = input("Qual CPF deseja buscar?: ")

if cpf in alunos:
    informacoes_aluno = busca(alunos, cpf)
    print(informacoes_aluno)
else:
    print("CPF não encontrado.")
