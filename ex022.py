nome = input('Digite o nome completo da pessoa:').strip()
nmaisculo = nome.upper()
nminusculo = nome.lower()
nletras = len(''.join(nome.split()))  #Simplificando len(nome) - nome.count(' ') - Lembre-se operações funcionam com strings
nj= nome.split()
pnletras = len(nj[0]) #Simplificando nome.find(' ') - Ele conta quantos caracteres tem até o primeiro espaço.
print('Nome em maiusculo: {}'.format(nmaisculo))
print('Nome em minisculo: {}'.format(nminusculo))
print('O nome inteiro possui a quantidade de letras: {}'.format(nletras))
print('O primeiro nome tem a quantidade de letras: {}'.format(pnletras))

