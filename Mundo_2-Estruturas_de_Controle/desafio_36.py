#aprovação de empréstimo para imóvel

valor = float(input('Valor do imóvel: R$ '))
salario = float(input('Valor do salário do comprador: R$ '))
periodo = int(input('Quantos anos vai pagar: '))
prestacao = valor / (periodo * 12)
print('Empréstimo de R${:.2f} em {} pestações o valor da prestação fica R${:.2f}'.format(valor, periodo, prestacao))
if prestacao <= (salario * 0.30):
    print('Empréstimo APROVADO')
else:
    print('Empréstimo NEGADO')
