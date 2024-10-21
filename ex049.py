v = int(input('Digite um valor para saber sua tabuada:'))
for c in range(1,11):
    print('{} X {:2} = {:2}'.format(v, c, c*v))
print('Fim')