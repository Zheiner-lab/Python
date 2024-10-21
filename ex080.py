lista = []
for c in range(0,5):
    a = int(input('Digite um valor: '))
    if c == 0 or a > lista[-1]:
        lista.append(a)
    else:
        pos = 0
        while pos < len(lista):
            if a <= lista[pos]:
                lista.insert(pos,a)
                break
            pos += 1
print(lista)