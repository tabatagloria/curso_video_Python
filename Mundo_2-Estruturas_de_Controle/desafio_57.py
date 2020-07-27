#validação de dados

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite o seu sexo M ou F: ').strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Dado inválido!')
    else:
        print('Dado registrado com sucesso')
