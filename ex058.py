from time import sleep
from random import randint
num = 0
jogador = 0
print('O computador está pensando em número de 0 a 10')
sleep(1)
pc = randint(0,10)
while jogador != pc:
    jogador = int(input('Digite o valor que o pc pensou:'))
    if jogador > pc:
        print('Menos...Errou tente novamente!')
        num += 1
    else:
        print('Mais... Errou tente novamente!')
        num += 1
print('Você acertou! Foram {} tentativas até acertar.'.format(num))
