frase = input('Digite uma frase:').strip()
txt = frase.replace(' ', '')
print(txt[::-1])

if txt == txt[::-1]:
    print('A frase é um palindromo')
else:
    print('Não é um palindromo')