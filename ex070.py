total = 0
cont = 0
contb = 0
barato = 1
nbarato = ''
while True:
    print('-*-'*10)
    nome = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Digite o preço: R$ '))
    contb += 1
    total += preco
    if preco > 1000:
        cont += 1
    if contb == 1:
        barato = preco
        nbarato = nome
    else:
        if preco < barato:
            barato = preco
            nbarato = nome

    conti = str(input('Continuar [S/N]? ')).strip()
    if conti in 'Nn':
        break
print(f'O valor total gastou foi R$ {total:.2f}')
print(f'{cont} produtos custuram mais de R$ 1000.00')
print(f'{nbarato} foi o produto mais barato.')