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
    print('Você PERDEU! \nPedra quebra tesoura')
elif jokenpo == 'tesoura' and jogador == 'pedra':
    print('Você Ganhou!! \nPedra quebra tesoura')
elif jokenpo == 'pedra' and jogador == 'papel':
    print('Você Ganhou!! \nPapel embrulha a pedra')
elif jokenpo == 'papel' and jogador == 'pedra':
    print('Você PERDEU! \nPapel embrulha a pedra')
elif jokenpo == 'tesoura' and jogador == 'papel':
    print('Você PERDEU! \nTesoura corta papel')
elif jokenpo == 'papel' and jogador == 'tesoura':
    print('Você Ganhou!! \nTesoura corta papel')
else:
    print('EMPATOU!')
