d = float(input('Qual a distância da viagem em Km?'))
if d <= 200:
    print('O valor total ficou R${:.2f}'.format(d*0.5))
else:
    print('O valor total ficou R${:.2f}'.format(d*0.45))
