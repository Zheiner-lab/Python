import math
def fatorial(a, show:False):
    if show:
        f = 0
        print('-'*50)
        print(f'{a} x ', end='')
        for c in range(0,a-1):
            f +=  1
            r = a - f
            print(f'{r} x ', end='')
        print(f'= {math.factorial(a)}')
    else:
        fatorial = math.factorial(a)
        return fatorial


print(fatorial(5,False))