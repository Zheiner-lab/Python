money = float(input('Digite o seu sálario:R$'))
if money <= 1250.00:
    print('Seu sálario com aumento de 15% ficou R${:.2f}'.format(money+(money * 15 / 100)))
else:
    print('Seu salário com aumento de 10% ficou R${:.2f}'.format(money+(money * 10 / 100)))
