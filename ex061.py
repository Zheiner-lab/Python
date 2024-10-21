print('Progressão Aritmética usando While')
a1 = int(input('Digite um primeiro termo:'))
r = int(input('Digite um número para ser a razão:'))
cont = 1
while cont <=10:
    print(a1, end=' -> ')
    cont += 1
    a1 += r
