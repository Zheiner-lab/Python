from time import sleep
from random import randint
print('-*-' * 20)
print('Computador está escolhendo um número inteiro entre 0 e 5...')
numpc = randint(0,5)
print('-*-' * 20)
num = int(input('Digite o número que o computador escolheu: '))
print('Hum...')
sleep(2)
if num == numpc:
    print('Você venceu :)')
else:
    print('Você perdeu :(')
print('---Fim---')