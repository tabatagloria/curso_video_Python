#sequência de Fibonacci
n = int(input('Digite um número: '))
calc = 1
cont = 0
while cont < n:
    cont += 1
    calc = calc + (calc - 1)
    print ('{} -> {}'.format(cont, calc))
    