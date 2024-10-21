tu = 'Lápis', 2.50, 'Caderno', 10.00, 'Bolsa', 35.50
cont = 0
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for p in range(0,len(tu)):
    if p % 2 == 0:
        print(f'{tu[p]:.<30}', end='')
    else:
        print(f'R$: {tu[p]:>5.2f}')



