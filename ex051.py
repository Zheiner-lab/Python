print('Progressão Aritmética')
a1 = int(input('Digite um primeiro termo:'))
r = int(input('Digite um número para ser a razão:'))
an = a1 + (10 - 1) * r
for c in range(a1, an + r, r):
    print(c, end=' -> ')
print('inferno')