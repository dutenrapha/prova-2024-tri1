import csv

# Função para cadastrar um novo usuário
def cadastrar_usuario(nome, email, senha):
    with open('usuarios.csv', 'a', newline='') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        escrever.writerow([nome, email, senha])

# Função para listar todos os usuários cadastrados
def listar_usuarios():
    usuarios = []
    with open('usuarios.csv', 'r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            usuarios.append(linha)
    return usuarios
