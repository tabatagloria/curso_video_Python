#conversão de número para bináio, octal ou hexadecimal
import math

numero = int(input('Digite um número: '))
print('Menu: ')
print('1 - Binário \n2 - Octal \n3 - Hexadecimal')
opcao = int(input('Escolha uma opção: '))
if opcao == 1:
    print('Binário: {}'.format(bin(numero)))
elif opcao == 2:
    print('Octal: {}'.format(oct(numero)))
else:
    print('Hexadeciaml: {}'.format(hex(numero)))