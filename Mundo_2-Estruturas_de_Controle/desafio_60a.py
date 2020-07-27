n = int(input('Digite um número: '))
fatorial = 1
n1 = n
while n != 0:
    fatorial = fatorial * n
    n = n - 1
print('O fatorial de {} é: {}'.format(n1,fatorial))