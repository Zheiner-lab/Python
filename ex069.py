idade = 0
cont = 0
conth = 0
contf = 0
while True:
    idade = int(input('Digite a idade: '))
    if idade > 18:
        cont += 1

    while True:
        sexo = str(input('Digite o sexo [F/M]: ')).strip()
        if sexo in 'FfMm':
            break
    if sexo in 'Mm':
        conth += 1
    if idade > 20 and sexo in 'Ff':
        contf += 1

    conti = str(input('Quer continuar [S/N] ? ')).strip()
    print('-=-'*10)
    if conti in 'Nn':
        break

print(f'Ao total {cont} pessoas tem mais de 18 anos.')
print(f'Ao total {conth} são homens.')
print(f'Ao total {contf} mulheres tem mais de 20 anos.')