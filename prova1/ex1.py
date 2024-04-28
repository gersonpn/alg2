#Escreva uma função Python que recebe uma lista e um cpf e então busca o(a) aluno(a) pelo cpf em uma lista de dicionários como no exemplo abaixo. Qual a complexidade do seu algoritmo no pior caso em notação O?


def busca(lista, cpf):
   for aluno in alunos:
       if aluno["cpf"] == cpf:
           return aluno

alunos = [
 {"nome": "João", "idade": 20, "cpf": "111.222.333-44"},
 {"nome": "Maria", "idade": 22, "cpf": "222.333.444-55"},
 {"nome": "Pedro", "idade": 21, "cpf": "333.444.555-66"},
 {"nome": "Ana", "idade": 19, "cpf": "444.555.666-77"},
 {"nome": "Lucas", "idade": 23, "cpf": "555.666.777-88"}
]
quem = busca(alunos,"555.666.777-88")
print(quem)