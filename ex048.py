soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma entre todos os {} valores ímpares de 1 a 500 múltiplos de 3 é: {}'.format(cont, soma))