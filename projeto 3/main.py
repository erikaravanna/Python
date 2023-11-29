from produto import Produto

def cadastrarProduto(produtos):
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ").capitalize()
    preco = float(input("Digite o preço do produto: "))

    produto = Produto(codigo, nome, preco)
    produtos.append(produto)
    print("Produto cadastrado com sucesso")

def excluirProduto(produtos):
    codigo = input("Digite o código do produto a ser excluído: ")
    for produto in produtos:
        if produto.codigo == codigo:
            produtos.remove(produto)
            print("Produto excluído com sucesso!")
            return
    print("Produto não encontrado.")

def listarProdutos(produtos):
    for produto in produtos:
        print(produtos)

def consultarPrecos(produtos):
    codigo = input("Digite o código do produto para consultar o preço: ")
    for produto in produtos:
        if produto.codigo == codigo:
            print(f"O preço do produto {produto.nome} é R${produto.preco:.2f}")
            return
    print("Produto não encontrado.")

def menu():
    produtos = []

    while True:
        print("\n====== MENU ======")
        print("1. Inserir novo produto")
        print("2. Excluir produto")
        print("3. Listar produtos")
        print("4. Consultar preço de um produto")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cadastrarProduto(produtos)
        elif opcao == "2":
            excluirProduto(produtos)
        elif opcao == "3":
            listarProdutos(produtos)
        elif opcao == "4":
            consultarPrecos(produtos)
        elif opcao == "0":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
