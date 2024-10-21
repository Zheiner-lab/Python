from time import sleep
def menu():
    print('='*50)
    print('M E N U'.center(50))
    print('=' * 50)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do Sistema')
    print('=' * 50)

def cadastro():
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    with open('cadastro.txt', 'a') as arquivo:
        arquivo.write(f"{nome};{idade}\n")
        print("Pessoa cadastrada com sucesso!")

def listar_pessoas():
  with open('cadastro.txt', 'r') as arquivo:
    for linha in arquivo:
      nome, idade = linha.strip().split(';')
      print(f"{nome:<10} {idade:>10} anos")


#PROGRAMA PRINCIPAL
pessoas = list()
pessoa = dict()
while True:
    try:
        sleep(1)
        menu()
        escolha = int(input('Sua Opção: '))
        if escolha == 1:
            listar_pessoas()

        elif escolha == 2:
            cadastro()

        elif escolha == 3:
            print('Obrigado!')
            break
        else:
            print('Digite uma opção existente!')
    finally:
        print('')