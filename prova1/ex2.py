alunos = [
    {'nome': 'João', 'idade': 20, 'cpf': '111.222.333-44'},
    {'nome': 'Maria', 'idade': 22, 'cpf': '222.333.444-55'},
    {'nome': 'Pedro', 'idade': 21, 'cpf': '333.444.555-66'},
    {'nome': 'Ana', 'idade': 19, 'cpf': '444.555.666-77'},
    {'nome': 'Lucas', 'idade': 23, 'cpf': '555.666.777-88'}
]

file = open("alunos.txt", "w")
file.write("nome,idade,cpf\n")
for aluno in alunos:
    linha = f"{aluno['nome']},{aluno['idade']},{aluno['cpf']}\n"
    file.write(linha)
file.flush()
file.close()
