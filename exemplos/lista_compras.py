def compras():
    while True:
        try:
            opcao = input("[I]nserir [A]pagar [L]istar: ").strip().lower()
            if opcao not in ["i", "a", "l"]:
                raise ValueError("Opção inválida. Por favor, escolha entre 'I', 'A' ou 'L'.")
            return opcao
        except ValueError as e:
            print(e)

def inserir(lista):
        produto = input("Escreva o nome do produto: ")
        lista.append(produto)
        return lista

def remover(lista):
    indice = int(input("Qual item remover? "))
    try:
         del lista[indice]
    except IndexError:
        print("Índice inválido.")
    return lista

def listar (lista):
    return lista


itens = []

while True:
    opcao_selecionada = compras()
    if opcao_selecionada == "i":
        itens = inserir(itens)
    elif opcao_selecionada == "a":
        itens = remover(itens)
    elif opcao_selecionada == "l":
        print("Lista de compras:", itens)
    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != "s" and continuar !=  "sim":
        break