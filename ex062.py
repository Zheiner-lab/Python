print('Progressão Aritmética de 10 termos usando While')
a1 = int(input('Digite um primeiro termo:'))
r = int(input('Digite um número para ser a razão:'))
an = a1
cont = 1
total = 0
extra = 10

while extra != 0:
    total = total + extra
    while cont <= total:
        print('{}'.format(an), end=' -> ')
        an += r
        cont += 1

    print('Pausa')
    extra = int(input('Quantos termos a mais você quer? '))
print('Fim')
