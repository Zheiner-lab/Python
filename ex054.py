from _pydatetime import datetime
ano = datetime.today().year
cont = 0
cont2 = 0
print(ano)
for c in range(1,8):
    id = int(input('Digite o ano de nascimento:'))
    idade = ano - id
    if idade > 17:
        cont = cont + 1
    elif idade < 17:
        cont2 = cont2 + 1
print('O número de pessoas maiores de idade é {}'.format(cont))
print('O número de pessoas menores de idade é {}'.format(cont2))




