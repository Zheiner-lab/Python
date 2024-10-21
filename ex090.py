dados = {'nome':'', 'media':'', 'situação':''}

dados ['nome'] = str(input('Nome do aluno: '))
dados ['media'] = float(input('Media da nota: '))
if dados ['media'] >= 7:
    dados ['situação'] = 'Aprovado'
else:
    dados ['situação'] = 'Reprovado'

print(f'O {dados["nome"]} teve sua media igual a {dados["media"]}, portanto ele foi {dados["situação"]}!')