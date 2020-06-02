#separando números

print('Separando numeros com String: ')
numero = input('Digite um número de 0 a 9999: ')
if len(numero) == 4:
    print('Unidade: {}'.format(numero[3]))
    print('Dezena: {}'.format(numero[2]))
    print('Centena: {}'.format(numero[1]))
    print('Milhar: {}'.format(numero[0]))

if len(numero) == 3:
    print('Unidade: {}'.format(numero[2]))
    print('Dezena: {}'.format(numero[1]))
    print('Centena: {}'.format(numero[0]))

if len(numero) == 2:
    print('Unidade: {}'.format(numero[1]))
    print('Dezena: {}'.format(numero[0]))

if len(numero) == 1:
    print('Unidade: {}'.format(numero[0]))
