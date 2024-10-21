r1 = float(input('Digite o valor da reta A:'))
r2 = float(input('Digite o valor da reta B:'))
r3 = float(input('Digite o valor da reta C:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilatéro')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isoceles')
    else:
        print('Escaleno')

else:
    print('Não podem formar um triângulo')
