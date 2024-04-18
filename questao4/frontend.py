# Função para interface de cadastro de usuário
def interface_cadastro():
    print("=== Cadastro de Usuário ===")
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    senha = input("Digite a senha do usuário: ")
    return nome, email, senha

# Função para interface de listagem de usuários
def interface_listagem(usuarios):
    print("=== Lista de Usuários ===")
    for usuario in usuarios:
        print("Nome:", usuario[0])
        print("Email:", usuario[1])
        print("Senha:", usuario[2])
        print("-------------------------")

# Função principal para interação com o usuário
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Cadastrar novo usuário")
        print("2. Listar usuários cadastrados")
        print("3. Sair")
        opcao = input("Opção: ")

        if opcao == '1':
            nome, email, senha = interface_cadastro()
            cadastrar_usuario(nome, email, senha)
            print("Usuário cadastrado com sucesso!")
        elif opcao == '2':
            usuarios = listar_usuarios()
            interface_listagem(usuarios)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
