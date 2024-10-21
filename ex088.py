import random
from time import sleep
t = int(input('Quantos jogos de MEGA SENA devo gerar?'))
for c in range(0,t):
    n = random.sample(range(1,61),6)
    print(n)
    sleep(1)
