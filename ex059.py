escolha = 5
soma = 0
mult = 0
maior = 0
menu = 1

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um outro valor: '))
while escolha != 0:
    print('''
    --- Menu ---
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Exit
    ''')
    escolha = int(input('Digite sua escolha: '))
    if escolha == 1:
        soma = num1 + num2
        print('A soma dos valores {} + {} = {}.'.format(num1, num2, soma))
    if escolha == 2:
        mult = num1 * num2
        print('A multiplicação os valors {} x {} = {}.'.format(num1, num2, mult))
    if escolha == 3:
        if num1 > num2:
            print('Entre {} e {} o maior é {}'.format(num1, num2, num1))
        elif num1 < num2:
            print('Entre {} e {} o maior é {}.'.format(num1, num2, num2))
        else:
            print('Os valores {} e {} são iguais.'.format(num1, num2))
    if escolha == 4:
        print('Escolha novos valores')
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite um outro valor: '))
    if escolha == 5:
        escolha = 0
        print('Programa fechado.')


