#análise de idade
from datetime import date

ano = int(input('Digite o ano do seu nascimento: '))
genero = input('Escolha uma opção: \n1 - Masculino \n2- Feminino\n')
idade = date.today().year - ano
if genero == '1':
    if idade < 18:
        print('Você ainda vai se alistar ao serviço militar. Falta(m) {} ano(s) para o seu alistamento'.format(18 - idade))
    elif idade == 18:
        print('Já pode se alistar!!!')
    else:
        print('Já passou o prazo para o seu alistamento à {} ano(s)'.format(idade - 18))
else:
    print('Você não precisa fazer o alistamento obrigatório')
