from random import sample, random, shuffle

a1 = input('Digite o nome do aluno 01: ')
a2 = input('Digite o nome do aluno 02: ')
a3 = input('Digite o nome do aluno 03: ')
a4 = input('Digite o nome do aluno 04: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A sequência de apresentação ficará {}'.format(lista))