def leiaint(msg):
    while True:
        try:
            ientra = int(input(msg))
        except ValueError:
            print('Erro, digite um número inteiro!')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return ientra

def leiafloat(msg):
    while True:
        try:
            fentra = float(input(msg))
        except ValueError:
            print('Erro, digite um número inteiro!')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return fentra

n = leiaint('Digite um número inteiro:')
f = leiafloat('Digite um número real:')
print(f'Você digitou o número inteiro {n} e o real foi {f}')