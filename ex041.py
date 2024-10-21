from datetime import date
ano = int(input('Digite o ano de nascimento:'))
idade = date.today().year - ano
if idade <= 9:
    print('Sua categoria de natação é Mirim')
elif idade > 9 and idade <= 14:
    print('Sua categoria de natação é Infantil')
elif idade > 14 and idade <= 19:
    print('Sua categoria de natação é Junior')
elif idade == 20:
    print('Sua categoria de natação é Sênior')
else:
    print('Sua categoria de natação é Master')