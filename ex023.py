num = input('Digita um número de 0 a 9999:')
n = num.zfill(4)
u = n[3:4]
d = n[2:3]
c = n[1:2]
m = n[0:1]
print('Unidade:{} Dezena:{} Centena:{} Milhar:{}'.format(u, d, c, m))

#Sem usar o zfill
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10