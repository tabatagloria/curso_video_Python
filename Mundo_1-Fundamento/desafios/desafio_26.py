#análise de frase

frase = str(input('Digite uma frase: ')).lower().strip()
print('Quantidade da letra A: {}'.format(frase.count('a')))
print('Posição que parece pela primeira vez na posição: {}'.format(frase.find('a') + 1))
print('Posição que aparece pela última vez: {}'.format(frase.rfind('a') + 1))