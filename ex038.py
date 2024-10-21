num = int(input('Digite um número:'))
num2 = int(input('Digite um segundo número:'))
if num > num2:
    print('O primeiro valor {} é maior que o segundo {}.'.format(num, num2))
elif num < num2:
    print('O segundo valor {} é maior que o primeiro {}.'.format(num2, num))
else:
    print('Não existe valor maior, os dois valores são iguais.')