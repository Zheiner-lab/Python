mult = 1
cont = 1
while True:
    num = int(input('Digite um valor para ver sua tabuada: '))
    print('-=-' * 10)
    if num <= 0:
        break
    while True:
        mult = num * cont
        print(f'{num} X {cont:2} = {mult:2}')
        cont += 1
        if cont >= 11:
            cont = 1
            break
    print('-=-' * 10)