lista = []
cont = 0
while True:
    a = int(input('Digite um valor: '))
    lista.append(a)
    cont +=1

    while True:
        re = str(input('Quer continuar [S/N]? ')).upper()
        if re in 'SSIM':
            break
        elif re in 'NNÃO':
            break
        else: print('Erro tente novamente')
    if re in 'NNÃO':
        break

print(f'A quantidade de números digitados foi {cont}')
lista.sort(reverse=True)
print(f'A lista decrescente: {lista}')
if 5 not in lista:
    print('O valor 5 não foi encontrado na lista')
else:
    print(f'O valor 5 foi encontrado na posição {lista.index(5)}')

