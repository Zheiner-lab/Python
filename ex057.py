sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Dados inválidos, por favor digite novamente:')).strip().upper()
print('Obrigado!')
