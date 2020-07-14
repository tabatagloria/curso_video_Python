#análise de idade
from datetime import date

maior = 0
menor = 0
cont = 0
for i in range(7):
    idade = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i+1)))
    cont = date.today().year - idade
    if cont < 18:
        menor += 1
    else:
        maior += 1
print('Quantidade de pessoas menores de idade: {}'.format(menor))
print('Quantidade de pessoas maiores de idade: {}'.format(maior))