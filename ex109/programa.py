import moeda

p = float(input('Digite o preço R$:'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, sit=True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,sit=True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p)}')
print(f'Reduzindo 10%, temos {moeda.diminuir(p)}')