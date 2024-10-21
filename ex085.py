dados = [[], []]
for c in range(0,7):
    n = int(input('Digite um valor:'))
    if n % 2 == 0:
        dados[0].append(n)
    elif n % 2 == 1:
        dados[1].append(n)

print(dados)
dados[0].sort()
dados[1].sort()
print(f'Os valores pares são {dados[0]}')
print(f'Os valores impares são {dados[1]}')
