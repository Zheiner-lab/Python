vc = int(input('Qual a velocidade que o carro estava em km/h?'))
if vc < 80:
    print('Você não foi multado! :)')
else:
    print('Você foi multado em R${}'.format((vc-80)*7))
print('---Fim---')