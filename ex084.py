
dados = list()
galera = list()
cont = 0
pesadas = list()
leves = list()
maiorp = menorp = 0
while True:
    n = str(input('Nome:')).upper()
    dados.append(n)
    p = int(input('Peso:'))
    dados.append(p)
    galera.append(dados[:])
    dados.clear()
    cont += 1
    r = input('QUER CONTINUAR [S/N]?').upper()
    if r in 'NNÃO':
        break

for pe in galera:

    if pe == galera[0]: # Define a primeira pessoa do laço como maior e menor peso
        maiorp = galera[0][1]
        menorp = galera[0][1]

    if pe[1] == maiorp:
        pesadas.append(pe[0])

    elif pe[1] == menorp:
        leves.append(pe[0])

    elif pe[1] > maiorp:
        pesadas.clear()
        pesadas.append(pe[0])
        maiorp = pe[1]  # Atualiza o maior peso

    elif pe[1] < menorp:
        leves.clear()
        leves.append(pe[0])
        menorp = pe[1]  # Atualiza o menor peso

print(f'A) Ao todo foram cadastradas {cont} pessoas.')
print(f'As pessoas mais pesadas foram {pesadas}')
print(f'As pessoas mais leves foram {leves}')





