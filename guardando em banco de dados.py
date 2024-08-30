import sqlite3

# Conectando ao banco de dados (ou criando se não existir)
conexao = sqlite3.connect('cadastro_usuarios.db')
cursor = conexao.cursor()

# Criando a tabela de usuários (se não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)
''')

# Função para exibir o menu
def exibir_menu():
    print("\nMenu de Cadastro")
    print("1. Cadastrar usuário")
    print("2. Exibir usuários cadastrados")
    print("3. Sair")

# Função para cadastrar um usuário
def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    senha = input("Digite a senha do usuário: ")
    
    try:
        cursor.execute('''
        INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)
        ''', (nome, email, senha))
        conexao.commit()
        print("Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: E-mail já cadastrado. Tente outro.")

# Função para exibir todos os usuários cadastrados
def exibir_usuarios():
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("\nUsuários cadastrados:")
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}")

# Loop principal
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        exibir_usuarios()
    elif opcao == '3':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")

# Fechando a conexão com o banco de dados
conexao.close()
