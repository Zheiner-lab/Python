expre = str(input('Digite sua expressão: ')).upper()
a1 = expre.count('(')
a2 = expre.count(')')
print(expre.count('('))
print(expre.count(')'))
if a1 == a2:
    print('Sua expressão está correta')
else:
    print('Sua expressão está com parenteses abertos')