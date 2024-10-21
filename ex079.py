lista = []
re = ''
while True:
    a = int(input('Digite um valor:'))
    if a not in lista:
        lista.append(a)
        print('O valor foi adicionado na lista')
    elif a in lista:
        print('O valor não foi adicionado, ele já está na lista')
    while True:
        re = str(input('Quer continuar [S/N] ? ')).upper()
        if re in 'NNÃO':
            break
        elif re in 'SSIM':
            break
        else:
            print('Erro tente novamente')
    if re in 'NNÃO':
        break
lista.sort()
print(f'Seus valores na ordem crescente são {lista}.')