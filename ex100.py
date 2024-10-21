from random import randint

def sorteia(lista):
    print(f'Sorteando os valores da lista:', end=' ')
    for c in range(0,5):
        num = randint(1,10)
        numeros.append(num)
        print(num, end=' ')
    print('PRONTO!')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma de todos os valores pares de {lista}, temos {soma}')



numeros = list()
sorteia(numeros)
somapar(numeros)