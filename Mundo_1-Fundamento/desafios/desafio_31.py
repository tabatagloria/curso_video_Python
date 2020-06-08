#preço da passagem

distancia = float(input('Digite a distância da viagem em km: '))
if distancia <= 200:
    preco = distancia * 0.5
    print('Total da passagem: R${:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('Total da passagem: R${:.2f}'.format(preco))