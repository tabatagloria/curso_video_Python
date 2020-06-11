#análise de peso
#assistir video


maior = 0
menor = 0
for i in range(5):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i+1)))
    if maior < peso:
        maior = peso
    else:
        aux = maior
        if peso > aux:
            menor = peso
print(maior, menor)