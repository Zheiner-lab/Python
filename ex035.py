r1 = float(input('Digite o valor de uma reta A:'))
r2 = float(input('Digite o valor de uma reta B:'))
r3 = float(input('Digite o valor de uma reta C:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podem formar um triângulo')
else:
    print('Não podem formar um triângulo')