def voto():
    import datetime
    idade =  datetime.date.today().year - ano
    if idade >= 18:
        if idade >= 70:
            print('VOTO OPICIONAL')
        else:
            print('VOTO OBRIGATÓRIO')
    else:
        print('AINDA NÃO PODE VOTAR')


ano = int(input('Em que ano você nasceu? '))
voto()