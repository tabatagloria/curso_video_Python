#análise de peso

maior = 0
menor = 0
for i in range(5):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i+1)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso >  maior :
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido é: {}'.format(maior))
print('O menor peso lido é: {}'.format(menor))