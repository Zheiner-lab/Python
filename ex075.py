a1 = int(input('Digite um primeiro valor: '))
a2 = int(input('Digite um segundo valor: '))
a3 = int(input('Digite um terceiro valor: '))
a4 = int(input('Digite um quarto valor: '))
tu = a1 , a2 , a3 , a4
print(tu)
print(f'O número 9 apareceu {tu.count(9)} vezes na lista.')
if 3 in tu:
    print(f'O número 3 apareceu na {tu.index(3)+1} posição.')
else:
    print('Não há nenhum número 3.')
print('Os números pares foram ', end='')
for pares in tu:
    if pares % 2 == 0:
       print(pares, end=' ')