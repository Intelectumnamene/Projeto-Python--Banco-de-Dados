def nomes(primeiro_nome, ultimo_nome, nome_do_meio=''):
    nome_completo = {'Nome': primeiro_nome,
                     'Nome do Meio': nome_do_meio, 
                     'Último_nome': ultimo_nome}
    if nome_do_meio:
        print(primeiro_nome + ' ' + nome_do_meio + ' ' + ultimo_nome)
    else:
        print(primeiro_nome + ' ' + ultimo_nome)
    return nome_completo


dicionario = []
while True:
    encerrar = input(
        "Para finalizar digite 'S' para continuar aperte 'ENTER'. ")
    if encerrar.lower() == 's':
        break

    primeiro_nome = input("Digite seu primeiro nome: ")
    if primeiro_nome.lower() == 's':
        break
    nome_do_meio = input("Digite um segundo nome se houver: ")
    if nome_do_meio == 's':
        break
    ultimo_nome = input("DIgite seu último nome: ")
    if ultimo_nome == 's':
        break

    dicionario.append(nomes(primeiro_nome, nome_do_meio, ultimo_nome))

print("Nomes armazenados: ")

for nome in dicionario:
    print(nome)
