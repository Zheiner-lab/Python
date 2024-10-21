cont = 0
maior = 0
menor = 0
soma = 0
total = 0
pause = 'S'
while pause != 'N':
        if pause == 'S':
            num = int(input('Digite algum número inteiro: '))
            cont += 1
            soma += num
            if cont == 1:
                maior = num
                menor = num
            else:
                if num > maior:
                    maior = num
                if num < menor:
                    menor = num
            pause = str(input('Gostaria de continuar, S ou N?: ')).upper()

print('A soma dos valores foi {} e foram digitados {} números e a média dos valores foi {:.1f}'.format(soma, cont, soma/cont))
print('O maior valor digitado foi {} e o menor valor digitado foi {}'.format(maior,menor))

