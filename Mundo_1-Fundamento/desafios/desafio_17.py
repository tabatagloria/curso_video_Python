#calculo da hipotenusa

from math import hypot

oposto = float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))
print('A hipotenusa é: {}'.format(hypot(oposto, adjacente)))
