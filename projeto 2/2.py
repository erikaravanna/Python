import random
import os

# Função para exibir lista de afazeres
def mostrarAfazeres(afazeres):
    for id, afazer in enumerate(afazeres, start=1):
        print(f"{id}. {afazer}")

# Função para adicionar novo afazer
def adicionarAfazer(afazeres, descricao):
    novoAfazer = f"{len(afazeres)+1}.{descricao.capitalize()} []"
    afazeres.append(novoAfazer)
    print("Afazer registrado com sucesso!")

# Função para marcar afazer como concluído
def afazerConcluido(afazeres, identificador):
    if 1 <= identificador <= len(afazeres):
        afazer = afazeres.pop(identificador - 1)
        afazer = afazer[:-3] + "[x]"
        afazeres.insert(0, afazer)
        print("Afazer concluído!")
    else:
        print("Identificador inválido!")

# Função para editar afazer
def editarAfazer(afazeres, identificador, novaDescricao):
    if 1 <= identificador <= len(afazeres):
        afazer = afazeres[identificador - 1]
        statusBox = afazer[-3:]
        novoAfazer = f"{identificador}.{novaDescricao} {statusBox}"
        afazeres[identificador - 1] = novoAfazer
        print("Afazer editado com sucesso!")
    else:
        print("Identificador inválido!")

# Função para salvar afazeres em um arquivo
def salvarAfazeres(afazeres, nomeArquivo="afazeres.txt"):
    with open(nomeArquivo, "w") as arquivo:
        for afazer in afazeres:
            arquivo.write(afazer + "\n")

# Função para carregar afazeres de um arquivo
def carregarAfazeres(nomeArquivo="afazeres.txt"):
    afazeres = []
    if os.path.exists(nomeArquivo):
        with open(nomeArquivo, "r") as arquivo:
            afazeres = [linha.strip() for linha in arquivo]

    return afazeres

arquivoAfazeres = "afazeres.txt"
afazeres = carregarAfazeres(arquivoAfazeres)

while True:
    print("\n ========== Gerenciador de Afazeres ==========")
    print("1- Listar Afazeres")
    print("2- Adicionar Novo Afazer")
    print("3- Marcar Afazer Como Concluído")
    print("4- Editar Afazer")
    print("5- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrarAfazeres(afazeres)
    elif opcao == "2":
        descricao = input("Informe a descrição do novo afazer: ")
        adicionarAfazer(afazeres, descricao)
    elif opcao == "3":
        identificador = int(input("Afazer a ser marcado como concluído: "))
        afazerConcluido(afazeres, identificador)
    elif opcao == "4":
        identificador = int(input("Afazer a ser editado: "))
        novaDescricao = input("Digite a nova descrição do afazer: ")
        editarAfazer(afazeres, identificador, novaDescricao)
    elif opcao == "5":
        salvarAfazeres(afazeres, arquivoAfazeres)
        print("Afazeres salvos. Saindo...")
        break
    else:
        print("Opção inválida, tente novamente!")
