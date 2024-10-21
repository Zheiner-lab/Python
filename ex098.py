from time import sleep

def contador(a, b, c):
    if c < 0:
        cp = c*-1
        print(f'Contagem de {a} até {b} de {cp} em {cp}')
        for c in range(a, b+c, c):
            print(c, end=' ')
        print()
        print('-=-' * 20)

    elif c == 0:
        c += 1
        print(f'Contagem de {a} até {b} de {c} em {c}')
        for c in range(a, b-c, -c):
            print(c, end=' ')
        print()
        print('-=-' * 20)

    elif a > b:
        print(f'Contagem de {a} até {b} de {c} em {c}')
        for c in range(a, b-c, -c):
            print(c, end=' ')
        print()
        print('-=-' * 20)

    else:
        print(f'Contagem de {a} até {b} de {c} em {c}')
        for c in range(a, b+c, c):
            print(c, end=' ')
        print()
        print('-=-'*20)


contador(1, 10, 1)
contador(10, 0, -2)

print('Agora é sua vez! Personalize a contagem:')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)