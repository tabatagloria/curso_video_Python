#jokenpô

from random import choice
from time import sleep
lista = ['pedra', 'papel', 'tesoura']
jokenpo = choice(lista)
jogador = input('Pedra, Papel ou Tesoura: ').lower()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('Computador: {} \nJogador: {} '.format(jokenpo.upper(), jogador.upper()))
if jokenpo == 'pedra' and jogador == 'tesoura':
    print('Você PERDEU! Pedra quebra tesoura')
elif jokenpo == 'tesoura' and jogador == 'pedra':
    print('Pedra quebra tesoura')
elif jokenpo == 'pedra' and jogador == 'papel':
    print('Papel embrulha a pedra')
elif jokenpo == 'papel' and jogador == 'pedra':
    print('Papel embrulha a pedra')
elif jokenpo == 'tesoura' and jogador == 'papel':
    print('Tesoura corta papel')
elif jokenpo == 'papel' and jogador == 'tesoura':
    print('Tesoura corta papel')
else:
    print('EMPATOU!')
