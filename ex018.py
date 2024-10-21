import math

num = math.radians(float(input('Digite um ângulo: ')))
print('Seu ângulo é {}, o seno {:.3f}, cosseno {:.3f} e tangente {:.3f}.'.format(math.ceil(math.degrees(num)) , math.sin(num), math.cos(num), math.tan(num)))