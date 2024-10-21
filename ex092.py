from datetime import datetime

dados = dict()
ano =  datetime.now()

dados['nome'] = str(input('Digite um nome: '))

idade = int(input('Digite o ano de nascimento: '))
dados['idade'] = ano.year - idade

carteira = int(input('Carteira de trabalho: '))

if carteira != 0:
    dados['carteira'] = carteira
    dados['contrato'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = float(input('Digite o salário: R$'))
    dados['aposentadoria'] = (dados['contrato'] + 35) - idade
    print(dados)
    print('-=-' * 10)
    for k, v in dados.items():
        print(f'{k} tem valor {v}')
else:
    print('-=-' * 10)
    for k, v in dados.items():
        print(f'{k} tem valor {v}')

