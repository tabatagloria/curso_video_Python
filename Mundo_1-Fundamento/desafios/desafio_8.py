#conversão de metros para quilometros, hectômetro, decametro, decimetros, centímetros e milímetros

metros = float(input('Digite o valor em metros: '))
quilometro = metros *  1000
hectometro = metros * 100
decametro = metros * 10
decimetro = metros / 10
centimetro = metros / 100
milimetro = metros / 1000
print('Valor em quilômetros: {}'.format(quilometro))
print('Valor em hectômetros: {}'.format(hectometro))
print('Valor em decametro: {}'.format(decametro))
print('Valor em decímetro: {}'.format(decimetro))
print('Valor em centímetros: {}'.format(centimetro))
print('Valor em milímetros: {}'.format(milimetro))