#soma de números pares com for

soma = 0
cont = 0
for i in range(6):
    n = (int(input('digite o {}º número: '.format(i+1))))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A quantidade de números pares foi {} e sua é: {}'.format(cont, soma))


    
