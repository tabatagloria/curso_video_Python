#calculando fatorial com for
n = int(input('Digite um número: '))
fatorial = 1
for i in range(n, 0, -1):
    fatorial = fatorial * i
print('o fatorial de {} é: {}'.format(n, fatorial))