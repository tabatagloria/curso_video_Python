#conversão de número para bináio, octal ou hexadecimal
import math

numero = int(input('Digite um número: '))
print('Menu: ')
print('1 - Binário \n2 - Octal \n3 - Hexadecimal')
opcao = int(input('Escolha uma opção: '))5

if opcao == 1:
    print('Binário: {}'.format(bin(numero)[2:])) #[2:] só imprime o número eliminando o código que indica que é binário, octal ou hexadecimal
elif opcao == 2:
    print('Octal: {}'.format(oct(numero)[2:]))
elif opcao == 3:
    print('Hexadeciaml: {}'.format(hex(numero)[2:]))
else:
    print('Opção inválida! Tente novamente')                                                                                    