#jogo da adivinhação

from random import randint #importa método randômico
from time import sleep #importa método sleep (programa dorme por alguns segundos)

sorteio = randint(0,5) #sorteia um número
numero = int(input('Escolha um número entre 0 e 5: ')) #solicita um número para o usuário

#mensagem de erro caso o usuário digite um número fora 
print('Processando...')
sleep(2)
if numero > 5 or numero < 0:
    print("Erro! Você escolheu um número fora do jogo!")

#printa a resposta se o usuário ganhou ou não
else:
    if numero == sorteio:
        print('Você Venceu. Parabéns!!!')
    else:
        print('Você Perdeu. Mais sorte na próxima vez')