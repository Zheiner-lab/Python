import math

n= int(input('Digite um número: '))
numx = n
resultado = 0
cont = 1
valor = 0
fat = math.factorial(n)
print('O valor em fatorial fica:')
print('{}! = {}'.format(n,n),end='')
while fat != n:
    valor = numx - cont
    n = n * valor
    cont += 1
    print(' x {}'.format(valor),end='')
print(' x 1 = {}'.format(fat))


