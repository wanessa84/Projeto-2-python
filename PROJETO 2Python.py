
#Projeto 02 - Gerenciador de Estoque
#Criar um sistema para gerenciar um pequeno estoque de produtos. O usuário
#pode adicionar, remover, listar e buscar produtos.
#Habilidades trabalhadas:
#• Uso de dicionários para armazenar dados
#• Laços (while) e condicionais (if)
#• Entrada e saída de dados (input( ), print( ))



def adicionar_produto(estoque):
    nome = input("Digite o nome do produto: ").strip()
    quantidade = int(input("Digite a quantidade: "))
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    print(f"Produto '{nome}' adicionado/atualizado com sucesso!")

def remover_produto(estoque):
    nome = input("Digite o nome do produto que deseja remover: ").strip()
    quantidade = int(input("Digite a quantidade: "))
    if nome in estoque:
        estoque[nome] -= quantidade
        print(f"Produto '{nome}' removido com sucesso!")
    else:
        print("Produto não encontrado no estoque.")

def listar_produtos(estoque):
    if not estoque:
        print("Estoque vazio.")
    else:
        print("Produtos no estoque:")
        for produto, quantidade in estoque.items():
            print(f"- {produto}: {quantidade} unidades")

def buscar_produto(estoque):
    nome = input("Digite o nome do produto para buscar: ").strip()
    if nome in estoque:
        print(f"Produto '{nome}' encontrado: {estoque[nome]} unidades")
    else:
        print("Produto não encontrado.")

def gerenciar_estoque():
    estoque = {}

    while True:
        print("\nMenu de opções:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Buscar produto")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            adicionar_produto(estoque)
        elif opcao == '2':
            remover_produto(estoque)
        elif opcao == '3':
            listar_produtos(estoque)
        elif opcao == '4':
            buscar_produto(estoque)
        elif opcao == '5':
            print("Encerrando o sistema de estoque. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o sistema
gerenciar_estoque()
