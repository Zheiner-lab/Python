from time import sleep

from colorama import Back, Style, Fore


def head():
    t = 'SISTEMA DE AJUDA PYTHON'
    print(Back.GREEN + Fore.LIGHTWHITE_EX + '-=-'*20)
    print( f'{t:^60}')
    print('-=-' * 20)
    print(Style.RESET_ALL)
def ajuda(a):
    print(Fore.BLACK+Back.LIGHTWHITE_EX)
    help(a)
    print(Style.RESET_ALL)


#PROGRAMA PRINCIPAL
head()
a = ''
while True:
    a = str(input('Biblioteca ou Função > '))
    if a in 'FimFIMfim':
        f = 'ATÉ LOGO!'
        print(Back.RED + Fore.LIGHTWHITE_EX + '-=-' * 20)
        print(f'{f:^50}')
        print('-=-' * 20)
        break
    else:
        ac = 'ACESSANDO -> ' + a
        print(Back.BLUE + Fore.LIGHTWHITE_EX + '-=-' * 20)
        print(f'{ac:^50}')
        print('-=-' * 20)
        sleep(1)
        ajuda(a)