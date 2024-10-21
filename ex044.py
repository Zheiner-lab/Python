valor = float(input('Digite o valor do produto:R$'))
print('Digite 1 para pagamento à vista/ cheque \n'
      'Digite 2 para pagamento à vista no cartão \n'
      'Digite 3 para pagamento em até 2x no cartão \n'
      'Digite 4 para pagamento em 3x ou mais no cartão')
mp = int(input('Digite sua escolha aqui:'))
if mp == 1:
    print('O valor à vista/ cheque fica R${} com 10% de desconto'.format(valor-(valor * 10 / 100)))
elif mp == 2:
    print('O valor à vista no cartão fica R${} com 5% de desconto'.format(valor-(valor* 5/ 100)))
elif mp == 3:
    print('O valor em 2x no cartão fica R${} preço normal do produto.'.format(valor))
elif mp == 4:
    print('O valor em 3x ou mais no cartão fica R${} com 20% de juros.'.format(valor+(valor * 20 / 100)))
else:
    print('Operação inválida.')