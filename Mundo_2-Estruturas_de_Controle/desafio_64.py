#tratando vários valores
n = 0
calc = 0
cont = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        print('Fim')
    else:
        cont += 1
        calc = calc + n
print('Quantidade de números digitados foi {} e a sua soma é {}'.format(cont, calc))
