num = int(input('Digite um número inteiro: '))
num1 = 0
num2 = 1
cont = 3
print('{} -> {} -> '.format(num1, num2), end='')
while cont <= num:
    num3 = num1 + num2
    print('{} -> '.format(num3), end='')
    num1 = num2
    num2 = num3
    cont += 1
print('Fim')






