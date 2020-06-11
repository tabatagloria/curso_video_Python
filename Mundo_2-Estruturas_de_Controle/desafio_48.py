#soma de números ímpares múltiplos de 3 com for

soma = 0
for i in range(1, 500):
    if i % 2 == 1 and i % 3 == 0:
        soma += i
print ('A soma dos números ímpares, múltiplos de 3 até 500 é: {}'.format(soma))