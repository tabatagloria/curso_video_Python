#análise de triângulo

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r2 - r3 < r1 < r2 + r3 and r1 - r3 < r2 < r1 + r3 and r1 - r2 < r3 < r1 + r2:
    if r1 == r2 and r1 == r3 and r2 == r3: #outra forma de escrever: r1 == r2 == r3
        print('Triângulo Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3: 
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')

else:
    print('Não forma um triângulo')