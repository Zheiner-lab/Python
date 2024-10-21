dados = list()
soma = 0
soma3 = 0

for c in range(0,9):
    n = int(input('Digite um número:'))
    dados.append(n)
    if n % 2 == 0: #print(f'A soma de todos os números pares é {soma}')
        soma += n

#print(f'A soma dos dados da terceira coluna é {soma3}')
soma3 = dados[2] + dados[5] + dados[8]

#print(f'O maior número da segunda linha é {maior}')
maior = 0

if dados[3] > dados[4] and dados[3] > dados[5]:
    maior = dados[3]
elif dados[4] > dados[3] and dados[4] > dados[5]:
    maior = dados[4]
else:
    maior = dados[5]

print(f'[ {dados[0]} ][ {dados[1]} ][ {dados[2]} ]\n'
      f'[ {dados[3]} ][ {dados[4]} ][ {dados[5]} ]\n'
      f'[ {dados[6]} ][ {dados[7]} ][ {dados[8]} ]')

print(f'A soma de todos os números pares é {soma}')
print(f'A soma dos dados da terceira coluna é {soma3}')
print(f'O maior número da segunda linha é {maior}')