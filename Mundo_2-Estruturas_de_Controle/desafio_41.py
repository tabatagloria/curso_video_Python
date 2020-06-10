#análise de idade

from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
if idade <= 9:
    print('Idade: {} - Categoria: MIRIM'.format(idade))
elif idade <= 14:
    print('Idade: {} - Categoria: INFANTIL'.format(idade))
elif idade <= 19:
    print('Idade: {} - Categoria: JUNIOR'.format(idade))
elif idade <= 25:
    print('Idade: {} - Categoria: SÊNIOR'.format(idade))
else:
    print('Idade: {} - Categoria: MASTER'.format(idade))
