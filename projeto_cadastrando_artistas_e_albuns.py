def make_album(nome_artista, album_artista, numero_faixa=''):
    dicionario = {'Artista': nome_artista, 'Álbum': album_artista}
    if dicionario:
        dicionario['numero_faixa'] = numero_faixa

    return dicionario


dicionarios = []

while True:
    encerrar = input("\nDeseja encerrar o programa [s/n]: ")
    if encerrar.lower() == 's':
        break

    nome_artista = input("Nome do artista: ")
    if nome_artista.lower() == 's':
        break

    album_artista = input("Álbum do artista: ")
    if album_artista.lower == 's':
        break

    numero_faixas = (input("Numero de faixas: "))
    if numero_faixas.lower == 's':
        break

    dicionarios.append(make_album(nome_artista, album_artista, numero_faixas))

print("Os artistas Cadastrados foram: ")
# for artista in dicionarios:
#     print(artista)
print(dicionarios)
