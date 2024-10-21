from random import randint


def maior(*num):
    tam = len(num)
    for c in range(0, len(num)):
        if c == 0:
            m = num[c]
        elif num[c] > m:
            m = num[c]
    print(f'Recebi os valores {num}, foram informados {tam} valores e o maior valor é {m}')

maior(6,5,4,3,2,1,10,13,20,4)
