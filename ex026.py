txt = input('Digite uma frase: ').upper().strip()

print('Quantidade de letras A são:{}'.format(txt.count('A')))
print('Primeira aparição do A:{}'.format(txt.find('A')+1))
print('Ultima aparição do A:{}'.format(txt.rfind('A')+1))

