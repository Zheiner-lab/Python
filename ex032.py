from datetime import date
ano = int(input('Digite um ano ou coloque 0 para analisar o ano atual:'))
ano1 = ano%4
ano2 = ano%100
ano3 = ano%400

if ano == 0:
    ano = date.today().year
# forma simplificada: if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0
if (ano%4) + (ano%100) != 0:
    print('Seu ano é bissexto')
elif (ano%4) + (ano%100) + (ano%400) == 0:
    print('Seu ano é bissexto')
else:
    print('Seu ano não é bissexto')
