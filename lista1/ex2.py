alunos = []

for _ in range(1):
    aluno = {}
    aluno['nome'] = input("Nome: ")
    aluno['idade'] = input("Idade: ")
    aluno['notas'] = []

    for i in range(3):
        nota = float(input(f"Nota {i+1}: "))
        aluno['notas'].append(nota)
        
    notas = aluno['notas']
    media = (notas[0] * 1 + notas[1] * 2 + notas[2] * 3) / 6
    aluno['media'] = round(media, 2)
    alunos.append(aluno)

for aluno in alunos:
    aluno.pop('idade')


print(alunos)
