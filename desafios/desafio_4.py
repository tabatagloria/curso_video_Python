#mostrar o tipo primitivo de uma variavel, e suas informações

dado = input('Digite algo: ')
print('Tipo primitivo é {}'.format(type(dado)))
print('É numérico: {}'.format(dado.isnumeric()))
print('É alfanumérico: {}'.format(dado.isalnum()))
print('É alfabético: {}'.format(dado.isalpha()))
print('É maiúscula: {}'.format(dado.isupper()))
print('É minuscúla: {}'.format(dado.islower()))
print('Está capitalizada: {}'.format(dado.istitle()))

