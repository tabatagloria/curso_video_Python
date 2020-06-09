#calcular o valor de um aluguel de carro

km = float(input('Quatidade de km percorrido: '))
dias = int(input('Quantos dias de aluguel: '))
total = (dias * 60.00) + (km * 0.15)
print('Valor Total: R${:.2f}'.format(total))