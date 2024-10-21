tu = 'cachorro', 'gato', 'macaco', 'passaro'
for v in tu:
    print(f'\nNa palavra {v} temos as vogais ', end='')
    for letras in v:
        if letras in 'aeiou':
            print(letras, end=' ')

