dias = int(input('Por quantos dias o carro foi alugado?'))
kilometro = float(input('Quantos Km foram rodados?'))
dc = dias * 60
kc = kilometro * 0.15
total = dc + kc
print('O custo por dia ficou R$ {:.2f} e o custo por kilometros R$ {:.2f}. Totalizando R$ {:.2f}'.format(dc, kc, total))