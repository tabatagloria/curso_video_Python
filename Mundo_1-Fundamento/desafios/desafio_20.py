#sorteando nomes

import random
alunos = []
for x in range(4):
    alunos.append(input('Digite o nome do {}º aluno: '.format(x+1)))

random.shuffle(alunos)
print(alunos)
print('A ordem de apresentação será: {}'.format(alunos))