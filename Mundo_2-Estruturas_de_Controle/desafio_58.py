#jogo da adivinhação
from random import randint

sorteio = randint(0, 10)
jogador = 0
cont = 0
while jogador != sorteio:
    jogador = int(input('Digite um número entre 0 e 10: '))
    if jogador != sorteio:
        print('Errou!')
        cont += 1
print('Você acertou e precisou de {} palpites'.format(cont))