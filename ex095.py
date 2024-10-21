

dado = dict()
jogadores = list()
totalg = list()
partidas = list()
soma = 0

while True:

    dado['nome'] = str(input('Nome do jogador: '))
    pt = int(input('Quantas partidas ele jogou? '))
    for c in range(0,pt):
        gols = int(input(f'Quantos gols foram feitos na {c+1}ªpartida: '))
        totalg.append(gols)
        dado['gols'] = totalg
        soma += gols
        dado['total'] = soma
        partidas.append(pt)
    jogadores.append(dado.copy())
    soma = 0
    totalg = list()
    partidas = list()
    continuar = input('Quer continuar [S/N]?').upper()[0]
    if continuar == 'N':
        break

print('='*20)

print('cod', end='')
for i in dado.keys():
    print(f'{i:<15}', end='')
print()

for k, v in enumerate(jogadores):
        print(f'{k}', end=' ')
        for d in v.values():
            print(f'{str(d):<16}', end='')
        print()

print('='*20)

while True:
    busca = int(input('Mostrar dados de qual jogador?'))
    if busca == 999:
        break
    if busca > len(jogadores):
        print(f'Erro não existe jogador com código da busca.')
    else:
        print(f'--DADOS DO JOGADOR {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]["gols"]):
            print(f' No jogo {i+1} fez {g} gols')
    print('='*40)