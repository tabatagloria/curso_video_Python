#porção inteira de um número Real

from math import trunc

num = float(input('Digite um número real: '))
print('Sua parte inteira é: {}'.format(trunc(num)))

#sem importação
print('Sua parte inteira é: {}'.format(int(num)))