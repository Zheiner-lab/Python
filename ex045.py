from random import randint
itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qual é a sua jogada?'))
print('-*-'*9)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-*-'*9)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador Venceu!')
    elif jogador == 2:
        print('Jogador Perdeu!')
    else:
        print('Jogada inválida')
elif computador == 1:
    if jogador == 0:
        print('Jogador Perder!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador Venceu!')
    else:
        print('Jogada inválida')
elif computador == 2:
    if jogador == 0:
        print('Jogador Ganhou!')
    elif jogador == 1:
        print('Jogador Perdeu!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida')