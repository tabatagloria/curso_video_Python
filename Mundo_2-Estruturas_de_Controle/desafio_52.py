#análise de número primo 
#ver correção

n = int(input('Digite um número: '))
if n <= 1:
    print('Número não é primo')
elif n == 2:
    print('É número primo: ')
elif n % 2 != 0 and n % 5 != 0 and n % 3 != 0 and n % 7 != 0:
    print('Número primo')
else:
    print('Número não é primo')

