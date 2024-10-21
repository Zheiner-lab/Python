from random import randint
cont = 0
while True:
    num = int(input('Digite um número de 0 a 10: '))
    escolha = str(input('[P/I]?: ')).strip().upper()
    numpc = randint(0,10)
    soma = num + numpc
    if soma % 2 == 0 and escolha == 'I':
        print(f'Você jogou {num} e o computador {numpc}. Total é {soma} deu PAR')
        print(f'GAME OVER, você venceu {cont}.')
        break
    if soma % 2 != 0 and escolha == 'P':
        print(f'Você jogou {num} e o computador {numpc}. Total é {soma} deu IMPAR')
        print(f'GAME OVER, você venceu {cont}.')
        break
    if soma % 2 == 0 and escolha == 'P':
        print(f'Você jogou {num} e o computador {numpc}. Total é {soma} deu PAR')
        print('Você Venceu!')
    if soma % 2 != 0 and escolha == 'I':
        print(f'Você jogou {num} e o computador {numpc}. Total é {soma} deu IMPAR')
        print('Você venceu!')
    cont += 1





