#manipulando strings

nome = str(input('Digite seu nome completo: ')).strip()
novo = nome.split()
print ('Nome em Maiúculo: {}'.format(nome.upper()))
print('Nome em Minúsculo: {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(len(nome.replace(' ', ''))))
print('Quantidade de letras 1º nome: {}'.format(len(novo[0])))