
dados = list()
alunos = list()

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    alunos.append(dados[:])
    print(alunos)
    dados.clear()
    stop = str(input('QUER CONTINUAR [S/N]?')).upper()
    if stop in 'NNÃO':
        break
for c in range(0,len(alunos)):
    media = (alunos[c][1] + alunos[c][2]) / 2
    print(f'{c:<5}{alunos[c][0]:<10}{media:^10}')

while True:
    re = int(input('Digite o número do aluno para ver suas notas (DIGITE 999 PARA SAIR): '))
    if re == 999:
        break
    else:
        print(f'{alunos[re][0]:<10}{alunos[re][1]:^10}{alunos[re][2]:>10}')


