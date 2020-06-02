#sortear nomes
import random

nomes = []
for x in range(4):
        nomes.append(input('Digite o nome do {}º aluno: '.format(x+1)))

sorteado = random.choice(nomes)

print('O aluno escolhido foi: {}'.format(sorteado))