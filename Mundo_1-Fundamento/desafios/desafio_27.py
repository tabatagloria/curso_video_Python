#mostrar o primeiro e ultimo nome

nome = str(input('Digite seu nome completo: ')).strip()
novo = nome.split()
print('Primeiro nome: {}'.format(novo[0]))
print('Último nome: {}'.format(novo[-1]))