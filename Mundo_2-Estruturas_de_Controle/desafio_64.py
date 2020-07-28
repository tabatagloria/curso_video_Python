#tratando vários valores
n = calc = cont = 0
while n != 999:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        print('Fim')
    else:
        cont += 1
        calc = calc + n
print('Quantidade de números digitados foi {} e a sua soma é {}'.format(cont, calc))
print( 'Fim do programa')
