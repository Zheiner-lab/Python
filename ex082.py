lista = []
listap = []
listai = []

while True:
    a = int(input('Digite um valor: '))

    lista.append(a)

    if a % 2 ==0:
        listap.append(a)

    elif a % 2 ==1:
        listai.append(a)

    while True:
        re = str(input('Quer continuar [S/N]? ')).upper()
        if re in 'SSIM':
            break
        elif re in 'NNÃO':
            break
        else:
            print('Erro tente novamente!')
    if re in 'NNÂO':
        break

print(f'Lista normal: {lista}')
print(f'Lista só com pares: {listap}')
print(f'Lista só com impares: {listai}')