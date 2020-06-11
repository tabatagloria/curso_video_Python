#análise de informação

media = 0
velho = 0
calc = 0
for i in range(4):
    print('{}ª Pessoa: '.format(i+1))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = int(input('1 - Masculino ou 2 - Feminino '))
    media += idade
    if sexo == 1 and velho < idade:
        nome2 = nome
    elif sexo == 2 and idade > 20:
        calc += 1

print('Média de idade: {}'.format(media / 4))
print('Homem mais velho: {}'.format(nome))
print('Quantidade de mulheres com menos de 20 anos: {}'.format(calc))
