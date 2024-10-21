num = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze','catorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
n = int(input('Digite um número entre 0 e 20:'))
while True:
    if n < 0 or n > 20:
        n = int(input('Tente novamente 0 e 20:'))
    else:
        print(f'O número {n} em extenso é {num[n]}.')
        break