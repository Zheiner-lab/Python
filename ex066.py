num = 0
soma = 0
cont = 0
while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    soma += num
    cont += 1
(print(f'Ao total {cont} foram digitados e a soma entre eles é {soma}.'))
