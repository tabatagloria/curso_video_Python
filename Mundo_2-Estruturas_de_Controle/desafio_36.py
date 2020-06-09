#aprovação de empréstimo para imóvel

valor = float(input('Valor do imóvel: '))
salario = float(input('Valor do salário do comprador: '))
periodo = int(input('Quantos anos vai pagar: '))
prestacao = valor / (periodo * 12)
if prestacao <= (salario * 0.30):
    print('Empréstimo APROVADO')
else:
    print('Empréstimo NEGADO')
