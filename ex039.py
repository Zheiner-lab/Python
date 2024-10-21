from datetime import date
ano = int(input('Digite o ano que você nasceu:'))
idade = date.today().year - ano
if idade < 18:
    print('Você ainda irá se alistar, falta {} ano(s) para seu alistamento.'.format(18 - idade))
elif idade == 18:
    print('Você já tem 18 anos, deve se alistar imediatamente.')
else:
    print('Já se passaram {} ano(s) do tempo de alistamento.'.format(idade - 18))
