times = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Cruzeiro', 'São Paulo', 'Bahia', 'Vasco',
         'Atlético-MG', 'Internacional', 'Bragantino', 'Athletico-PR', 'Criciúma', 'Juventude', 'Grêmio',
         'Fluminense', 'Corinthians', 'Vitória', 'Cuiabá', 'Atlético-GO')
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Os 4 últimos colocados são: {times[-4:]}')
print(f'Os times na ordem alfabética: {sorted(times)}')
print(f'O time no flamengo está na {times.index('Flamengo')+1}ª posição.')