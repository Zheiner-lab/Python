
def ficha(a, b=0):
    global nome
    global gol


    print(f'Jogador {nome} fez {gol} gol(s) no campeonato')

nome = str(input('Digite o nome do jogador: '))
gol = str(input('Digite o número de gols: '))

if nome.strip() == '':
    nome = '<desconhecido>'
else:
    nome = nome
if gol.isalnum():
    gol = int(gol)
else:
    gol = 0

ficha(nome, gol)
