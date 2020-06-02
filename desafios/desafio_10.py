#conversão para dólar com cotação à 3.27

valor = float(input('Quanto dinheiro você tem? R$'))
print('Você pode comprar US${:.2f}'.format(valor / 3.27))