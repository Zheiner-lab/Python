num = int(input('Digite um número:'))
print('Sistema de Conversão')
conversao = int(input('Digite 1 para binário, 2 para octal e 3 para hexadecimal:'))
if conversao == 1:
    print('O número {} em binário é {}'.format(num,bin(num)[2:]))
elif conversao == 2:
    print('O número {} em octal é {}'.format(num,oct(num)[2:]))
elif conversao == 3:
    print('O número {} em hexadecimal é {}'.format(num,hex(num)[2:]))
