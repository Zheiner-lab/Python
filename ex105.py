def notas(*n, sit=False):
    dados = dict()
    dados['Quantidade'] = len(n)
    dados['Maior'] = max(n)
    dados['Menor'] = min(n)
    dados['Media'] = sum(n) / len(n)
    if sit:
        if dados['Media'] >= 7:
            dados['Situação'] = 'BOA'
        elif dados['Media'] >= 5:
            dados['Situação'] = 'RAZOÁVEL'
        else:
            dados['Situação'] = 'RUIM'
    return dados

#Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)