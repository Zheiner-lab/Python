from operator import itemgetter
from random import randint
from time import sleep

dados = {}
lista = []
for j in range(0,4):
    dados['jogador 1'] = randint(1,7)
    dados['jogador 2'] = randint(1, 7)
    dados['jogador 3'] = randint(1, 7)
    dados['jogador 4'] = randint(1, 7)

ranking = list()
print(lista)
print(dados)

for k, v in dados.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('----- RANKING -----')
for i, v in enumerate(ranking):
    print(f'O {i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)