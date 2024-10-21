dado = {}
pessoas = []
mulheres = []
cont = 0
sumage = 0
while True:
    dado['nome'] = str(input('Nome: ')).upper()
    dado['sexo'] = str(input('Sexo: ')).upper()
    dado['idade'] = int(input('Idade: '))
    cont += 1
    sumage += dado['idade']
    pessoas.append(dado.copy())

    if dado['sexo'] == 'F'or dado['sexo'] == 'FEMININO':
        mulheres.append(dado['nome'])

    re = str(input('Quer continuar [S/N]? ')).upper()
    if re in 'NNÃO':
        break
media = sumage/cont
print(dado)
print(pessoas)
print('='*20)

print(f'Ao total foram cadastradas {cont} pessoa(s).')
print(f'A media de idades foi de {media:.2f} anos.')
print(f'As mulheres cadastradas foram: {mulheres}')
print('PESSOAS ACIMA DA MEDIA DE IDADE')
for dado in pessoas:
    if dado['idade'] >= media:
        print(f'nome = {dado["nome"]}, idade = {dado["idade"]}, sexo = {dado["sexo"]}')