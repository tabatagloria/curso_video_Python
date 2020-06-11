#soma de números pares com for

soma = 0
for i in range(6):
    n = (int(input('digite o {}º número: '.format(i+1))))
    if n % 2 == 0:
        soma += n
print('A soma dos números pares são: {}'.format(soma))


    
