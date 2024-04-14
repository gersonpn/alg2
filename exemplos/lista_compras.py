def compras(lista):
    opcoes = '\n'.join([f"{i+1}. {item}" for i, item in enumerate(lista)])
    escolha = input(f"Selecione uma opção:\n{opcoes}\n")
    return escolha

lista = []

minha_lista = ["inserir", "remover", "listar"]
opcao_selecionada = compras(minha_lista)

if opcao_selecionada == "1":
    produto = input("Escreva o nome do produto: ")
    lista.append(produto)

elif opcao_selecionada == "2":
    indice = int(input("Qual indice remover? "))
    if indice < len(lista):
        lista.pop(indice)
    else:
        print("Índice inválido.")

elif opcao_selecionada == "3":
    print(lista)