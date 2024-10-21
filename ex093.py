dados = dict()
totalg = list()
soma = 0
dados['nome'] = str(input('Nome do jogador: '))

pt = int(input('Quantas partidas ele jogou? '))

for c in range(0,pt):
    gols = int(input(f'Quantos gols foram feitos na {c+1}ªpartida: '))
    totalg.append(gols)
    soma += gols

dados['gols'] = totalg
dados['total'] = soma

print('='*20)
print(dados)
print('='*20)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('='*20)

print(f'O jogador {dados["nome"]} jogou {pt} partidas')
for c in range(0,pt):
    print(f'Na partida {c+1}, fez {totalg[c]} gol(s)')