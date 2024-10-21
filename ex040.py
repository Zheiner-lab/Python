n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1+n2) / 2
if m < 5.0:
    print('Sua média foi {:.1f}. REPOVADO!'.format(m))
elif m > 5.0 and m < 6.9:
    print('Sua média foi {:.1f}. RECUPERAÇÃO!'.format(m))
else:
    print('Sua média foi {}. APROVADO!'.format(m))