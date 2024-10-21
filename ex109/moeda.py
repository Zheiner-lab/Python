def aumentar(p, sit=False):
    if sit:
        p = p + (p * 10 / 100)
        return f'R${p:.2f}'.replace('.', ',')
    else:
        return p + (p * 10 / 100)

def diminuir(p,sit=False):
    if sit:
        p = p - (p * 10 / 100)
        return f'R${p:.2f}'.replace('.', ',')
    else:
        return p - (p * 10 / 100)

def dobro(p,sit=False):
    if sit:
        p = p * 2
        return f'R${p:.2f}'.replace('.', ',')
    else:
        return p * 2

def metade(p,sit=False):
    if sit:
        p = p / 2
        return f'R${p:.2f}'.replace('.', ',')
    else:
        return p / 2

def moeda(p):
    return f'R${p:.2f}'.replace('.',',')