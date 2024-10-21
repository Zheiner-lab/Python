from utilidadeCeV import dado

def aumentar(p, b, c, sit=False):
    if sit:
        p = p + (p * b / 100)
        return f'R${p:.2f}'.replace('.', ',')
    else:
        return p + (p * b / 100)

def diminuir(p, b, c,sit=False):
    if sit:
        p = p - (p * c / 100)
        return f'R${p:.2f}'.replace('.', ',')
    else:
        return p - (p * c / 100)

def dobro(p, b, c,sit=False):
    if sit:
        p = p * 2
        return f'R${p:.2f}'.replace('.', ',')
    else:
        return p * 2

def metade(p, b, c, sit=False):
    if sit:
        p = p / 2
        return f'R${p:.2f}'.replace('.', ',')
    else:
        return p / 2

def moeda(p, b, c):
    return f'R${p:.2f}'.replace('.',',')

def resumo(p, b, c):
    print('-'*50)
    t = 'RESUMO DO VALOR'
    print(f'{t:^50}')
    print('-' * 50)
    print('Preço analisado:', end=f'{moeda(p,b,c):>34}\n')
    print('Dobro do preço:', end=f'{dobro(p,b,c,sit=True):>35}\n')
    print('Metade do preço:', end=f'{metade(p,b,c,sit=True):>34}\n')
    print(f'{b}% de aumento:', end=f'{aumentar(p,b,c,sit=True):>35}\n')
    print(f'{c}% de redução:', end=f'{diminuir(p,b,c,sit=True):>35}\n')
    print('-' * 50)