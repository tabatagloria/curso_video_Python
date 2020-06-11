#análise de idade

maior = 0
menor = 0
for i in range(7):
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i+1)))
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('Quantidade de pessoas menores de idade: {}'.format(menor))
print('Quantidade de pessoas maiores de idade: {}'.format(maior))