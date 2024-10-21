lista = []
for c in range(0,5):
    lista.append(int(input('Digite um valor: ')))

print(lista)
print(f'O maior número da lista foi {max(lista)} e está na posição {lista.index(max(lista))}')
print(f'O menor número da lista foi {min(lista)} e está na posição {lista.index(min(lista))}')