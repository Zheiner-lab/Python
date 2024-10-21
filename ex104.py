def leiaint(n = 'Digite um número'):
    while True:
        n = str(input('Digite um número: '))
        if n.isalpha() or n == '':
            print('Erro, digite um número valido!')
        if n.isnumeric():
            n = int(n)
            return n


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}.')
