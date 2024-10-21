def aumentar(p):
    return p + (p * 10/100)

def diminuir(p):
    return p - (p * 10 / 100)

def dobro(p):
    return p * 2

def metade(p):
    return p / 2

def moeda(p):
    return f'R${p:.2f}'.replace('.',',')