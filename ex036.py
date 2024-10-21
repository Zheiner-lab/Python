valorcasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você gostaria de pagar?'))

if valorcasa / (anos * 12) > salario * 30 / 100:
    print('Infelizmente seu empréstimo não poderá ser feito.')
else:
    print('PARABÉNS, seu empréstimo foi aprovado!')