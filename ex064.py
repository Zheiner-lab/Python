num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite qualquer número inteiro:'))
    if num != 999:
        soma += num
        cont += 1
    else:
        print('A soma de todos os números digitados é {}'.format(soma))


print('fim')

